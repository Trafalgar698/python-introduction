from src import calcul_score

# Tests
def test_bowling():
    assert calcul_score(['X','X','X','X','X','X','X','X','X','X','X','X']) == 300
    assert calcul_score(['9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-','9','-']) == 90
    assert calcul_score(['5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5','/','5']) == 150
    print("Tous les tests passent avec succès!")

test_bowling()