import streamlit as st
from mplsoccer import Pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrow

# Initial positions for teams and the ball
initial_red_team = [
    (10, 40), (20, 40), (20, 60),  # Defenders
    (40, 50), (60, 40), (40, 30)   # Midfielders
]
initial_blue_team = [
    (100, 20), (100, 40), (100, 60),  # Defenders
    (120, 40), (70, 30), (70, 50)   # Midfielders
]
initial_ball_position = (60, 40)

# Sidebar Controls
st.sidebar.title("Training Board Controls")

reset = st.sidebar.button("Reset")
add_arrow = st.sidebar.button("Add Arrow")
clear_arrows = st.sidebar.button("Clear Arrows")

# Arrow data
if "arrows" not in st.session_state:
    st.session_state.arrows = []

# Reset positions and arrows
if reset:
    current_red_team = initial_red_team.copy()
    current_blue_team = initial_blue_team.copy()
    current_ball_position = initial_ball_position
    st.session_state.arrows = []
else:
    current_red_team = initial_red_team
    current_blue_team = initial_blue_team
    current_ball_position = initial_ball_position

# Add a new arrow
if add_arrow:
    st.session_state.arrows.append({"start": (30, 30), "end": (50, 50)})

# Clear all arrows
if clear_arrows:
    st.session_state.arrows = []

# Sliders for the last arrow's start and end positions
if st.session_state.arrows:
    last_arrow = st.session_state.arrows[-1]
    start_x = st.sidebar.slider("Arrow Start X", 0, 120, int(last_arrow["start"][0]))
    start_y = st.sidebar.slider("Arrow Start Y", 0, 80, int(last_arrow["start"][1]))
    end_x = st.sidebar.slider("Arrow End X", 0, 120, int(last_arrow["end"][0]))
    end_y = st.sidebar.slider("Arrow End Y", 0, 80, int(last_arrow["end"][1]))

    # Update the last arrow's position
    st.session_state.arrows[-1] = {"start": (start_x, start_y), "end": (end_x, end_y)}

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

# Draw arrows
for arrow in st.session_state.arrows:
    arrow_patch = FancyArrow(
        arrow["start"][0], arrow["start"][1],
        arrow["end"][0] - arrow["start"][0], arrow["end"][1] - arrow["start"][1],
        color="black", width=0.5, head_width=2, head_length=2, zorder=4
    )
    ax.add_patch(arrow_patch)

# Render the pitch in Streamlit
st.pyplot(fig)

st.sidebar.write("Use sliders to adjust the last arrow's position.")
st.sidebar.write("Click 'Add Arrow' to add a new one or 'Clear Arrows' to remove all.")
st.sidebar.write("Click 'Reset' to reset all players, the ball, and arrows.")
