# simulations
## Agent-Based Modeling (ABM): Traffic Simulation

This Python script implements an agent-based model (ABM) for simulating traffic behavior in a city. The simulation is built using the Mesa library, which provides a framework for creating ABMs.

The script defines two classes: `Vehicle` and `City.` Each `Vehicle` represents a moving agent within the simulation, possessing attributes such as speed, vehicle type (car, bike, or bus), behavior (cautious, average, or aggressive), and a goal destination. The `City` class represents the overall model and manages the grid-based environment where the vehicles move.

The simulation begins by initializing a city model with a specified grid size and vehicle number. Each vehicle is randomly assigned a grid position and placed on the city's update schedule. During each simulation step, vehicles move to neighbor grid cells based on speed, following a random selection from possible steps. A new goal location is randomly assigned when a vehicle reaches its destination.

The simulation also includes stochastic elements, such as random weather conditions and road quality, which can influence vehicle behavior. These elements add variability to the simulation and allow for exploring different scenarios and their impact on traffic patterns.

The script's primary function initializes the city model and simulates the traffic behavior over a specified number of steps (in this case, 100). The output includes the current step number and the weather conditions for each step.

The ABM traffic simulation provided by this script helps study and analyze various traffic scenarios, testing different traffic management strategies, and gaining insights into emergent traffic patterns and behaviors. It can be used for educational purposes, research, and even as a basis for developing and evaluating traffic management algorithms or policies.

Overall, this script serves as a starting point for understanding and experimenting with agent-based simulations of traffic dynamics within a city environment.

## Repo Summary: Simulating Public Transit Costs

This Python script simulates and compares public transit costs versus driving over ten years. The script provides insights into the cost-effectiveness of public transit based on simulated scenarios.

The simulation begins by defining several variables, including the number of people in the city (`num_people`), the cost per year per person for public transit (`public_transit_cost_per_person`), the cost per year per person for driving (`driving_cost_per_person`), and the percentage of people who will use public transit (`public_transit_use_rate`).

The script then defines a function, `simulate_costs(),` which calculates the total public transit and driving costs for one year based on the defined variables. It multiplies the number of people by the corresponding price and usage rates to determine the total costs.

Next, the script simulates for ten years by iterating over a specified number of simulations (`num_simulations`). Each simulation calls the `simulate_costs()` function to calculate the one-year costs and accumulates the total public transit and driving costs.

After completing the simulations, the script calculates the average public transit and driving costs by dividing the accumulated expenses by the number of simulations (`num_simulations`).

The results are then formatted as USD currency with commas using the `locale` module and printed to the console. Additionally, the script compares the average public transit cost with the average driving cost over ten years. If the average public transit cost is lower, it indicates that paying for public transit is more cost-effective based on the simulations.

This script is helpful for understanding and analyzing the financial implications of public transit versus driving over a specified period. It allows for easy experimentation with different cost variables, such as the number of people, cost per person, and usage rates. It provides valuable insights for transportation planning, policy, and budgeting decision-making.
