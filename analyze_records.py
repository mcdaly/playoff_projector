from loguru import logger
from team import team

def analyze_records(possible_records: list[dict[str, team]]):
    for cur_records in possible_records:
        select_playoff_teams(cur_records)

    # For each team, how many times do they reach the playoffs and how many require a tiebreaker
    team_chances = {}
    for cur_team in possible_records[0]:
        playoff_results = sum([record[cur_team].playoff_team for record in possible_records])
        tiebreaker_results = sum([record[cur_team].tiebreaker_team for record in possible_records])
        team_chances[cur_team] = [playoff_results, tiebreaker_results]
    print(1)


def select_playoff_teams(records: dict[str, team]):
    # # East Winner
    # find_top_in_each_conference(records, "E")
    # # West Winner
    # find_top_in_each_conference(records, "W")

    find_any_tiebreaker_teams(records)


def find_any_tiebreaker_teams(records):
    # Designate the next 4 teams into the playoffs since we have already removed the top 2 teams
    teams_remaining = [team for team in records.values() if not team.playoff_team]
    teams_remaining.sort()
    for ind in range(-1, -8, -1):
        teams_remaining[ind].designate_for_playoffs()
    # Find if any teams have the same win percentage as the 4th place team
    [team.designate_for_tiebreakers() for team in teams_remaining if team.win_percentage == teams_remaining[-6].win_percentage]


def find_top_in_each_conference(records: dict[str, team], conference: str):
    teams = [team for team in records.values() if team.conference is conference]
    teams.sort()
    teams[-1].designate_for_playoffs()
