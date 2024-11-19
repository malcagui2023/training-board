import streamlit as st
import plotly.graph_objects as go

# Define initial positions
initial_red_team = [(10, 40), (20, 40), (20, 60), (40, 50), (60, 40), (40, 30)]
initial_blue_team = [(100, 20), (100, 40), (100, 60), (120, 40), (70, 30), (70, 50)]
initial_ball_position = (60, 50)

# Sidebar controls
reset = st.sidebar.button("Reset")

# Store positions in session state
if "red_team" not in st.session_state or reset:
    st.session_state.red_team = initial_red_team
if "blue_team" not in st.session_state or reset:
    st.session_state.blue_team = initial_blue_team
if "ball_position" not in st.session_state or reset:
    st.session_state.ball_position = initial_ball_position

# Create Plotly figure
fig = go.Figure()

# Add red team players
for idx, position in enumerate(st.session_state.red_team):
    fig.add_trace(go.Scatter(
        x=[position[0]],
        y=[position[1]],
        mode='markers+text',
        marker=dict(size=12, color='red'),
        text=f"Red {idx + 1}",
        textposition="top center",
        name=f"Red {idx + 1}"
    ))

# Add blue team players
for idx, position in enumerate(st.session_state.blue_team):
    fig.add_trace(go.Scatter(
        x=[position[0]],
        y=[position[1]],
        mode='markers+text',
        marker=dict(size=12, color='blue'),
        text=f"Blue {idx + 1}",
        textposition="top center",
        name=f"Blue {idx + 1}"
    ))

# Add ball
fig.add_trace(go.Scatter(
    x=[st.session_state.ball_position[0]],
    y=[st.session_state.ball_position[1]],
    mode='markers',
    marker=dict(size=10, color='white', line=dict(color='black', width=2)),
    name="Ball"
))

# Update layout
fig.update_layout(
    title="Interactive Football Training Board",
    xaxis=dict(range=[0, 120], title="Pitch Width"),
    yaxis=dict(range=[0, 80], title="Pitch Height"),
    plot_bgcolor="green",
    showlegend=False
)

# Display the figure
st.plotly_chart(fig, use_container_width=True)
