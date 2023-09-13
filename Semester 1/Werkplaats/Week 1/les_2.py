# integers
people = 7861304740
print(people)

people = 7_861_304_740
print(people)

people = 7_861_304_740

meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

type(meals_per_year)

# Float

ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

ethernet_speed_mbps = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

speed_of_light = 299_792_458

distance_Rotterdam_NewYork = 5_862.03
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.')

type(time_to_reach_NYC)

# String

ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

zonder_escape = 'This is a "good" plan'
print(zonder_escape)
met_escape = "This is a \"good\" plan"
print(met_escape)

paragraph = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the math "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)

characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"

invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

type(invention)

# Boolean

logged_in = False
print(logged_in)

netwerk_activity = True
print(netwerk_activity)

# Logische operatoren

# user_name = "John Doe"
# entered_name = input("User name, please: ")
# size_user_name = len(user_name)
# size_entered_name = len(entered_name)
# user_name_is_bigger = size_user_name > size_entered_name
# entered_name_is_bigger = size_entered_name > size_user_name
# print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")
# print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")
#
# lights_on = False
# lock_closed = True
# alarm_activated = not lights_on and lock_closed
# print(f"The alarm is activated, is: {alarm_activated}")

# Containers

los_containers = 331
totale_lostijd = 441

gemiddelde_lostijd = totale_lostijd / los_containers
print(f'De gemiddelde lostijd bedraagt {gemiddelde_lostijd} minuten per container')

laad_containers = 287
totale_laadtijd = 295

gemiddelde_laadtijd = totale_laadtijd / laad_containers
print(f'De gemiddelde laadtijd bedraagt {gemiddelde_laadtijd} minuten per container')

# Berekening 1

import math

x = 9.1
math1 = (3 * x) - 1
math2 = 1 + x
math3 = (math2)**2
y = math.sqrt(math1) + math3

print(f'De waarde van y = {y} als x = {x}')

# Berekening 2

a = 0.87
b = 22.7
c = 5.03
math1 = b**2
math2 = 4 * a * c
math3 = math1 - math2

print(f'{math1}, {math2}, {math3}')

math4 = math.sqrt(math3)
math5 = -b + math4
math6 = 2 * a
y = math5 / math6

print(f'De waarde van y = {y} als a = {a}, b = {b} en c = {c}')

# Berekening 3

t = 4
v = 179875474.8
c = 299_792_458

math1 = v**2
math2 = c**2
math3 = math1 / math2
math4 = 1 - math3
math5 = v * math4
math6 = 1 / math5
delta = t * math6

print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0} minuten op de tuinstoel.')
print(f'Vanaf een komeet gezien zit u {delta * 60.0 * 60.0} seconden op de tuinstoel.')