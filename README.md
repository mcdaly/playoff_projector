# Welcome to the Playoff Projector

This is a simulator to determine what is needed for each team to reach the playoffs from their current record

To run the code, 
1. Install the Python modules from the requirements.txt
2. Create your config_file.yaml (or use one of the default ones in the config_yamls directory)
3. From the terminal, run `python3 main.py`

## Config File Yaml
The format for the config file yaml is as follows:
* teams: (These are all the teams in the league and their current statistics)
  * <Team_Name>: [# of Wins, # of Losses, # of Ties, # of Total Points, Conference Letter]
* schedule: (These are all of the remaining weeks and the matchups in each week. These team names need to match the <Team_Name> in the above `teams` section)
  * week_##:
    * "<Team 1> vs <Team 2>"

````
teams:
  # Team Name followed by Wins, Losses, Ties, Total Points Scored, and "E" or "W" for Conference
  Olbert: [8, 5, 0, 1540, "E"]
  Quinn: [7, 6, 0, 1471, "W"]

schedule:
  # Remaining matchups to review
  week_14:
    - "Olbert vs Quinn"
````
