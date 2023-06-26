# Simulate Public Transit Costs.
import random
import locale

# Set locale for USD currency formatting
locale.setlocale(locale.LC_ALL, 'en_US')

# Define the variables
num_people = 1000000  # number of people in the city
public_transit_cost_per_person = 1000  # cost per year per person for public transit
driving_cost_per_person = 5000  # cost per year per person for driving
public_transit_use_rate = 0.4  # percentage of people who will use public transit

# Define a function to simulate the costs for one year
def simulate_costs():
    total_public_transit_cost = num_people * public_transit_cost_per_person * public_transit_use_rate
    total_driving_cost = num_people * driving_cost_per_person * (1 - public_transit_use_rate)
    return (total_public_transit_cost, total_driving_cost)

# Simulate the costs for 10 years and calculate the average
total_public_transit_cost = 0
total_driving_cost = 0
num_simulations = 100

for i in range(num_simulations):
    public_transit_cost, driving_cost = simulate_costs()
    total_public_transit_cost += public_transit_cost
    total_driving_cost += driving_cost

avg_public_transit_cost = total_public_transit_cost / num_simulations
avg_driving_cost = total_driving_cost / num_simulations

# Format the results as USD with commas and print the results
formatted_public_transit_cost = locale.currency(avg_public_transit_cost, grouping=True)
formatted_driving_cost = locale.currency(avg_driving_cost, grouping=True)

print(f"Avg. Public Transit Cost: {formatted_public_transit_cost}")
print(f"Avg. Driving Cost: {formatted_driving_cost}")

if avg_public_transit_cost < avg_driving_cost:
    print("""Paying for public transit is more cost-effective over 10 years.  
Based on the simulations, the average public transit cost 
is cheaper than the average driving cost.""")
else:
    print("Forcing everyone to drive cars is more cost-effective over 10 years.")
