def calcul_score(score: str) -> int :
    # "-- -- -- -- -- -- --" ->   ["--", "--", "--"...]
    frames: list[str] = score.split()
    total = 0
    for frame in frames :
        for throw in frame :
            if frame == "-":
                continue

            elif throw.isdigit():
                total += int(throw)
    return total
