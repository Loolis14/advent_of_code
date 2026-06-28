def first_part(file: str) -> int:
    my_score = 0
    scores = {('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,
              ('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'): 6}
    choice_score = {'X': 1, 'Y': 2, 'Z': 3}
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            oppenent_choice = line[0]
            guide_choice = line[-1]
            my_score += choice_score[guide_choice]
            if (oppenent_choice, guide_choice) in scores:
                my_score += scores[(oppenent_choice, guide_choice)]
        return my_score


def second_part(file: str) -> int:
    my_score = 0
    choice_score = {'A': 1, 'B': 2, 'C': 3}
    guide_instruction_score = {'X': 0, 'Y': 3, 'Z': 6}
    relation_win = {'C': 'A', 'A': 'B', 'B': 'C'}
    relation_loose = {'C': 'B', 'A': 'C', 'B': 'A'}
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            oppenent_choice = line[0]
            guide_instruction = line[-1]
            my_score += guide_instruction_score[guide_instruction]
            if guide_instruction == 'X':
                choice = relation_loose[oppenent_choice]
                my_score += choice_score[choice]
            elif guide_instruction == 'Y':
                my_score += choice_score[oppenent_choice]
            elif guide_instruction == 'Z':
                choice = relation_win[oppenent_choice]
                my_score += choice_score[choice]
        return my_score


# print('First part solution:', first_part('test2.txt'))
print('Second part solution:', second_part('test2.txt'))
