class Match:
    def __init__(self, team_a, team_b, team_a_score, team_b_score, match_date, id = None):
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = team_a_score
        self.team_b_score = team_b_score
        self.match_date = match_date
        self.id = id

    def winner(match):
        if match.team_a_score > match.team_b_score:
            return match.team_a
        elif match.team_a_score == match.team_b_score:
            return "Draw"
        else:
            return match.team_b
