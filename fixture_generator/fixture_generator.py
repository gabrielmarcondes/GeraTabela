from typing import Iterable


class InvalidInputException(Exception):
    pass


class NotValidatedException(Exception):
    pass


class FixturesGenerator:
    def __init__(self, names: Iterable[str] = None):
        self._names = names
        self._validated_names = None
        self._name_count = 0

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

    def _initialize_flags(self):
        return [[] for _ in range(self._name_count)]

    def _initialize_turns(self, rounds_count):
        return (
            ['' for _ in range(rounds_count)],
            ['' for _ in range(rounds_count)],
        )

    def generate(self, seed=2):
        if self._validated_names is None:
            raise NotValidatedException

        rounds_count = self._get_round_count()
        flags = self._initialize_flags()
        first_turn_rounds, second_turn_rounds = self._initialize_turns(rounds_count)

        home_game = True
        for name_index, name in enumerate(self._validated_names):
            round_index = (seed * name_index) % rounds_count

            for opponent_index, opponent in enumerate(self._validated_names[name_index + 1:]):

                while round_index in flags[name_index]:
                    round_index = (round_index + 1) % rounds_count

                home = "{} vs {}\n".format(name, opponent)
                away = "{} vs {}\n".format(opponent, name)

                first_turn_rounds[round_index] += home if home_game else away
                second_turn_rounds[round_index] += away if home_game else home

                flags[name_index].append(round_index)
                flags[opponent_index + name_index + 1].append(round_index)
                home_game = not home_game

        return {
            'first': first_turn_rounds,
            'second': second_turn_rounds,
        }
