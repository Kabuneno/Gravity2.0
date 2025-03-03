# Gravity Simulation

This repository contains Python code for simulating gravitational interactions between multiple objects in 3D space. The simulation models the motion of celestial bodies under the influence of gravity, accounting for their masses, positions, velocities, and elastic collisions.

## Features

- Simulate gravitational interactions between multiple objects in 3D space
- Visualize object trajectories using Matplotlib
- Support for elastic collisions between objects
- Configurable simulation parameters (time step, duration)
- Optional animation using Manim (currently commented out)
- Solar system simulation with orbital velocity calculation

## Requirements

The code requires the following Python libraries:
- NumPy
- Matplotlib
- tqdm
- Manim (optional, for animations)

Install dependencies with:
```bash
pip install numpy matplotlib tqdm manim
```

## Usage

### Basic Gravity Simulation

The `crush.py` file contains a general gravity simulation that allows objects to collide:

```python
from crush import Object, Space

# Define objects with initial parameters
agents = [
    {'coords': [2, 2, 0],
     'speed': [0, 0, 0],
     'mass': 7 * 10 ** 9,
     'radius': .3,
     'color':'RED'
    },
    {'coords': [7, 2, 0],
     'speed': [0, .3, 0.07],
     'mass': 8 * 10 ** 8,
     'radius': .2,
     'color':'BLUE'
    },
    # Add more objects as needed
]

# Create simulation space
space = Space(agents)

# Run simulation for 100 time units
space.get_trajectory(100)

# Plot the resulting trajectories
space.get_plot()
```

### Solar System Simulation

The `solarsystem.py` file contains a specialized simulation for planetary systems:

```python
from solarsystem import Object, Space

# Define a star and planets
agents = [
    # Star
    {'coords': [0, 0, 0],
     'speed': [0, 0, 0],
     'mass': 1e12,
     'radius': 1,
     'color': 'ORANGE'
    },
    # Planets
    {'coords': [10, 0, 0],
     'speed': [0, 0, 0],
     'mass': 1e8,
     'radius': 0.5,
     'color': 'RED'
    },
    # Add more planets as needed
]

# Create simulation space
space = Space(agents)

# Calculate initial orbital velocities
space.get_agentsnosun()
space.get_speed()

# Run simulation for 100 time units
space.get_trajectory(100)

# Plot the resulting trajectories
space.get_plot()
```

## How It Works

### Object Class

The `Object` class represents a celestial body with the following properties:
- Position coordinates in 3D space
- Velocity vector
- Mass
- Radius
- Color (for visualization)

It also calculates gravitational forces between objects using Newton's law of universal gravitation.

### Space Class

The `Space` class manages the simulation:
- Creates and tracks all objects
- Updates object positions and velocities based on gravitational forces
- Records object trajectories over time
- Handles collision detection and response
- Provides visualization methods

## Visualization

The simulation results are visualized in 3D plots showing the trajectories of all objects. Each object is represented by a different color, making it easy to track their movements.

## Advanced Features

### Collision Detection

The `crush.py` implementation includes elastic collision detection and response between objects when their surfaces come into contact.

### Orbital Velocity Calculation

The `solarsystem.py` implementation can automatically calculate appropriate orbital velocities for planets around a central star using the formula:

```
v_orbital = sqrt(G * M / r)
```

Where:
- G is the gravitational constant
- M is the mass of the central body
- r is the distance from the central body

## Animation (Optional)

The code includes commented sections for creating animations using the Manim library. To enable animations, uncomment the relevant code sections in either file and run with the appropriate Manim commands.

