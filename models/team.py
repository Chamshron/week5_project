class Team:
    def __init__(self, name, country, score = None, id = None):
        self.name = name
        self.country = country
        self.score = score
        self.players = []
        self.id = id

