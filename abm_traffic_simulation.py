"""Agent-Based Modeling (ABM): Traffic Simulation"""

# pip install mesa
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random

class Vehicle(Agent):
    vehicle_types = ['car', 'bike', 'bus']
    behaviors = ['cautious', 'average', 'aggressive']

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.speed = random.randint(1, 3)
        self.vehicle_type = random.choice(self.vehicle_types)
        self.behavior = random.choice(self.behaviors)
        self.goal = self.random_location()

    def random_location(self):
        return (random.randrange(self.model.grid.width), random.randrange(self.model.grid.height))

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False,
            radius=self.speed
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def step(self):
        self.move()
        if self.pos == self.goal:
            self.goal = self.random_location()  # Pick new goal when reached the old one

class City(Model):
    def __init__(self, width, height, num_agents):
        self.grid = MultiGrid(width, height, torus=False)
        self.schedule = RandomActivation(self)
        self.weather = random.choice(['sunny', 'rainy', 'snowy', 'cloudy'])
        self.road_quality = random.choice(['good', 'average', 'bad'])

        for i in range(num_agents):
            vehicle = Vehicle(i, self)
            self.schedule.add(vehicle)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            while len(self.grid.get_cell_list_contents((x, y))) != 0:  # Ensure the cell is not full
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)
            self.grid.place_agent(vehicle, (x, y))

    def step(self):
        self.schedule.step()

def main():
    # Initialize the city model with a 20x20 grid and 20 cars
    city_model = City(20, 20, 20)

    # Simulate over 100 steps
    for i in range(100):
        print("Step:", i, "Weather:", city_model.weather)
        city_model.step()

if __name__ == "__main__":
    main()
