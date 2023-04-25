import random


def cards():
    """Retorna duas cartas."""
    cards = [random.randint(1, 13), random.randint(1, 13)]
    return cards


def cards_to_letters(list_of_cards):
    """Converte as cartas de valor 1,11,12,13 em A,J,Q,K respectivamente."""
    numbers_to_letters = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }
    for i in range(0, len(list_of_cards)):
        for j in numbers_to_letters:
            if j == list_of_cards[i]:
                list_of_cards[i] = numbers_to_letters[j]
    return list_of_cards


def letters_to_cards(list_of_cards):
    """Converte as cartas de valor A,J,Q,K em 1,10,10,10 respectivamente. (regras do BlackJack)"""
    numbers_to_letters = {
        'A': 1,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    for i in range(0, len(list_of_cards)):
        for j in numbers_to_letters:
            if j == list_of_cards[i]:
                list_of_cards[i] = numbers_to_letters[j]
    return list_of_cards


def add_card(list):
    """Adiciona uma carta a sua mão"""
    list.append(random.randint(1, 13))
    return list


def comparition(cards_player, cards_computer):
    """Compara as duas mãos e escolhe o ganhador"""
    comp = 0
    player = 0
    for i in letters_to_cards(cards_player):
        player += i
        if len(cards_player) == 2 and i == 1:
            player += 10

    for j in letters_to_cards(cards_computer):
        comp += j
        if len(cards_computer) == 2 and j == 1:
            comp += 10
    if player <= 21 and comp <= 21:
        if player > comp:
            print(f"You Win. Your score is {player} and computer's score is {comp}")
        elif player == comp:
            print(f"You Draw. Your score is {player} and computer's score is {comp}")
        else:
            print(f"You Loose. Your score is {player} and computer's score is {comp}")
    elif player > 21:
        print(f'Your hand is more than 21, your score is {player}. You Loose')


player_cards = cards_to_letters(cards())
computer_cards = cards_to_letters(cards())

print('Welcome to the BackJack Game!')
print(f'Your cards: {player_cards}')
print(f"Computer's first card: {computer_cards[0]}")
another_card = 'y'
while another_card == 'y':
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        add_card(player_cards)
    print(f"Your hand is {cards_to_letters(player_cards)}")
print(f"Computer's hand is: {computer_cards}")
comparition(player_cards, computer_cards)
