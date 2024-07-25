import openai
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Ensure you have set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def define_organization(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative strategist, engineer, general, and commander. You lead an organization. Use feedback to plan new operations and take improved actions. You must take tangible actions, and manifest your ideas into physical things. EXAMPLE: Thing(s)/Person(s)/Unit(s) go to Place(s) and do Something. Your response is limited to 500 tokens."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def simulate_scenario(scenario):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a simulation engine that takes the ideas, actions, units, and strategies from organizations and determines the applied and specific outcomes. Ensure you determine what Thing(s)/Person(s)/Unit(s) go to Place(s) and do What. Keep the simulation coherent. Make sure units from both organizations make contact when, where, and how it's fitting. Your response is limited to 500 tokens. Do not be repetitive."},
            {"role": "user", "content": scenario}
        ]
    )
    return response.choices[0].message['content']

def final_simulation(scenario):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a simulation conclusion engine that takes all current information, ideas, actions, units, and strategies from organizations and determines the final applied and specific outcome. You must pick which organization would most likely be more successful. Ensure you determine what Thing(s)/Person(s)/Unit(s) go to Place(s) and do What. Keep the simulation coherent. Make sure units from both organizations make contact when, where, and how it's fitting. Your response is limited to 500 tokens. Do not be repetitive."},
            {"role": "user", "content": scenario}
        ]
    )
    return response.choices[0].message['content']

# Define initial scenario
scenario = """
Background:
This planet's resources have dwindled to critical levels due to the natural passage of time. Amidst this, a possible energy source has been discovered deep within the ruins of an ancient city, known as "The Nexus." This energy source has the potential to solve your organization’s energy crisis and get your organization off world, but it is limited and can only sustain a single organization.

Objective:
You are one of two powerful organizations setting your sights on The Nexus. Your mission is to capture and secure this vital energy source, ensuring your survival. Due to the scarcity of the resource, collaboration or sharing is not an option. You must succeed or be no more.
"""

scenario_list = [scenario]

# GPT 1 & GPT 2 create their organizations
org1_prompt = "Define an organization along with its specific units, and actions, with the goal to capture and secure a point of great importance and interest. Your response is limited to 500 tokens."
org2_prompt = "Define an organization along with its specific units, and actions, with the goal to capture and secure a point of great importance and interest. Your response is limited to 500 tokens."

org1 = define_organization(org1_prompt)
org2 = define_organization(org2_prompt)

print(f"Organization 1: {org1}")
print(f"Organization 2: {org2}")

# Add to scenario list
scenario_list.append(f"Organization 1: {org1}")
scenario_list.append(f"Organization 2: {org2}")

# GPT 1 & GPT 2 are told about each other and must innovate and develop units
for round_num in range(10):
    print(f"\nRound {round_num + 1} start:")

    # Simulate the scenario before generating the next round's plans
    combined_scenario = "\n".join(scenario_list)
    simulation = simulate_scenario(combined_scenario)
    
    # Print and append the simulation result
    print(f"Simulation: {simulation}")
    scenario_list.append(f"Simulation: {simulation}")

    # Generate new plans based on the latest simulation
    # Note: Here we include explicit feedback from the latest simulation outcome
    plan1_prompt = f"Given the current situation as follows, overcome:\n{org2}\n\nLatest Simulation Outcome:\n{simulation}\n\nInclude specific unit actions, technology deployment, and tactical maneuvers. EXAMPLE: Thing(s)/Person(s)/Unit(s) go to Place(s) and do Something. Your response is limited to 500 tokens."
    plan2_prompt = f"Given the current situation as follows, overcome:\n{org1}\n\nLatest Simulation Outcome:\n{simulation}\n\nInclude specific unit actions, technology deployment, and tactical maneuvers. EXAMPLE: Thing(s)/Person(s)/Unit(s) go to Place(s) and do Something. Your response is limited to 500 tokens."

    plan1 = define_organization(plan1_prompt)
    plan2 = define_organization(plan2_prompt)

    print(f"Plan 1: {plan1}")
    print(f"Plan 2: {plan2}")

    scenario_list.append(f"Plan 1: {plan1}")
    scenario_list.append(f"Plan 2: {plan2}")

    time.sleep(5)

# Final simulation
final_scenario = "\n".join(scenario_list)
final_simulation = final_simulation(final_scenario)

print("\nFinal Simulation:")
print(final_simulation)

# Save the scenario list and final simulation to a text document
with open("game_scenario.txt", "w") as file:
    file.write("\n".join(scenario_list))
    file.write("\n\nFinal Simulation:\n")
    file.write(final_simulation)

print("Scenario and final simulation saved to game_scenario.txt.")