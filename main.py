import numpy as np
import yaml
from team import team
from loguru import logger

from simulate_games import simulate_remaining_weeks
from analyze_records import analyze_records

# OUTCOMES = ["Team1 wins", "Team2 wins", "Tie"]
OUTCOMES = ["Team1 wins", "Team2 wins"]

def run_playoff_projections(config_file):
    """
    Go through all remaining games and provide a detailed list of what is needed to make the playoffs

    :param config_file:
    :return:
    """
    with open(config_file, 'r') as file:
        configs = yaml.safe_load(file)
    teams = {}
    for cur_team in configs["teams"]:
        teams[cur_team] = team(team=cur_team, config_vals=configs["teams"][cur_team])
    # Run all possibly remaining games
    record_projections = simulate_remaining_weeks(configs["schedule"], teams, OUTCOMES)

    # Analyze possible records
    analyze_records(record_projections)
    print(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config_file = "/config_yamls/config_file_week14.yaml"
    run_playoff_projections(config_file)
