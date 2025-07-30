def calcul_score(score):
    scoring = 0
    i = 0

    for frame in range(10):
        if frame < 9:
            if score[i] == 'X':
                scoring += 10 + valeur_quilles(score[i + 1]) + valeur_quilles(score[i + 2])
                i += 1
            elif score[i + 1] == '/':
                scoring += 10 + valeur_quilles(score[i + 2])
                i += 2
            else:
                scoring += valeur_quilles(score[i]) + valeur_quilles(score[i + 1])
                i += 2
        else:
            if score[i] == 'X':
                scoring += 10 + valeur_quilles(score[i + 1]) + valeur_quilles(score[i + 2])
            elif score[i + 1] == '/':
                scoring += 10 + valeur_quilles(score[i + 2])
            else:
                scoring += valeur_quilles(score[i]) + valeur_quilles(score[i + 1])

    return scoring


def valeur_quilles(lancer):
    if lancer == 'X':
        return 10
    elif lancer == '/':
        return 10
    elif lancer == '-':
        return 0
    else:
        return int(lancer)