# IterativeImprovmentSimulation
I was interested in seeing if a clear winner could be produced if two AI had to overcome one another.

## Project Overview

**Objective**: Two organizations compete to capture a vital energy source, "The Nexus," which is crucial for their survival. The simulation evaluates their actions and strategies over several rounds, culminating in a final simulation that determines the more successful organization.

**Skills Demonstrated**:
- Python programming
- API integration
- Simulation and game development

**Tools Used**:
- Python
- OpenAI API
- dotenv for environment variable management

## Setup Instructions

1. **Clone the Repository**:
   git clone https://github.com/HumanSynthetic/IterativeImprovementSimulation.git
   cd IterativeImprovementSimulation

2. **Create a .env File**:
-In the root directory of the project, create a file named .env and add your OpenAI API key:
  OPENAI_API_KEY='your-api-key'

3. **Install the Required Packages**:
-Ensure you have Python and pip installed, then run:
  pip install openai python-dotenv

4. Run the Script:
   python IterativeImprovementSimulation.py

How It Works
Define Organizations
The script starts by defining two organizations using the define_organization function, which generates their specific units and actions based on the provided prompt.

Simulate Scenarios
In each round, the script simulates the scenario using the simulate_scenario function, which evaluates the actions and strategies of the organizations.

Iterative Improvement
Over ten rounds, each organization iteratively improves its strategy based on the outcome of the previous simulation. The define_organization function is used to generate new plans considering the latest simulation outcome.

Final Simulation
After ten rounds, the final_simulation function determines the final outcome and which organization is more successful.

Save Results
The script saves the entire scenario and the final simulation result to a text document named game_scenario.txt.

Code Overview
Here is a brief overview of the key functions in the script:

define_organization(prompt)
Generates an organization's structure and actions based on a given prompt.

def define_organization(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative strategist..."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

simulate_scenario(scenario)
Simulates the scenario and determines the outcome of the organizations' actions.

def simulate_scenario(scenario):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a simulation engine..."},
            {"role": "user", "content": scenario}
        ]
    )
    return response.choices[0].message['content']

final_simulation(scenario)
Evaluates the final outcome of the scenario and determines the more successful organization.

def final_simulation(scenario):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a simulation conclusion engine..."},
            {"role": "user", "content": scenario}
        ]
    )
    return response.choices[0].message['content']

    Important Notes
API Costs: Using the OpenAI API incurs costs. Ensure you monitor your usage and set appropriate limits.

Environment Variables: Keep your API key secure by using environment variables and never hard-code them in your scripts.

Contact
For any questions or issues, please contact me at jared.hull.dev@gmail.com or find me on GitHub.
