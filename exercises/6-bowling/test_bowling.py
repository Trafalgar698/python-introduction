from src import calcul_score

def test_shitty_player():
    assert calcul_score("-- -- -- -- -- -- -- -- -- --") == 0

def test_additional_score():
    assert calcul_score( "81 -- -- -- -- -- -- -- -- --") == 9
    assert calcul_score("9- 8- -- -- -- -- -- -- -- --") == 17
    assert calcul_score("5/ X -- -- -- -- -- -- -- --") == 5
def test_spare():
    assert calcul_score("5/ 8- -- -- -- -- -- -- -- --") == 18
