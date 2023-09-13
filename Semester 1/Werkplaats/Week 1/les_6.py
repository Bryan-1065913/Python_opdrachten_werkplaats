# Rekenmachine

# def add(first_number, second_number):
#     print(first_number + second_number)
#
# def subtract(first_number, second_number):
#     print(first_number - second_number)
#
# def multiply(first_number, second_number):
#     print(first_number * second_number)
#
# def divide(first_number, second_number):
#     print(first_number / second_number)
#
# def calculate(first_number, second_number, operator):
#     if operator == '+':
#         add(first_number, second_number)
#     elif operator == '-':
#         subtract(first_number, second_number)
#     elif operator == '*':
#         multiply(first_number, second_number)
#     elif operator == '/':
#         divide(first_number, second_number)
#     else:
#         print('Abort, unknown input.')
#
# input_one = input('Geef het eerste getal: ')
# input_two = input('Geef het tweede getal: ')
# operator = input('Geef de operator (+, -, * of /): ')
# calculate(int(input_one), int(input_two), operator)
#
# # Debug Rekenmachine
#
# def debug_print(first_number, second_number, operator_type):
#     if first_number == 0:
#         print('Debug: first_number is 0')
#     if second_number == 0:
#         print('Debug: second_number is 0')
#     print(f"Debug: {first_number} {operator_type} {second_number}")
#
# def add(first_number, second_number, debug=False):
#     if debug:
#         debug_print(first_number, second_number, '+')
#     print(first_number + second_number)
#
# def subtract(first_number, second_number, debug=False):
#     if debug:
#         debug_print(first_number, second_number, '-')
#     print(first_number - second_number)
#
# def multiply(first_number, second_number, debug=False):
#     if debug:
#         debug_print(first_number, second_number, '*')
#     print(first_number * second_number)
#
# def divide(first_number, second_number, debug=False):
#     if debug:
#         debug_print(first_number, second_number, '/')
#     print(first_number / second_number)
#
# def calculate(first_number, second_number, operator_type, debuginput):
#     if debuginput == 'Yes':
#         debug = True
#     else:
#         debug = False
#
#     if operator_type == '+':
#         add(first_number, second_number, debug)
#     elif operator_type == '-':
#         subtract(first_number, second_number, debug)
#     elif operator_type == '*':
#         multiply(first_number, second_number, debug)
#     elif operator_type == '/':
#         divide(first_number, second_number, debug)
#     else:
#         print('Abort, unknown input.')
#
# input_one = input('Geef het eerste getal: ')
# input_two = input('Geef het tweede getal: ')
# input_debug = input('Debug? [Yes/No]: ')
# operator = input('Geef de operator (+, -, * of /): ')
# calculate(int(input_one), int(input_two), operator, input_debug)

# Verbeterde McDonald's

# import sys
# aborted = False
#
# def eat_or_takeaway():
#     eat_in = False
#     answer_eating_location = input('Hier opeten of meenemen? [Hier opeten/Meenemen]: ')
#     uppercase_answer_eating_location = answer_eating_location.upper()
#     if uppercase_answer_eating_location == 'HIER OPETEN':
#         print('Hier opeten')
#         eat_in = True
#     elif uppercase_answer_eating_location == 'MEENEMEN':
#         print('Meenemen')
#         eat_in = False
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
#     return eat_in
#
# def burgers_or_drinks():
#     answer_burgers_drinks = input('Burgers of drankjes? [Burgers/Drankjes]: ')
#     uppercase_answer_burgers_drinks = answer_burgers_drinks.upper()
#     if uppercase_answer_burgers_drinks == 'BURGERS':
#         burgers()
#     elif uppercase_answer_burgers_drinks == 'DRANKJES':
#         drinks()
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# def burgers():
#     print('Burgers')
#     answer_burgers = input('Burgers [Hamburger, Cheeseburger, Bic Mac, Quarter Pounder]: ')
#     uppercase_answer_burgers = answer_burgers.upper()
#     if uppercase_answer_burgers == 'HAMBURGER':
#         print('Hamburger')
#     elif uppercase_answer_burgers == 'CHEESEBURGER':
#         print('Cheeseburger')
#     elif uppercase_answer_burgers == 'BIC MAC':
#         print('Big Mac')
#     elif uppercase_answer_burgers == 'QUARTER POUNDER':
#         print('Quarter Pounder')
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# def drinks():
#     answer_cold_warm_drinks = input('Warme of koude dranken? [Warm/Koud]: ')
#     uppercase_answer_cold_warm_drinks = answer_cold_warm_drinks.upper()
#     if uppercase_answer_cold_warm_drinks == 'WARM':
#         hot_drinks()
#     elif uppercase_answer_cold_warm_drinks == 'KOUD':
#         cold_drinks()
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# def hot_drinks():
#     print('Warme drankjes')
#     answer_warm_drinks = input('Koffie, Cappucino, Chocolademelk? [Koffie/Cappucino/Chocolademelk]: ')
#     uppercase_answer_warm_drinks = answer_warm_drinks.upper()
#     if uppercase_answer_warm_drinks == 'KOFFIE':
#         print('Koffie')
#     elif uppercase_answer_warm_drinks == 'CAPPUCINO':
#         print('Cappucino')
#     elif uppercase_answer_warm_drinks == 'CHOCOLADEMELK':
#         print('Chocolademelk')
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# def cold_drinks():
#     print('Koude drankjes')
#     answer_cold_drinks = input('Coca Cola, Cola Zero, 7-up, Fanta, Fristi? [Coca Cola/Cola Zero/7-up/Fanta/Fristi]: ')
#     uppercase_answer_cold_drinks = answer_cold_drinks.upper()
#     if answer_cold_drinks == 'COCA COLA':
#         print('Coca Cola')
#     elif answer_cold_drinks == 'COLA ZERO':
#         print('Cola Zero')
#     elif answer_cold_drinks == '7-UP':
#         print('7-up')
#     elif answer_cold_drinks == 'FANTA':
#         print('Fanta')
#     elif answer_cold_drinks == 'FRISTI':
#         print('Fristi')
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# def order_completed(eat_in):
#     if eat_in == True:
#         print('Bedankt voor uw bestelling en eet smakelijk in ons restaurant.')
#     elif eat_in == False:
#         print('Bedankt voor uw bestelling, goede reis en eet smakelijk.')
#     else:
#         sys.exit('Helaas, dit ging niet helemaal goed. Probeer het opnieuw.')
#
# print("Mc Donald's")
#
# eat_in=eat_or_takeaway()
#
# burgers_or_drinks()
#
# order_completed(eat_in)

# Studenten rapport

students_per_classroom = {
    "SWDVT-2023-1E": [
        {
            "naam": "Bryan de Knikker",
            "resultaten": {
                "WP1": "goed",
                "WP2": "uitstekend",
                "WP3": "uitstekend",
                "WP4": "voldoende",
            },
        },
        {
            "naam": "Wilfred Larson",
            "resultaten": {
                "WP1": "onvoldoende",
                "WP2": "goed",
                "WP3": "uitstekend",
                "WP4": "voldoende",
            },
        },
    ],
    "SWDVT-2023-1B": [
        {
            "naam": "Amaya Kane",
            "resultaten": {
                "WP1": "onvoldoende",
                "WP2": "goed",
                "WP3": "voldoende",
                "WP4": "goed",
            },
        },
        {
            "naam": "Lisa Obrien",
            "resultaten": {
                "WP1": "goed",
                "WP2": "uitstekend",
                "WP3": "goed",
                "WP4": "onvoldoende",
            },
        },
    ],
}


def get_is_student_excellent(student):
    excellent = False
    excellent_count = 0
    no_low_grades = True

    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            excellent_count += 1
        if (
            student["resultaten"][result] == "onvoldoende"
            or student["resultaten"][result] == "voldoende"
        ):
            no_low_grades = False

    if no_low_grades or excellent_count > 1:
        excellent = True

    return excellent


def get_excellent_students(students):
    excellent_students = []
    for student in students:
        if get_is_student_excellent(student):
            excellent_students.append(student)
    return excellent_students


def get_most_excellent_classroom(students_per_classroom):
    best_classroom = None
    best_classroom_count = -1
    for classroom in students_per_classroom:
        excellent_students = get_excellent_students(students_per_classroom[classroom])
        if len(excellent_students) > best_classroom_count:
            best_classroom = classroom
            best_classroom_count = len(excellent_students)
        elif len(excellent_students) == best_classroom_count:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def calculate_score_per_student(student):
    score = 0
    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            score += 3
        if student["resultaten"][result] == "goed":
            score += 2
        if student["resultaten"][result] == "voldoende":
            score += 1
    return score


def get_best_scoring_classroom(students_per_classroom):
    best_classroom = ""
    best_classroom_score = 0
    for classroom in students_per_classroom:
        classroom_score = 0
        for student in students_per_classroom[classroom]:
            classroom_score += calculate_score_per_student(student)
        if classroom_score > best_classroom_score:
            best_classroom = classroom
            best_classroom_score = classroom_score
        elif classroom_score == best_classroom_score:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def get_failed_students(students, min_score=3):
    failed_students = []
    for student in students:
        score = calculate_score_per_student(student)
        if score < min_score:
            student["score"] = score
            failed_students.append(student)
    return failed_students


def full_report(students_per_classroom):
    all_students = []
    for classroom in students_per_classroom:
        for student in students_per_classroom[classroom]:
            all_students.append(student)

    print("----- Report -----")
    print("Excellente studenten:")
    excellent_students = get_excellent_students(all_students)
    for student in excellent_students:
        print(f'\t{student["naam"]}')

    print("Klas met de meeste excellente studenten:")
    best_classroom = get_most_excellent_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Klas met de hoogste scores gemiddeld:")
    best_classroom = get_best_scoring_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Studenten met inhaalopdracht:")
    failed_students = get_failed_students(all_students)
    for student in failed_students:
        print(f'\t{student["naam"]}')
        for subject, result in student["resultaten"].items():
            print(f"\t\t{subject}: {result}")


full_report(students_per_classroom)