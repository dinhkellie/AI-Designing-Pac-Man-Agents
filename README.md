# AI-Designing-Pac-Man_Agents

### Step 7: A Random Agent
1. Describe behavior of RandomAgent

  * tinyMaze: The agent chooses one random action from an array of available actions. The game runs until the agent eats the capsule. The agent moves randomly and quickly and has continuous movements. In the tinyMaze environment, the agent completed the game relatively quickly compared to the mediumMaze due to the less amount of walls. It eventually will always get the food but the time it will take is not predetermined. 

  * mediumMaze: We used the openSearch layout and the agent was also moving randomly and quickly, but does not look for the food. It took a longer time, more steps, and had a lower score. When the agent finds food, it does not continue in that direction and just moves randomly, oftentimes moving in circles in a blank section of the environment without any food. 
  
### Step 8: Exploring Environments
1. Screenshot of ![myLayout.lay](https://github.com/clairew2018/AI-Designing-Pac-Man-Agents/blob/master/Screen%20Shot%202017-09-17%20at%2012.24.03%20PM.png)
2. Describe the agent's behaviour in myLayout and openSearch Environment

  * myLayout: 

  * openSearch:

### Step 9: A Better Random Agent
1. Describe behavior of RandomAgent without stop action

  * openSearch: The agent moves much faster without stop as an available action. It chooses randomly, and often between two opposite directions multiple times. It does not eat the pellets in any order, and once the agent has ate all the pellets in a part of the environment it can stay in that empty part for a long time moving somewhat circularly without eating other pellets. Average score out of 3 games is -142.0 with a 100% win rate because there are no ghosts in this environment.

  * myLayout: The agent moves around the board randomly, often getting in circle within the parts of the maze that have many walls. It has a 100% win rate and an average score of -676.0 out of 5 games. The agent does not have any perception of pellets and does not seek them out. 
### Step 10: Reflex Agents: Adding Percepts
