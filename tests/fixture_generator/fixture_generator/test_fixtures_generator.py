from typing import Iterable

import pytest

from fixture_generator import (
    FixturesGenerator,
    InvalidInputException,
    NotValidatedException,
)


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

    def _mirror_match(self, match: str):
        home, away = match.split(' vs ')
        return '{} vs {}'.format(away, home)

    def _mirror_round(self, r: Iterable[str]):
        return [
            self._mirror_match(m)
            for m in r
        ]

    def test_when_not_validated_raises_exception(self):
        generator = FixturesGenerator(self.eight_names)

        with pytest.raises(NotValidatedException):
            generator.generate()

    def test_returns_dict_with_two_round_robins(self):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        assert len(generated.keys()) == 2

    @pytest.mark.parametrize('name', list('ABCDEFGH'))
    def test_team_shows_once_per_round_in_a_robin_with_even_teams(self, name):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        first_robin = generated['first']
        occurrences = [
            robin_round.count(name)
            for robin_round
            in first_robin
        ]

        assert occurrences == [1 for _ in range(7)]

    @pytest.mark.parametrize('name', list('ABCDEFGHI'))
    def test_team_misses_one_round_in_a_robin_with_odd_teams(self, name):
        generator = FixturesGenerator(self.nine_names)
        generator.validate()
        generated = generator.generate()

        first_robin = generated['first']
        occurrences = [
            robin_round.count(name)
            for robin_round
            in first_robin
        ]

        assert sorted(occurrences) == [0, *[1 for _ in range(8)]]

    def test_second_robin_has_mirrored_matches_of_first_robin(self):
        generator = FixturesGenerator(self.eight_names)
        generator.validate()
        generated = generator.generate()

        first_robin = [
            r.split('\n')[:-1]
            for r
            in generated['first']
        ]

        second_robin = [
            r.split('\n')[:-1]
            for r
            in generated['second']
        ]

        mirrored_second_robin = [
            self._mirror_round(r)
            for r
            in second_robin
        ]

        assert first_robin == mirrored_second_robin
