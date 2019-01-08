from typing import Iterable

from fixture_generator.fixtures import Turn, Match


class InvalidInputException(Exception):
    pass


class NotValidatedException(Exception):
    pass


class FixturesGenerator:
    def __init__(self, names: Iterable[str] = None):
        self._names = names
        self._validated_names = None
        self._name_count = 0
        self.seed = 2

    def validate(self) -> bool:
        self._validated_names = [
            name.strip()
            for name
            in self._names
            if name.strip()
        ]
        self._name_count = len(self._validated_names)
        
        if not self._validated_names:
            raise InvalidInputException

        return True

    def _get_round_count(self):
        rounds_count = self._name_count - 1
        if self._name_count % 2 != 0:
            rounds_count += 1

        return rounds_count

    def _club_has_played_round(self, name, turn, round_index):
        return name in turn.get_round(round_index).all_clubs()

    def generate(self):
        if self._validated_names is None:
            raise NotValidatedException

        rounds_count = self._get_round_count()
        turn1, turn2 = Turn(), Turn()

        home_game = True
        for name_index, name in enumerate(self._validated_names):
            round_index = (self.seed * name_index) % rounds_count

            for opponent in self._validated_names[name_index + 1:]:

                while self._club_has_played_round(name, turn1, round_index):
                    round_index = (round_index + 1) % rounds_count

                match = Match(
                    home=name if home_game else opponent,
                    away=opponent if home_game else name,
                )

                turn1.get_round(round_index).add_match(match)
                turn2.get_round(round_index).add_match(match.mirror())

                home_game = not home_game

        return {
            'first': turn1,
            'second': turn2,
        }
