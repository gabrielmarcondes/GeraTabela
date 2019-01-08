from __future__ import annotations

from collections import Iterable

from fixture_generator.fixtures import Round, Match


class TestGetMatches:
    def test_when_there_are_no_matches_returns_empty_iterable(self):
        r = Round()
        matches = r.get_matches()

        assert list(matches) == []

    def test_returns_an_iterable(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        matches = r.get_matches()

        assert isinstance(matches, Iterable)

    def test_returns_an_iterable_of_matches(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        matches = r.get_matches()

        assert isinstance(list(matches)[0], Match)

    def test_returns_an_iterable_with_match_h_vs_a(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        matches = list(r.get_matches())

        assert matches[0].is_same(Match(home='H', away='A'))


class TestAddMatch:
    def test_adds_match_to_list(self):
        match = Match(home='H', away='A')
        r = Round()
        r.add_match(match)
        matches = list(r.get_matches())

        assert matches[0].is_same(match)


class TestHomeClubs:
    def test_when_there_are_no_matches_returns_empty_iterable(self):
        r = Round()
        clubs = r.home_clubs()

        assert list(clubs) == []

    def test_returns_an_iterable(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.home_clubs()

        assert isinstance(clubs, Iterable)

    def test_returns_an_iterable_of_strings(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.home_clubs()

        assert isinstance(list(clubs)[0], str)

    def test_returns_an_iterable_with_h(self):
        r = Round()
        r.add_match(Match(home='H', away='A'))
        clubs = set(r.home_clubs())

        assert clubs == {'H'}


class TestAwayClubs:
    def test_when_there_are_no_matches_returns_empty_iterable(self):
        r = Round()
        clubs = r.away_clubs()

        assert list(clubs) == []

    def test_returns_an_iterable(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.away_clubs()

        assert isinstance(clubs, Iterable)

    def test_returns_an_iterable_of_strings(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.away_clubs()

        assert isinstance(list(clubs)[0], str)

    def test_returns_an_iterable_with_a(self):
        r = Round()
        r.add_match(Match(home='H', away='A'))
        clubs = set(r.away_clubs())

        assert clubs == {'A'}


class TestAllClubs:
    def test_when_there_are_no_matches_returns_empty_iterable(self):
        r = Round()
        clubs = r.all_clubs()

        assert list(clubs) == []

    def test_returns_an_iterable(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.all_clubs()

        assert isinstance(clubs, Iterable)

    def test_returns_an_iterable_of_strings(self):
        r = Round()
        r.matches = {
            'H': 'A',
        }
        clubs = r.all_clubs()

        assert isinstance(list(clubs)[0], str)

    def test_returns_an_iterable_with_h_and_a(self):
        r = Round()
        r.add_match(Match(home='H', away='A'))
        clubs = set(r.all_clubs())

        assert clubs == {'H', 'A'}
