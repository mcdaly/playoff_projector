from copy import deepcopy
from team import team
from loguru import logger


def simulate_remaining_weeks(schedule: dict[str, list], teams: dict[str, team], outcomes: list[str]) -> list[dict[str, team]]:
    """
    Run the weeks in the remaining schedule
    :param schedule: Dictionary of weeks and remaining games in each of those weeks
    :param teams: Dictionary of team objects
    :param outcomes: List of possible outcomes for each match
    :return: List of team records for the games simulated this week
    """
    cur_teams = deepcopy(teams)
    final_team_results = []
    for cur_week in schedule:
        final_team_results = simulate_remaining_games(schedule[cur_week], cur_teams, outcomes)
    return final_team_results


def simulate_remaining_games(games_this_week: list, teams: dict[str, team], outcomes: list[str]) -> list[dict[str, team]]:
    """
    Run the games for the current week then remove the game from the
    weekly games and recursively pass the games and teams into itself
    :param games_this_week: List of matchups left to analyze in the current week
    :param teams: Dictionary of team objects
    :param outcomes: List of possible outcomes for each match
    :return: List of team records for the games simulated so far
    """
    final_team_results = []
    cur_game = games_this_week[0]
    # Find the two opponents
    names = cur_game.split()
    team1 = names[0]
    team2 = names[2]
    if not team1 or not team2:
        logger.error(f"Fix the naming of the {cur_game} matchup")

    # Simulate each outcome
    for cur_outcome in outcomes:
        cur_teams = deepcopy(teams)
        if cur_outcome == "Team1 wins":
            cur_teams[team1].add_win()
            cur_teams[team2].add_loss()
        elif cur_outcome == "Team2 wins":
            cur_teams[team2].add_win()
            cur_teams[team1].add_loss()
        elif cur_outcome == "Tie":
            cur_teams[team1].add_tie()
            cur_teams[team2].add_tie()

        remaining_games_this_week = games_this_week[1:]
        if len(remaining_games_this_week) > 0:
            # If we have at least 1 game to analyze, simulate the game
            final_team_results.extend(simulate_remaining_games(remaining_games_this_week, cur_teams, outcomes))
        else:
            # If no more games remain to be simulated, we want to save off the current records
            final_team_results.extend([cur_teams])
    return final_team_results
