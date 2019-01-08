import pytest

from fixture_generator import (
    FixturesGenerator,
    InvalidInputException,
    NotValidatedException,
)
from fixture_generator.fixtures import Turn


class TestValidate:
    def test_when_all_names_are_blank_raises_exception(self):
        names = ['\t', ' ', '\n']
        generator = FixturesGenerator(names=names)

        with pytest.raises(InvalidInputException):
            generator.validate()

    def test_when_one_name_is_not_blank_returns_true(self):
        names = ['\t', ' ', '\n', '\tvalid name']
        generator = FixturesGenerator(names=names)

        assert generator.validate()


class TestGenerate:
    eight_names = list('ABCDEFGH')
    nine_names = list('ABCDEFGHI')

    def test_when_not_validated_raises_exception(self):
        generator = FixturesGenerator(self.eight_names)

        with pytest.raises(NotValidatedException):
            generator.generate()

    def test_returns_dict_with_two_round_robins(self):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        assert len(generated.keys()) == 2

    def test_returns_dict_with_two_turns(self):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        assert (
            isinstance(generated['first'], Turn)
            and isinstance(generated['second'], Turn)
        )

    @pytest.mark.parametrize('name', list('ABCDEFGH'))
    def test_team_shows_once_per_round_in_a_robin_with_even_teams(self, name):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        first_robin = generated['first']
        occurrences = [
            name in robin_round.all_clubs()
            for robin_round
            in first_robin.rounds.values()
        ]

        assert all(occurrences)

    @pytest.mark.parametrize('name', list('ABCDEFGHI'))
    def test_team_misses_one_round_in_a_robin_with_odd_teams(self, name):
        generator = FixturesGenerator(self.nine_names)
        generator.validate()
        generated = generator.generate()

        first_robin = generated['first']
        occurrences = [
            name in robin_round.all_clubs()
            for robin_round
            in first_robin.rounds.values()
        ]

        assert sorted(occurrences) == [0, *[True for _ in range(8)]]
