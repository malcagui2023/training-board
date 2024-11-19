import streamlit as st
from mplsoccer import Pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create a soccer pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Define initial positions
initial_red_team = [(10, 40), (20, 20), (20, 60), (40, 50), (50, 40), (40, 30)]
initial_blue_team = [(100, 20), (100, 40), (100, 60), (110, 40), (70, 30), (70, 50)]
initial_ball_position = (60, 40)

# Sidebar controls for interactivity
st.sidebar.title("Interactive Controls")

# Red team positions
st.sidebar.header("Red Team")
red_team = [
    (
        st.sidebar.slider(f"Red {i+1} X", 0, 120, initial_red_team[i][0]),
        st.sidebar.slider(f"Red {i+1} Y", 0, 80, initial_red_team[i][1])
    )
    for i in range(len(initial_red_team))
]

# Blue team positions
st.sidebar.header("Blue Team")
blue_team = [
    (
        st.sidebar.slider(f"Blue {i+1} X", 0, 120, initial_blue_team[i][0]),
        st.sidebar.slider(f"Blue {i+1} Y", 0, 80, initial_blue_team[i][1])
    )
    for i in range(len(initial_blue_team))
]

# Ball position
st.sidebar.header("Ball Position")
ball_position = (
    st.sidebar.slider("Ball X", 0, 120, initial_ball_position[0]),
    st.sidebar.slider("Ball Y", 0, 80, initial_ball_position[1])
)

# Add players to the pitch
for position in red_team:
    ax.add_patch(Circle(position, radius=2, color='red', ec='black', zorder=5))
for position in blue_team:
    ax.add_patch(Circle(position, radius=2, color='blue', ec='black', zorder=5))
ax.add_patch(Circle(ball_position, radius=1, color='white', ec='black', zorder=6))

# Display the interactive pitch
st.pyplot(fig)
