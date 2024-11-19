from mplsoccer import Pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.widgets as widgets

# Create a pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw()

# Initial positions for teams (6 players each) and the ball

initial_red_team = [
    (10, 40), (20, 20), (20, 60),  # Defenders
    (40, 50), (50, 40), (40, 30)   # Midfielders
]
initial_blue_team = [
    (100, 20), (100, 40), (100, 60),  # Defenders
    (110, 40), (70, 30), (70, 50)   # Midfielders
]
initial_ball_position = (60, 40)

# Store current positions (modifiable during the session)
current_red_team = initial_red_team.copy()
current_blue_team = initial_blue_team.copy()
current_ball_position = initial_ball_position

# Store draggable player and ball markers
players = []
ball = None

# Function to make an object draggable
class Draggable:
    def __init__(self, obj):
        self.obj = obj
        self.press = None

    def connect(self):
        self.cidpress = self.obj.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.obj.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.obj.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        if event.inaxes != self.obj.axes: return
        contains, _ = self.obj.contains(event)
        if not contains: return
        self.press = (self.obj.center, event.xdata, event.ydata)

    def on_motion(self, event):
        if self.press is None or event.inaxes != self.obj.axes: return
        center, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.obj.center = (center[0] + dx, center[1] + dy)
        self.obj.figure.canvas.draw()

    def on_release(self, event):
        self.press = None
        self.obj.figure.canvas.draw()

# Function to reset all positions to their initial states
def reset_positions(event):
    global current_red_team, current_blue_team, current_ball_position
    current_red_team = initial_red_team.copy()
    current_blue_team = initial_blue_team.copy()
    current_ball_position = initial_ball_position

    # Reset player positions
    for i, circle in enumerate(players[:6]):  # Red team
        circle.obj.center = current_red_team[i]
    for i, circle in enumerate(players[6:]):  # Blue team
        circle.obj.center = current_blue_team[i]

    # Reset ball position
    ball.obj.center = current_ball_position
    plt.draw()

# Add players to the pitch
for position in current_red_team:
    circle = Circle(position, radius=2, color='red', ec='black', zorder=5)
    ax.add_patch(circle)
    player = Draggable(circle)
    player.connect()
    players.append(player)

for position in current_blue_team:
    circle = Circle(position, radius=2, color='blue', ec='black', zorder=5)
    ax.add_patch(circle)
    player = Draggable(circle)
    player.connect()
    players.append(player)

# Add soccer ball
ball_circle = Circle(current_ball_position, radius=1, color='white', ec='black', zorder=6)
ax.add_patch(ball_circle)
ball = Draggable(ball_circle)
ball.connect()

# Add menu for reset
reset_button_ax = plt.axes([0.4, 0.01, 0.2, 0.05])
reset_button = widgets.Button(reset_button_ax, 'Reset')
reset_button.on_clicked(reset_positions)

plt.title('Training Board')
plt.show()
