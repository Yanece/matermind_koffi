import random


def generer_combinaison(possibilites):
    combinaison = []
    for _ in range(4):
        combinaison.append(random.choice(possibilites))
    return combinaison


possibilites = ["A", "B", "C", "D", "E", "F"]
combinaison_secrete = generer_combinaison(possibilites)

print(combinaison_secrete)
