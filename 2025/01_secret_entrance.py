"""
Dans cet exercice, l'input donnait une série de nombres
qui indiquait la direction (droite (+) ou gauche (-)) ainsi que le nombre
à manipuler.
ex d'input:
"""


def second_part(lines: list[str]) -> int:
    """
    Dans cette seconde partie, il fallait compter le nombre de fois où
    le nombre passait par 0.
    Exemple: 12 + 100 = 12 -> il passe une fois par 0.

    Args: lines, une liste des lines parsait dans la premiere partie.
    """
    start: int = 50
    count_0: int = 0
    for content in lines:
        number: int = int(content[1:])
        # On divise par 100 pour voir le nombre de fois où l'on a de 100 dans
        # le nombre
        count_0 += number // 100

        # On recupère ensuite le reste pour avoir la nouvelle valeur et
        # faire la meme methode que pour la premiere partie
        number = number % 100
        if content[0] == 'L':
            temp: int = (start - number) % 100
            if start != 0 and temp != 0 and temp >= start:
                count_0 += 1
        elif content[0] == 'R':
            temp: int = (start + number) % 100
            if start != 0 and temp != 0 and temp <= start:
                count_0 += 1
        if temp == 0:
            count_0 += 1
        start = temp
    return count_0


def first_part() -> int:
    """
    La première partie consistait a compter le nombre de fois où le code
    tombait sur 0 exactement.
    """

    # Initialisation des variables
    start: int = 50
    count_0: int = 0

    # Parsing de l'input
    with open('test1.txt') as f:
        lines: list[str] = f.read().splitlines()

    print('Second part result: ', second_part(lines))

    for content in lines:
        number: int = int(content[1:])
        if content[0] == 'L':
            temp: int = (start - number) % 100  # modulo pour cycler
        elif content[0] == 'R':                 # sur le maximum
            temp: int = (start + number) % 100

        # Vérification de la condition de l'énoncé
        if temp == 0:
            count_0 += 1
        start = temp

    return count_0


print('First part result: ', first_part())
