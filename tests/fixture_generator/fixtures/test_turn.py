from fixture_generator.fixtures import Turn, Round


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
