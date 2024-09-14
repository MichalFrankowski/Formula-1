import streamlit as st
import fastf1
import numpy as np
import plotly.express as px
import 

# Cache the data fetching process to prevent re-fetching on every interaction
@st.cache_data
def load_session(year, card_id):
    return fastf1.get_session(int(year), int(card_id), 'Q')

def cards_draw_track(year, card_id):

    # Load session data
    session = load_session(year,card_id)
    session.load()

    # Get the fastest lap and its position data
    lap = session.laps.pick_fastest()
    pos = lap.get_pos_data()

    # Get circuit information
    circuit_info = session.get_circuit_info()

    def rotate(xy, *, angle):
        rot_mat = np.array([[np.cos(angle), np.sin(angle)],
                            [-np.sin(angle), np.cos(angle)]])
        return np.matmul(xy, rot_mat)

    # Convert the position data into a numpy array
    track = pos.loc[:, ('X', 'Y')].to_numpy()

    # Convert the rotation angle from degrees to radians
    track_angle = circuit_info.rotation / 180 * np.pi

    # Rotate the track
    rotated_track = rotate(track, angle=track_angle)

    # Close the loop by appending the first point to the end
    rotated_track = np.append(rotated_track, [rotated_track[0]], axis=0)

    # Create a Plotly Express line plot to connect the points
    fig = px.line(x=rotated_track[:, 0], y=rotated_track[:, 1])

    # Customize the layout: hide axes, gridlines, set the aspect ratio, and make the line bolder
    fig.update_traces(line=dict(width=4))  # Make the line bolder
    fig.update_layout(
        showlegend=False,
        xaxis=dict(
            visible=False,  # Hide the entire x-axis
            scaleanchor="y",  # Lock aspect ratio
            scaleratio=1.2,
        ),
        yaxis=dict(
            visible=False  # Hide the entire y-axis
        ),
        margin=dict(l=15, r=15, t=15, b=15),  # Adjust margins

        # Set the width and height of the figure
        width=100,   # Set the width of the figure (in pixels)
        height=150   # Set the height of the figure (in pixels)
    )

    return fig

if __name__ == "__main__": 
      cards_draw_track()

