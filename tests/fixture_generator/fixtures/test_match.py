from fixture_generator.fixtures import Match


class TestToString:
    def test_returns_a_string(self):
        match = Match(home='Home', away='Away')
        result = match.to_string()

        assert isinstance(result, str)

    def test_returns_home_vs_away(self):
        match = Match(home='Home', away='Away')
        result = match.to_string()
        expected_result = 'Home vs Away'

        assert result == expected_result


class TestMirror:
    def test_returns_another_match(self):
        match = Match(home='Home', away='Away')
        new_match = match.mirror()

        assert isinstance(new_match, Match)

    def test_returns_match_with_away_as_home(self):
        match = Match(home='Home', away='Away')
        new_match = match.mirror()

        assert new_match.home == 'Away'

    def test_returns_match_with_home_as_away(self):
        match = Match(home='Home', away='Away')
        new_match = match.mirror()

        assert new_match.away == 'Home'


class TestIsMirror:
    def test_returns_boolean(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = match_1.mirror()
        result = match_2.is_mirror(match_1)

        assert isinstance(result, bool)

    def test_when_called_on_original_returns_true(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = match_1.mirror()
        result = match_1.is_mirror(match_2)

        assert result

    def test_when_called_on_mirror_returns_true(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = match_1.mirror()
        result = match_2.is_mirror(match_1)

        assert result

    def test_when_matches_not_mirrored_returns_false(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = Match(home='Home', away='Another Away')
        result = match_2.is_mirror(match_1)

        assert not result


class TestIsSame:
    def test_returns_boolean(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = Match(home='Home', away='Away')
        result = match_2.is_same(match_1)

        assert isinstance(result, bool)

    def test_when_called_on_match_1_returns_true(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = Match(home='Home', away='Away')
        result = match_1.is_same(match_2)

        assert result

    def test_when_called_on_match_2_returns_true(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = Match(home='Home', away='Away')
        result = match_2.is_same(match_1)

        assert result

    def test_when_matches_not_equal_returns_false(self):
        match_1 = Match(home='Home', away='Away')
        match_2 = Match(home='Home', away='Another Away')
        result = match_2.is_same(match_1)

        assert not result
