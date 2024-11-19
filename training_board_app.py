import streamlit as st
import plotly.graph_objects as go

# Initial positions for players and ball
initial_red_team = [(10, 40), (20, 20), (20, 60), (40, 50), (50, 40), (40, 30)]
initial_blue_team = [(100, 20), (100, 40), (100, 60), (110, 40), (70, 30), (70, 50)]
initial_ball_position = (60, 40)

# Reset functionality
if "red_team" not in st.session_state:
    st.session_state.red_team = initial_red_team
if "blue_team" not in st.session_state:
    st.session_state.blue_team = initial_blue_team
if "ball_position" not in st.session_state:
    st.session_state.ball_position = initial_ball_position

# Create Plotly figure
fig = go.Figure()

# Add red team players
for i, position in enumerate(st.session_state.red_team):
    fig.add_trace(go.Scatter(
        x=[position[0]], y=[position[1]],
        mode='markers+text',
        marker=dict(size=12, color='red'),
        text=f"Red {i + 1}",
        textposition="top center",
        name=f"Red {i + 1}",
        customdata=[i],  # Custom index for callback
        hoverinfo='text'
    ))

# Add blue team players
for i, position in enumerate(st.session_state.blue_team):
    fig.add_trace(go.Scatter(
        x=[position[0]], y=[position[1]],
        mode='markers+text',
        marker=dict(size=12, color='blue'),
        text=f"Blue {i + 1}",
        textposition="top center",
        name=f"Blue {i + 1}",
        customdata=[i],  # Custom index for callback
        hoverinfo='text'
    ))

# Add the ball
fig.add_trace(go.Scatter(
    x=[st.session_state.ball_position[0]], y=[st.session_state.ball_position[1]],
    mode='markers',
    marker=dict(size=10, color='white', line=dict(color='black', width=2)),
    name='Ball',
    customdata=['ball'],  # Special ID for the ball
    hoverinfo='text'
))

# Update layout for the pitch
fig.update_layout(
    title="Interactive Football Training Board",
    xaxis=dict(range=[0, 120], title="Pitch Width", zeroline=False),
    yaxis=dict(range=[0, 80], title="Pitch Height", zeroline=False),
    plot_bgcolor="green",
    dragmode='pan',  # Allows dragging of objects
    showlegend=False
)

# Display the plotly figure
st.plotly_chart(fig, use_container_width=True)

# Placeholder for drag-and-drop future enhancements
st.info("Drag-and-drop functionality requires advanced components.")
