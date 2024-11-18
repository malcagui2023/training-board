import streamlit as st
from mplsoccer import Pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Initial positions for teams and the ball
initial_red_team = [
    (20, 20), (20, 40), (20, 60),  # Defenders
    (40, 50), (40, 40), (40, 30)   # Midfielders
]
initial_blue_team = [
    (100, 20), (100, 40), (100, 60),  # Defenders
    (110, 40), (70, 30), (70, 50)   # Midfielders
]
initial_ball_position = (60, 30)

# Streamlit Sidebar Controls
st.sidebar.title("Training Board Controls")
reset = st.sidebar.button("Reset")

# Reset positions
if reset:
    current_red_team = initial_red_team.copy()
    current_blue_team = initial_blue_team.copy()
    current_ball_position = initial_ball_position
else:
    current_red_team = initial_red_team
    current_blue_team = initial_blue_team
    current_ball_position = initial_ball_position

# Create the football pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Add players and ball to the pitch
for position in current_red_team:
    circle = Circle(position, radius=2, color='red', ec='black', zorder=5)
    ax.add_patch(circle)

for position in current_blue_team:
    circle = Circle(position, radius=2, color='blue', ec='black', zorder=5)
    ax.add_patch(circle)

ball_circle = Circle(current_ball_position, radius=1, color='white', ec='black', zorder=6)
ax.add_patch(ball_circle)

# Render the pitch in Streamlit
st.pyplot(fig)

st.sidebar.write("Drag players or ball to rearrange them visually.")
st.sidebar.write("Click 'Reset' to reset the positions.")
