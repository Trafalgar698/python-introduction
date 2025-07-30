from src import calcul_score

def test_shitty_player():
    assert calcul_score("-- -- -- -- -- -- -- -- -- --") == 0

def test_additional_score():
    assert calcul_score( "81 -- -- -- -- -- -- -- -- --") == 9