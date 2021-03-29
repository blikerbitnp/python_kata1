# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import namedtuple

import enum

Player = namedtuple("Player", ["name", "score"])


class VerbalScore(enum.Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTEEN = 2
    FOURTY = 3
    DEUCE = "deuce"
    ADV = "advantage"
    WIN = "win"

    def describe(self):
        return self.name.lower()


class Team:
    def __init__(self, players, team_name=None):
        if isinstance(players, str):
            players = [players]
        if team_name is None:
            self.team_name = " & ".join(players)
        else:
            self.team_name = team_name

        self.score = Score()


class Score:
    score_set_a = [0, 1, 2, "win"]
    score_set_b = ["deuce", "advantage", "win"]

    def __init__(self):
        self.points = 0
        self.score_method = Score.score_set_a
        self.score_index = 0

    def get_score(self):
        return self.score_method[self.score_index]

    def verbal_score(self):
        return VerbalScore(self.get_score()).describe()

    def increment(self):
        self.points += 1
        self.score_index += 1

    def deuce(self):
        self.score_method = Score.score_set_b
        self.score_index = 0


class Match:
    def __init__(self, teama="a", teamb="b"):
        self.ta = Team(teama)
        self.tb = Team(teamb)
        self.match_point = 3
        self.deuce_point = 2
        self.team_won = None

    def set_deuce(self):
        self.ta.score.deuce()
        self.tb.score.deuce()

    def increment_for_team(self, team_name):
        if self.team_won:
            return

        if team_name == self.ta.team_name:
            current_team, other_team = self.ta, self.tb
        elif team_name == self.tb.team_name:
            other_team, current_team = self.ta, self.tb
        else:
            return
        current_team.score.increment()

        if (
            current_team.score.get_score()
            == other_team.score.get_score()
            == self.deuce_point
        ):
            self.set_deuce()
            return
        if (
            current_team.score.get_score()
            == other_team.score.get_score()
            == "advantage"
        ):
            self.set_deuce()
            return
        if current_team.score.get_score() == "win":
            self.team_won = current_team

    def get_score(self):
        return {
            self.ta.team_name: self.ta.score.get_score(),
            self.tb.team_name: self.tb.score.get_score(),
        }

    def get_verbal_score(self):
        return {
            self.ta.team_name: self.ta.score.verbal_score(),
            self.tb.team_name: self.tb.score.verbal_score(),
        }


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    a = Match()
    print(a.get_score())
    a.increment_for_team("a")
    print(a.get_score())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
