import streamlit as st
import pandas as pd 
import fastf1

def cards_detail_view():
    # fetching URL parameters
    params = st.query_params
    year = params.get("year")
    card_id = params.get("card_id")
    
    # fetching event data
    event = fastf1.get_event(int(year), int(card_id))
    
    #### Header Section ####
    OfficialEventName = event["OfficialEventName"]
    st.header(OfficialEventName)
    
    #### Subheader Section ####
    # Select the required subheader columns
    subheader_selection= ["Country", "Location", "EventDate"]

    # Create columns for subheaders
    header = st.columns([2, 2, 4, 6], vertical_alignment="bottom", gap="small")

    # Loop through the selected subheader columns and display each one
    for idx, col in enumerate(subheader_selection):
        if col == "EventDate":
            # Format the EventDate
            event_date = pd.Timestamp(event[col]).strftime('%d %b %Y')
            header[idx].subheader(f"{col}: {event_date}")
        else:
            header[idx].subheader(f"{col}: {event[col]}")
            
    st.divider()
    #### Show Events Date/Time Section ####
    # Select the required session and date/time columns 
    session_selection= ["Session1", "Session2", "Session3","Session4", "Session5"]
    time_date_selection= ["Session1DateUtc", "Session2DateUtc", "Session3DateUtc","Session4DateUtc", "Session5DateUtc"]

    event_session = st.columns([3, 3, 3, 3, 3], vertical_alignment="bottom", gap="small")

    # Loop through the session and time/date columns simultaneously
    for idx, (session_col, time_date_col) in enumerate(zip(session_selection, time_date_selection)):
        session_name = event[session_col]
        session_time = pd.Timestamp(event[time_date_col]).strftime('%d %b %Y %H:%M UTC')
        
        # Display session name and time using st.metric
        #event_session[idx].metric(label=session_name, value=session_time)
        event_session[idx].text(session_name)
        event_session[idx].subheader(session_time)
        
    st.divider()
    with st.expander("F1 Data"): 
        st.table(event)
