from loguru import logger
from team import team


def analyze_records(possible_records: list[dict[str, team]]):
    """
    Analyze the records of each team to determine how they can make the playoffs
    :param possible_records: List of team records for each possible scenario
    """
    for cur_records in possible_records:
        select_playoff_teams(cur_records)

    # For each team, how many times do they reach the playoffs and how many require a tiebreaker
    team_chances = {}
    for cur_team in possible_records[0]:
        playoff_results = sum(
            [record[cur_team].playoff_team for record in possible_records]
        )
        tiebreaker_results = sum(
            [record[cur_team].tiebreaker_team for record in possible_records]
        )
        team_chances[cur_team] = [playoff_results, tiebreaker_results]
        how_can_this_team_make_the_playoffs(cur_team, possible_records)
    logger.info(f"Chances for each team to make the playoffs:\n{team_chances}")


def how_can_this_team_make_the_playoffs(
    cur_team: str, all_records: list[dict[str, team]]
):
    """
    Analyze each team individually and what happens in the times when they make the playoffs

    :return:
    """
    playoff_results = sum([record[cur_team].playoff_team for record in all_records])
    tiebreaker_results = sum(
        [record[cur_team].tiebreaker_team for record in all_records]
    )
    total_scenarios = len(all_records)

    # Do they make the playoffs in all cases? If so, print that and move on
    if playoff_results == total_scenarios and tiebreaker_results == 0:
        logger.info(f"{cur_team} has qualified for the playoffs!")

    # Do they miss the playoffs in all cases?
    if playoff_results == 0 and tiebreaker_results == 0:
        logger.info(f"{cur_team} has qualified for the losers bracket!")

    # Now the finer cases...

    print(1)


def select_playoff_teams(records: dict[str, team]):
    """

    :param records:
    :return:
    """
    # # East Winner
    # find_top_in_each_conference(records, "E")
    # # West Winner
    # find_top_in_each_conference(records, "W")

    playoff_spots_available = 6

    # Designate the next 4 teams into the playoffs since we have already removed the top 2 teams
    teams_remaining = [team for team in records.values() if not team.playoff_team]
    teams_remaining.sort()
    for ind in range(-1, -playoff_spots_available - 2, -1):
        teams_remaining[ind].designate_for_playoffs()

    # Find if any teams have the same win percentage as the 6th place team
    [
        team.designate_for_tiebreakers()
        for team in teams_remaining
        if team.win_percentage
        == teams_remaining[-playoff_spots_available].win_percentage
    ]


def find_top_in_each_conference(records: dict[str, team], conference: str):
    """
    Find the top team in each conference and designate them for the playoffs
    :param records:
    :param conference:
    :return:
    """
    teams = [team for team in records.values() if team.conference is conference]
    teams.sort()
    teams[-1].designate_for_playoffs()
