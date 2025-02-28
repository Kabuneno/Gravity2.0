import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm, tqdm_notebook
from manim import *


class Object:
  GRAVITATIONAL_CONSTANT = 6.674*10**(-11)
  all_objects = []
  def __init__(self, name:str,
              coords:list,
              speed:list,
              mass:float,
              radius:float,
              color:str):
    self.name = name
    self.coords = np.array(coords)
    self.speed = np.array(speed)
    self.mass = mass
    self.radius = radius
    self.color = color
    self.__class__.all_objects.append(self)

  def add_ather_obj(self):
    self.obj_list = []
    """get info aboat ather objects"""
    for instance in self.__class__.all_objects:
      if instance != self:
        self.obj_list.append(instance)

  @classmethod
  def clear_all_objects(cls):
    cls.all_objects.clear()

  def get_gravity_force(self)->np.ndarray:
    force_list = []
    for neighbour in self.obj_list:
      r = neighbour.coords - self.coords
      r_one = r / np.linalg.norm(r)
      force_list.append(self.GRAVITATIONAL_CONSTANT * self.mass * neighbour.mass / np.linalg.norm(r)**2 * r_one)
    self.gravi_force = np.array(force_list).sum(axis=0)

















class Space:

  def __init__(self, agents:list):
    self.time_frame = .01
    self.agents_info = agents
    self.num_agents = len(self.agents_info)
    self.agent_ex_list = []
    self.obj_list = []
    Object.clear_all_objects()
    for i, obj in enumerate(self.agents_info):
      self.agent_ex_list.append(Object(f'Object_{i+1}', obj['coords'],
             obj['speed'],
             obj['mass'],
             obj['radius'],
             obj['color']))
    for ex in self.agent_ex_list:
      ex.add_ather_obj()



  def get_trajectory(self, time: float) -> np.ndarray:
        history = []
        num_steps = int(time / self.time_frame)


        for agent in self.agent_ex_list:
            agent.get_gravity_force()

        for _ in tqdm(range(num_steps)):
            trajectory_i = []
            for agent in self.agent_ex_list:
                other_objects = [i for i in self.agent_ex_list if i != agent]
                for n in other_objects:
                    radius = np.linalg.norm(n.coords - agent.coords)
                    if radius <= (n.radius + agent.radius):
                        Vector = (agent.coords - n.coords) / radius
                        print(np.dot(agent.speed - n.speed, Vector))
                        agent.speed = agent.speed - 2 * np.dot(agent.speed - n.speed, Vector) * Vector

                new_position = agent.coords + agent.speed * self.time_frame + 0.5 * self.time_frame**2 * agent.gravi_force / agent.mass
                new_speed = agent.speed + agent.gravi_force / agent.mass * self.time_frame

                agent.coords = new_position
                agent.speed = new_speed

                trajectory_i.append(agent.coords)

            history.append(np.array(trajectory_i))

            for agent in self.agent_ex_list:
                agent.get_gravity_force()


        self.history = np.array(history)

  def get_plot(self):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d')

    for ind, agent in enumerate(self.agent_ex_list):
      ax.scatter(self.history[0, ind, 0], self.history[0, ind, 1],
              self.history[0, ind, 2], color=agent.color.lower(), s=50, label=f'Start {agent.name}')

      ax.plot(self.history[:, ind, 0], self.history[:, ind, 1],
              self.history[:, ind, 2], color=agent.color.lower())

    ax.set_xlabel('Ось X')
    ax.set_ylabel('Ось Y')
    ax.set_zlabel('Ось Z')
    ax.legend()
    plt.show()






agents = [{'coords': [2, 2, 0],
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
          {'coords': [5, 5, 5],
         'speed': [-.1, 0, 0.1],
         'mass': 1 * 10 ** 8,
         'radius': .15,
         'color':'YELLOW'
         },
          {'coords': [0, 8, 10],
         'speed': [0, 0, 0],
         'mass': 1 * 10 ** 9,
         'radius': .4,
         'color':'green'
         }]
space = Space(agents)
space.get_trajectory(100)
space.get_plot()














# from manim import *
# class GravitySimulation(ThreeDScene):
#     colors_dict = {
#         "BLACK": BLACK,
#         "BLUE": BLUE,
#         "RED": RED,
#         "GREEN": GREEN,
#         "YELLOW": YELLOW,
#         "PURPLE": PURPLE,
#         "ORANGE": ORANGE,
#         "PINK": PINK
#     }

#     def construct(self):

#         self.set_camera_orientation(
#             phi=75 * DEGREES,
#             theta=30 * DEGREES,
#             zoom=0.4,
#             frame_center=[0, 0, 0]
#         )


#         axes = ThreeDAxes(
#             x_range=[-10, 10, 2],
#             y_range=[-10, 10, 2],
#             z_range=[-10, 10, 2],
#             x_length=20,
#             y_length=20,
#             z_length=20,
#             axis_config={
#                 "stroke_width": 1,
#                 "include_ticks": True,
#                 "include_tip": True,
#                 "line_to_number_buff": 0.7,
#                 "color": WHITE,
#             }
#         )
#         self.add(axes)

#         agents = [
#             Dot3D(
#                 radius=agent.radius,
#                 color=self.colors_dict[agent.color.upper()]
#             ).move_to(space.history[0, j])
#             for j, agent in enumerate(space.agent_ex_list)
#         ]

#         for agent in agents:
#             self.add(agent)


#         trajectory_ = space.history
#         for i in tqdm_notebook(range(0, trajectory_.shape[0], 100)):
#             self.play(
#                 *[agents[j].animate.move_to(trajectory_[i, j]) for j in range(len(agents))],
#                 run_time=0.00001
#             )

#         self.wait(1)

# %manim -pql GravitySimulation













# from manim import *
# class GravitySimulation(ThreeDScene):
#      colors_dict = {
#                        "BLACK": BLACK,
#                        "BLUE": BLUE,
#                        "RED": RED,
#                        "GREEN": GREEN,
#                        "YELLOW": YELLOW,
#                        "PURPLE": PURPLE,
#                        "ORANGE": ORANGE,
#                        "PINK": PINK
#                    }

#      def construct(self):
#          self.set_camera_orientation(zoom=0.4)
#          agents = [Dot3D(radius=agent.radius, color=self.colors_dict[agent.color.upper()]) for agent in space.agent_ex_list]
#          trajectory_ = space.history

#          for i in tqdm_notebook(range(0, trajectory_.shape[0], 100)):
#              self.play(
#                  *[agents[j].animate.move_to(trajectory_[i, j]) for j in range(len(agents))],
#                  run_time=0.00001
#              )
#          self.wait(1)

# %manim -pql GravitySimulation