class Match:
    def __init__(self, team_a, team_b, team_a_score, team_b_score, match_date, id = None):
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = team_a_score
        self.team_b_score = team_b_score
        self.match_date = match_date
        self.id = id

    def winner(self):
        if self.team_a_score > self.team_b_score:
            return self.team_a
        elif self.team_a_score == self.team_b_score:
            return "Draw"
        else:
            return self.team_b
