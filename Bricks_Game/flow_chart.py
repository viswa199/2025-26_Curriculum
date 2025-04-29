import graphviz

# Create a new directed graph
g = graphviz.Digraph('G', filename='brick_game_flowchart.gv',
                     node_attr={'shape': 'box', 'style': 'rounded', 'fontname': 'Arial', 'fontsize': '14', 'fontcolor': 'black'},
                     edge_attr={'fontname': 'Arial', 'fontsize': '12', 'fontcolor': 'blue'},
                     graph_attr={'rankdir': 'TB', 'splines': 'ortho', 'dpi': '300', 'fontsize': '20', 'fontname': 'Arial Bold'})

# Create clusters for main components
with g.subgraph(name='cluster_init') as c:
    c.attr(label='Initialization')
    c.node('init_pygame', 'Initialize Pygame')
    c.node('setup_window', 'Create Game Window')
    c.node('define_constants', 'Define Game Constants')
    c.node('setup_paddle', 'Set Up Paddle')
    c.node('setup_ball', 'Set Up Ball')
    c.node('create_bricks', 'Create Bricks')

with g.subgraph(name='cluster_game_loop') as c:
    c.attr(label='Game Loop')
    c.node('process_events', 'Process Events')
    c.node('handle_input', 'Handle Keyboard Input')
    c.node('move_ball', 'Move Ball')
    c.node('check_collisions', 'Check Collisions')
    c.node('render', 'Render Game Objects')
    c.node('update_display', 'Update Display')

with g.subgraph(name='cluster_collisions') as c:
    c.attr(label='Collision Handling')
    c.node('wall_collision', 'Ball-Wall Collision')
    c.node('paddle_collision', 'Ball-Paddle Collision')
    c.node('brick_collision', 'Ball-Brick Collision')

with g.subgraph(name='cluster_game_state') as c:
    c.attr(label='Game State')
    c.node('check_win', 'Check for Win')
    c.node('check_lose', 'Check for Loss')
    c.node('reset_game', 'Reset Game')

# Main flow
g.edge('init_pygame', 'setup_window')
g.edge('setup_window', 'define_constants')
g.edge('define_constants', 'setup_paddle')
g.edge('setup_paddle', 'setup_ball')
g.edge('setup_ball', 'create_bricks')
g.edge('create_bricks', 'process_events')

# Game loop
g.edge('process_events', 'handle_input')
g.edge('handle_input', 'move_ball')
g.edge('move_ball', 'check_collisions')
g.edge('check_collisions', 'wall_collision')
g.edge('wall_collision', 'paddle_collision')
g.edge('paddle_collision', 'brick_collision')
g.edge('brick_collision', 'check_win')
g.edge('check_win', 'check_lose')
g.edge('check_lose', 'render')
g.edge('render', 'update_display')
g.edge('update_display', 'process_events', label='Loop')

# Reset game path
g.edge('check_lose', 'reset_game', label='If ball falls below screen')
g.edge('check_win', 'reset_game', label='If all bricks destroyed')
g.edge('process_events', 'reset_game', label='If R key pressed')
g.edge('reset_game', 'process_events')

# Add detailed descriptions for key components
g.node('description_init', '''Initialize game:
- Set up screen size
- Define colors
- Create fonts
- Set up game clock''', shape='note')

g.node('description_paddle', '''Paddle:
- Width: 100px
- Height: 20px
- Controlled by arrow keys
- Speed: 10px per frame''', shape='note')

g.node('description_ball', '''Ball:
- Size: 20x20 pixels
- Starts at center of screen
- Moves in both X and Y directions
- Bounces off walls, paddle, and bricks''', shape='note')

g.node('description_bricks', '''Bricks:
- 5 rows x 9 columns
- 78px width, 20px height
- 10px padding between bricks
- Disappear when hit by ball''', shape='note')

# Connect descriptions
g.edge('description_init', 'init_pygame', style='dashed', arrowhead='none')
g.edge('description_paddle', 'setup_paddle', style='dashed', arrowhead='none')
g.edge('description_ball', 'setup_ball', style='dashed', arrowhead='none')
g.edge('description_bricks', 'create_bricks', style='dashed', arrowhead='none')

# Render the graph
g.render(format='png')

print("Flowchart created as 'brick_game_flowchart.gv.jpg'")