# IterativeImprovmentSimulation
I was interested in seeing if a clear winner could be produced if two AI had to overcome one another.

---------------------------------------------------------------

**Objective**: Two organizations compete to capture a vital energy source, "The Nexus," which is crucial for their survival. The simulation evaluates their actions and strategies over several rounds, culminating in a final simulation that determines the more successful organization.

**Skills Demonstrated**:
- Python programming
- API integration
- Simulation and game development

**Tools Used**:
- Python
- OpenAI API
- dotenv for environment variable management
- VS Code Insider
- Copilot
- ChatGPT

---------------------------------------------------------------

## Setup Instructions

1. **Clone the Repository**:
   git clone https://github.com/HumanSynthetic/IterativeImprovementSimulation.git
   cd IterativeImprovementSimulation

   OR

   Download/Copy the code and open/paste it in your text editing software.

3. **Create a .env File**:
-In the root directory of the project, create a file named .env and add your OpenAI API key:
  OPENAI_API_KEY='your-api-key'

4. **Install the Required Packages**:
-Ensure you have Python 3+ and pip installed, then run:
  pip install openai python-dotenv

6. Run the Script:
   python IterativeImprovementSimulation.py

   OR

   Click run in your text editing software.

---------------------------------------------------------------

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

---------------------------------------------------------------

Important Notes
API Costs: Using the OpenAI API incurs costs. Ensure you monitor your usage and set appropriate limits.

Contact
For any questions or issues, please contact me at jared.hull.dev@gmail.com or find me on GitHub.
