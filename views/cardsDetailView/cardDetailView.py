import streamlit as st
import pandas as pd 
import fastf1
import flagpy as fp

from views.cardsDetailView.functions.cardTrack import cards_draw_track

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_event(year, card_id):
    return fastf1.get_event(int(year), int(card_id))

def cards_detail_view():
    # fetching URL parameters
    params = st.query_params
    year = params.get("year")
    card_id = params.get("card_id")
    
    # fetching event data
    #event = fastf1.get_event(int(year), int(card_id))
    event_details = load_event(int(year), int(card_id))
    #print(event)
    
    #### Header Section ####
    OfficialEventName = event_details["OfficialEventName"]
    
    header = st.columns([1, 7], vertical_alignment="bottom", gap="small")
  
    flag_placeholder = header[0].empty()
    header[1].header(OfficialEventName)
    
    st.divider()
    #### Subheader Section ####
    # Select the required subheader columns
    subheader_selection= ["Country", "Location", "EventDate"]

    # Create columns for subheaders
    subheader = st.columns([1, 1, 1, 1 ,2], vertical_alignment="center", gap="small")

    # Loop through the selected subheader columns and display each one
    circut_placeholder = subheader[0].empty()
    for idx, col in enumerate(subheader_selection, start=1):
        if col == "EventDate":
            # Format the EventDate
            event_date = pd.Timestamp(event_details[col]).strftime('%d %b %Y')
            subheader[idx].text(col)
            subheader[idx].subheader(event_date)
            
        else:
            subheader[idx].text(col)
            subheader[idx].subheader(event_details[col])
    
        
    st.divider()
    
    #### Show Events Date/Time Section ####
    # Select the required session and date/time columns 
    session_selection= ["Session1", "Session2", "Session3","Session4", "Session5"]
    time_date_selection= ["Session1DateUtc", "Session2DateUtc", "Session3DateUtc","Session4DateUtc", "Session5DateUtc"]

    event_session = st.columns([3, 3, 3, 3, 3], vertical_alignment="bottom", gap="small")

    # Loop through the session and time/date columns simultaneously
    for idx, (session_col, time_date_col) in enumerate(zip(session_selection, time_date_selection)):
        session_name = event_details[session_col]
        session_time = pd.Timestamp(event_details[time_date_col]).strftime('%d %b %Y %H:%M UTC')
        
        # Display session name and time using st.metric
        #event_session[idx].metric(label=session_name, value=session_time)
        event_session[idx].text(session_name)
        event_session[idx].subheader(session_time)
        
    st.divider()
    with st.expander("F1 Data"): 
        df_event_api = pd.DataFrame([event_details])
        st.table(df_event_api)
        
    #### Placeholders Section ####
    # adjusting the country names for flagpy lib
    if event_details["Country"] in ['United Kingdom','United States','Netherlands', 'United Arab Emirates']:
        event_details["Country"] = str('The ' + event_details["Country"])
     
    with st.spinner('Loading Flag Data...'):
        flag_img = fp.get_flag_img(event_details["Country"])
        flag_placeholder.image(flag_img)
    
    with circut_placeholder:
        with st.spinner('Loading Track Data...'):
            fig = cards_draw_track(year, card_id)
            # Display the figure using Streamlit
    
    circut_placeholder.plotly_chart(fig, theme="streamlit")
    
if __name__ == "__main__":
    cards_detail_view()
