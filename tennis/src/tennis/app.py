"""
tennis scoring app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import tennis_match


class tennis_app(toga.App):
    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label("Your name: ", style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.display_score = toga.TextInput(style=Pack(flex=1), readonly=True)

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button_1 = toga.Button(
            "Team A", on_press=self.score_for_team_a, style=Pack(padding=5)
        )

        button_2 = toga.Button(
            "Team B", on_press=self.score_for_team_b, style=Pack(padding=5)
        )
        button_3 = toga.Button(
            "Create Match", on_press=self.create_match, style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button_1)
        main_box.add(button_2)
        main_box.add(button_3)
        main_box.add(self.display_score)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print("Hello", self.name_input.value)

    def create_match(self, widget):
        self.match = tennis_match.Match("Team A", "Team B")
        print(self.match.get_verbal_score())
        self.name_input.value = self.match.get_verbal_score()

    def score_for_team_a(self, widget):
        self.match.increment_for_team("Team A")
        print(self.match.get_verbal_score())
        self.name_input.value = self.match.get_verbal_score()

    def score_for_team_b(self, widget):
        self.match.increment_for_team("Team B")
        print(self.match.get_verbal_score())
        self.name_input.value = self.match.get_verbal_score()


def main():
    return tennis_app()
