from __future__ import annotations

from collections import OrderedDict
from typing import Iterable


class Match:
    def __init__(
        self,
        home: str = None,
        away: str = None,
    ):
        self.home = home
        self.away = away

    def to_string(self) -> str:
        return "{0.home} vs {0.away}".format(self)

    def mirror(self) -> Match:
        return Match(home=self.away, away=self.home)

    def is_mirror(self, other_match: Match) -> bool:
        return (
            self.home == other_match.away
            and self.away == other_match.home
        )

    def is_same(self, other_match: Match) -> bool:
        return (
            self.home == other_match.home
            and self.away == other_match.away
        )


class Round:
    def __init__(self):
        self.matches = OrderedDict()

    def add_match(self, match: Match):
        self.matches[match.home] = match.away

    def get_matches(self) -> Iterable[Match]:
        for home, away in self.matches.items():
            yield Match(home=home, away=away)

    def home_clubs(self) -> Iterable[str]:
        return set(self.matches.keys())

    def away_clubs(self) -> Iterable[str]:
        return set(self.matches.values())

    def all_clubs(self) -> Iterable[str]:
        return {*self.home_clubs(), *self.away_clubs()}


class Turn:
    def __init__(self):
        self.rounds = OrderedDict()

    def get_round(self, round_index: int) -> Round:
        if round_index not in self.rounds:
            self.rounds[round_index] = Round()

        return self.rounds[round_index]

    def mirror_turn(self) -> Turn:
        other_turn = Turn()
        for ri, r in self.rounds.items():
            other_round = Round()
            for match in r.get_matches():
                other_round.add_match(match.mirror())
            other_turn.rounds[ri] = other_round
        return other_turn
