class team:
    team_name: str
    win_percentage: float
    wins: int
    losses: int
    ties: int
    points: int
    conference: str
    new_wins: int = 0
    new_losses: int = 0
    new_ties: int = 0
    playoff_team: bool = False
    tiebreaker_team: bool = False  # Playoff team only if tiebreaker goes their way

    def __init__(self, team, config_vals):
        self.team_name = team
        self.wins = config_vals[0]
        self.losses = config_vals[1]
        self.ties = config_vals[2]
        self.points = config_vals[3]
        self.conference = config_vals[4]

    def add_win(self):
        self.wins += 1
        self.new_wins += 1
        self.update_win_percentage()

    def add_loss(self):
        self.losses += 1
        self.new_losses += 1
        self.update_win_percentage()

    def add_tie(self):
        self.ties += 1
        self.new_ties += 1
        self.update_win_percentage()

    def update_win_percentage(self):
        self.win_percentage = (self.wins + self.ties * 1 / 2) / (
            self.wins + self.ties + self.losses
        )

    def designate_for_playoffs(self):
        self.playoff_team = True

    def designate_for_tiebreakers(self):
        self.tiebreaker_team = True

    def __lt__(self, other):
        # return (self.wins, self.ties, self.points) < (other.wins, other.ties, other.points)
        return (self.win_percentage, self.points) < (other.win_percentage, other.points)
