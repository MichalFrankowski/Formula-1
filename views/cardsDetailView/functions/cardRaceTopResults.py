import fastf1 
import pandas as pd
import streamlit as st

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_event(year, card_id):
    return fastf1.get_event(int(year), int(card_id)) 

def card_race_top_results(year, card_id):
    # Get the the evnet
    final_race_event = load_event(year, card_id)

    # Get the race session from the final event
    race = final_race_event.get_race()

    # Load the session results
    race.load()

    # Get the top 3 drivers
    top_3 = race.results.head(3)

    # Clean up the race time by removing "0 days"
    clean_race_times = top_3['Time'].apply(lambda x: str(x).replace('0 days ', '').split('.')[0])

    # Create a DataFrame with selected columns
    df_top_3 = pd.DataFrame({
        'Position': top_3['Position'],
        'FullName': top_3['FullName'],
        'TeamName': top_3['TeamName'],
        'Race Time': clean_race_times
    })

    # Convert Position to integer
    df_top_3['Position'] = top_3['Position'].astype(int)

    # Return the DataFrame
    return df_top_3

if __name__ == "__main__":
    card_race_top_results()