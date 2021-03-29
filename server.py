from tornado.web import RequestHandler, Application
import tornado
import uuid
from tennis_match import *
import json

game_dict = {}



class MatchHandler(RequestHandler):
    def post(self):
        a_team = self.get_argument("teamA", "team_A")
        b_team = self.get_argument("teamB", "team_B")
        match_id = str(uuid.uuid4())
        game_dict[match_id] = Match(a_team, b_team)
        return self.finish(match_id)

    def get(self):
        self.finish(str(list(game_dict.keys())))


class ScoreHandler(RequestHandler):
    def post(self, match_id):
        team = self.get_argument("pointTo")
        game_dict[match_id].increment_for_team(team)
        self.finish(json.dumps(game_dict[match_id].get_score()))

    def get(self, match_id):
        self.finish(json.dumps(game_dict[match_id].get_score()))


def make_app():
    return Application(
        [
            (r"/match", MatchHandler),
            (r"/score/(.*)", ScoreHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
