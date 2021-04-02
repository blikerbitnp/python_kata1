from tennis_match import *


def test_for_deuce():
    a = Match()
    print(a.get_score())
    a.increment_for_team("a")
    a.increment_for_team("b")
    a.increment_for_team("a")
    a.increment_for_team("b")
    a.increment_for_team("a")
    a.increment_for_team("b")
    assert a.get_score() == {"a": "deuce", "b": "deuce"}


def test_for_straight_win():
    a = Match()
    for i in range(3):
        a.increment_for_team("a")
    assert a.team_won.team_name == "a"


def test_for_set_deuce():
    a = Match()
    a.set_deuce()
    assert a.get_score() == {"a": "deuce", "b": "deuce"}


def test_for_advantage():
    a = Match()
    a.set_deuce()
    a.increment_for_team("a")
    a.get_score()


def test_verbal_score():
    a = Match()
    assert {"a": "love", "b": "love"} == a.get_verbal_score()
    a.increment_for_team("a")
    assert a.get_verbal_score() == {"a": "fifteen", "b": "love"}
    a.increment_for_team("a")
    assert a.get_verbal_score() == {"a": "thirteen", "b": "love"}
    a.increment_for_team("a")
    assert a.get_verbal_score() == {"a": "win", "b": "love"}
    a.increment_for_team("a")
    assert a.get_verbal_score() == {"a": "win", "b": "love"}


# other tests..
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
