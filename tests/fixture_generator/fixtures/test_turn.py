from fixture_generator import FixturesGenerator
from fixture_generator.fixtures import Turn, Round, Match


class TestGetRound:
    def test_when_round_exists_returns_round(self):
        turn = Turn()
        turn.rounds = {0: Round()}
        r = turn.get_round(0)

        assert isinstance(r, Round)

    def test_when_round_does_not_exist_round_is_created_and_returned(self):
        turn = Turn()
        r = turn.get_round(0)

        assert isinstance(r, Round)


class TestMirrorTurn:
    def _turn_is_mirrored(self, turn: Turn, other_turn: Turn):
        assert turn.rounds.keys() == other_turn.rounds.keys()

        for t1_r, t2_r in zip(turn.rounds.values(), other_turn.rounds.values()):
            for t1_match, t2_match in zip(t1_r.get_matches(), t2_r.get_matches()):
                assert t1_match.is_mirror(t2_match)

        return True

    def test_returns_mirrored_turn(self):
        turn = Turn()

        round_1 = Round()
        round_1.add_match(Match(home='h', away='a'))
        round_2 = Round()
        round_2.add_match(Match(home='o', away='y'))

        turn.rounds = {
            0: round_1,
            1: round_2,
        }

        mirrored_turn = turn.mirror_turn()

        assert self._turn_is_mirrored(turn, mirrored_turn)
