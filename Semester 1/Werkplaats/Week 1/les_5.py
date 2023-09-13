# FizzBuzz

numbers = list(range(1, 31))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    print(number)

# Priemgetallen

numbers = list(range(1, 100))

for number in numbers:
    is_prime = True
    for division in numbers:
        if number > division > 1:
            if number % division == 0:
                is_prime = False
                break
    if is_prime:
        print(number)

# Bingo

import random

bingo_card = []
bingo_card_size = 4
bingo_number_total = bingo_card_size ** 2
bingo_numbers_all = list(range(1, 100))
random.shuffle(bingo_numbers_all)
bingo_numbers = bingo_numbers_all[:bingo_number_total]
for line in range(bingo_card_size):
    bingo_row = []
    for column in range(bingo_card_size):
          bingo_row.append(bingo_numbers.pop())
    bingo_card.append(bingo_row)

draw_number = 50
bingo_balls = list(range(1, 100))
random.shuffle(bingo_balls)
drawn_balls = bingo_balls[:draw_number]
# Streep de getallen weg die je op jouw kaart hebt staan
# Dit is niet de meest efficiënte manier, maar het werkt
for ball in drawn_balls:
    for line in range(bingo_card_size):
        for column in range(bingo_card_size):
            if bingo_card[line][column] == ball:
                bingo_card[line][column] = 0

bingo = False
for index in range(bingo_card_size):
    if sum(bingo_card[index]) == 0:
        bingo = True
        break
    # De kolommen zijn wat lastiger.
    column_total = 0
    for column_index in range(bingo_card_size):
        column_total += bingo_card[column_index][index]
    if column_total == 0:
        bingo = True
        break

for line in bingo_card:
    print(line)
if bingo:
    print("Yes! Bingo!")
else:
    print("Jammer, geen bingo, morgen weer een dag")

# While priemgetal

input_prime_number = ""
while input_prime_number != ".":
    input_prime_number = input('Voer een getal in om te controleren of dit een priemgetal is. Wilt u het programma afsluiten, typ dan een . ')
    if input_prime_number == ".":
        print("Tot ziens!")
    else:
        number_input = int(input_prime_number)
        numbers = list(range(2, number_input - 1))
        is_prime = True
        for devision in numbers:
            if devision < number_input:
                if number_input % devision == 0:
                    is_prime = False
                    break
        if is_prime:
            print("Is priemgetal: " + str(input_prime_number))
        else:
            print("Is geen priemgetal: " + str(input_prime_number))