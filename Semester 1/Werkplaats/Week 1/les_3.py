# Input vragen

# age = input('What is your age? ')
# print(f'Your age is {age}')

# Verbinding

# connection = input('Welke verbinding wilt u gebruiken? [4G, 5G, Wifi open]:')
#
# if connection == '4G' or connection == '4g':
#     print(f'U bent verbonden via 4G!')
# elif connection == '5G' or connection == '5g':
#     print(f'U bent verbonden via 5G!')
# elif connection == 'Wifi open' or connection == 'wifi open':
#     print(f'U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.')
#     answer_str = input('Wilt u nog steeds een verbinding maken? [ja/nee]: ')
#     answer = answer_str.upper()
#     if answer == 'JA':
#         print(f'U bent verbonden via {connection}!')
#     else:
#         print('U bent niet verbonden!')
# else:
#     print('Onbekende invoer, er wordt geen verbinding tot stand gebracht.')

# Vergelijken met een sub-string

# print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
# if "Hello" in "Hello, everyone!":
#     print('Yes, Hello is within the Hello, everyone! string')
#
# print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
# if "hello" in "Hello, everyone!":
#     print('Yes, hello is within the Hello, everyone! string')
# else:
#     print('No, hello with small letters in not within the string')

# Flowchart TB

# print('Patient exposed to TB')
# answer_adult_child = input('Is the patient an adult or a child? [Adult/Child]: ')
# if answer_adult_child == 'Adult' or answer_adult_child == 'adult':
#     print('Adult')
#     answer_tb_adult_symptoms = input('Has common TB symptoms [Yes/No]: ')
#     if answer_tb_adult_symptoms == 'Yes' or answer_tb_adult_symptoms == 'yes':
#         print('Treat as likely TB patient and perform full TB exam.')
#     else:
#         print('Have patient report back if unwell; return in 1 month for checkup.')
#
# elif answer_adult_child == 'Child' or answer_adult_child == 'child':
#     answer_tb_test_child = input('Can TB test be given? [Yes/No]: ')
#     if answer_tb_test_child == 'Yes' or answer_tb_test_child == 'yes':
#         print('Administer TB test.')
#         print("Assess TB test results and child's condition")
#     else:
#         answer_child_well = input('Child well? [Yes/No]: ')
#         if answer_child_well == 'Yes' or answer_child_well == 'yes':
#             print('6 months preventive isoniazid.')
#             print('Have parent bring in if child shows any symptoms')
#         else:
#             print('Take full history. Examine for TB')
#             print('If TB likely diagnosis, treat for TB')
#             print('If other diagnosis more likely, treat as needed and watch for TB symptoms')
# else:
#     print('Abort, unknown input.')

# Flowchart Shopping

# print('Shopping cart')
# answer_payment_method = input('Payment method [Online/Offline]: ')
# if answer_payment_method == 'Online' or answer_payment_method == 'online':
#     print('Online')
#     print('Place purchase order')
#     answer_admin_user = input('Admin user? [Yes/No]: ')
#     if answer_admin_user == 'Yes' or answer_admin_user == 'yes':
#         print('Enter payment details.')
#     elif answer_admin_user == 'No' or answer_admin_user == 'no':
#         answer_approval_rules = input('Approval rules? [Approved/Rejected]: ')
#         if answer_approval_rules == 'Approved' or answer_approval_rules == 'approved':
#             payment_details = input('Enter payment details.')
#             print('Place order.')
#         elif answer_approval_rules == 'Rejected' or answer_approval_rules == 'rejected':
#             print('Purchase order rejected.')
#         else:
#             print('Abort, unknown input.')
#     else:
#         print('Abort, unknown input.')
#
# elif answer_payment_method == 'Offline' or answer_payment_method == 'offline':
#     print('Offline')
#     print('Place purchase order')
#     answer_admin_user = input('Admin user? [Yes/No]: ')
#     if answer_admin_user == 'Yes' or answer_admin_user == 'yes':
#         print('Order created automatically.')
#     elif answer_admin_user == 'No' or answer_admin_user == 'no':
#         answer_approval_rules = input('Approval rules? [Approved/Rejected]: ')
#         if answer_approval_rules == 'Approved' or answer_approval_rules == 'approved':
#             print('Order created automatically.')
#         elif answer_approval_rules == 'Rejected' or answer_approval_rules == 'rejected':
#             print('Purchase order rejected.')
#         else:
#             print('Abort, unknown input.')
#     else:
#         print('Abort, unknown input.')
# else:
#     print('Abort, unknown input.')

# Mc Donald's

print("Mc Donald's")
answer_eating_location = input('Hier opeten of meenemen? [Hier opeten/Meenemen]: ')
if answer_eating_location == 'Hier opeten' or answer_eating_location == 'hier opeten' or answer_eating_location == 'opeten':
    print('Hier opeten')
    answer_burgers_drinks = input('Burgers of drankjes? [Burgers/Drankjes]: ')
    if answer_burgers_drinks == 'Burgers' or answer_burgers_drinks == 'burgers':
        answer_burgers = input('Hamburger, Cheese Burger, Big Mac of Quarter Pounder? [Hamburger/Cheese Burger/Big Mac/Quarter Pounder]: ')
        if answer_burgers == 'Hamburger' or answer_burgers == 'hamburger':
            print('Hamburger.')
        elif answer_burgers == 'Cheese Burger' or answer_burgers == 'cheese burger':
            print('Cheese Burger.')
        elif answer_burgers == 'Big Mac' or answer_burgers == 'big mac':
            print('Big Mac.')
        elif answer_burgers == 'Quarter Pounder' or answer_burgers == 'quarter pounder':
            answer_quarter_pounder_cheese = input('Quarter Pounder met of zonder kaas? [Met/Zonder]: ')
            if answer_quarter_pounder_cheese == 'Met' or answer_burgers == 'met':
                print('Quarter Pounder met kaas.')
            elif answer_quarter_pounder_cheese == 'Zonder' or answer_burgers == 'zonder':
                print('Quarter Pounder zonder kaas.')
            else:
                print('Annuleren, onbekende invoer.')
        else:
            print('Annuleren, onbekende invoer.')
    elif answer_burgers_drinks == 'Drinks' or answer_burgers_drinks == 'drinks':
        answer_drinks = input('Warme of koude dranken? [Warm/Koud]: ')
        if answer_drinks == 'Warm' or answer_drinks == 'warm':
            print('Warme dranken.')
            answer_warm_drinks = input('Koffie, Cappucino, Chocolademelk? [Koffie/Cappucino/Chocolademelk]: ')
            if answer_warm_drinks == 'Koffie' or answer_warm_drinks == 'koffie':
                print('Koffie')
            elif answer_warm_drinks == 'Cappucino' or answer_warm_drinks == 'cappucino':
                print('Cappucino')
            elif answer_warm_drinks == 'Chocolademelk' or answer_warm_drinks == 'chocolademelk':
                print('Chocolademelk')
            else:
                print('Annuleren, onbekende invoer.')
        elif answer_drinks == 'Koud' or answer_drinks == 'koud':
            print('Koude dranken.')
            answer_cold_drinks = input('Coca Cola, Cola Zero, 7-up, Fanta, Fristi? [Coca Cola/Cola Zero/7-up/Fanta/Fristi]: ')
            if answer_cold_drinks == 'Coca Cola' or answer_cold_drinks == 'coca cola':
                print('Coca Cola')
            elif answer_cold_drinks == 'Cola Zero' or answer_cold_drinks == 'cola zero':
                print('Cola Zero')
            elif answer_cold_drinks == '7-up':
                print('7-up')
            elif answer_cold_drinks == 'Fanta' or answer_cold_drinks == 'fanta':
                print('Fanta')
            elif answer_cold_drinks == 'Fristi' or answer_cold_drinks == 'fristi':
                print('Fristi')
            else:
                print('Annuleren, onbekende invoer.')
        else:
            print('Annuleren, onbekende invoer.')
    else:
        print('Annuleren, onbekende invoer.')

elif answer_eating_location == 'Meenemen' or answer_eating_location == 'meenemen':
    print('Meenemen')
    answer_burgers_drinks = input('Burgers of drankjes? [Burgers/Drankjes]: ')
    if answer_burgers_drinks == 'Burgers' or answer_burgers_drinks == 'burgers':
        answer_burgers = input(
            'Hamburger, Cheese Burger, Big Mac of Quarter Pounder? [Hamburger/Cheese Burger/Big Mac/Quarter Pounder]: ')
        if answer_burgers == 'Hamburger' or answer_burgers == 'hamburger':
            print('Hamburger.')
        elif answer_burgers == 'Cheese Burger' or answer_burgers == 'cheese burger':
            print('Cheese Burger.')
        elif answer_burgers == 'Big Mac' or answer_burgers == 'big mac':
            print('Big Mac.')
        elif answer_burgers == 'Quarter Pounder' or answer_burgers == 'quarter pounder':
            answer_quarter_pounder_cheese = input('Quarter Pounder met of zonder kaas? [Met/Zonder]: ')
            if answer_quarter_pounder_cheese == 'Met' or answer_burgers == 'met':
                print('Quarter Pounder met kaas.')
            elif answer_quarter_pounder_cheese == 'Zonder' or answer_burgers == 'zonder':
                print('Quarter Pounder zonder kaas.')
            else:
                print('Annuleren, onbekende invoer.')
        else:
            print('Annuleren, onbekende invoer.')
    elif answer_burgers_drinks == 'Drinks' or answer_burgers_drinks == 'drinks':
        answer_drinks = input('Warme of koude dranken? [Warm/Koud]: ')
        if answer_drinks == 'Warm' or answer_drinks == 'warm':
            print('Warme dranken.')
            answer_warm_drinks = input('Koffie, Cappucino, Chocolademelk? [Koffie/Cappucino/Chocolademelk]: ')
            if answer_warm_drinks == 'Koffie' or answer_warm_drinks == 'koffie':
                print('Koffie')
            elif answer_warm_drinks == 'Cappucino' or answer_warm_drinks == 'cappucino':
                print('Cappucino')
            elif answer_warm_drinks == 'Chocolademelk' or answer_warm_drinks == 'chocolademelk':
                print('Chocolademelk')
            else:
                print('Annuleren, onbekende invoer.')
        elif answer_drinks == 'Koud' or answer_drinks == 'koud':
            print('Koude dranken.')
            answer_cold_drinks = input(
                'Coca Cola, Cola Zero, 7-up, Fanta, Fristi? [Coca Cola/Cola Zero/7-up/Fanta/Fristi]: ')
            if answer_cold_drinks == 'Coca Cola' or answer_cold_drinks == 'coca cola':
                print('Coca Cola')
            elif answer_cold_drinks == 'Cola Zero' or answer_cold_drinks == 'cola zero':
                print('Cola Zero')
            elif answer_cold_drinks == '7-up':
                print('7-up')
            elif answer_cold_drinks == 'Fanta' or answer_cold_drinks == 'fanta':
                print('Fanta')
            elif answer_cold_drinks == 'Fristi' or answer_cold_drinks == 'fristi':
                print('Fristi')
            else:
                print('Annuleren, onbekende invoer.')
        else:
            print('Annuleren, onbekende invoer.')
    else:
        print('Annuleren, onbekende invoer.')
else:
    print('Annuleren, onbekende invoer.')

if answer_eating_location == 'Hier opeten' or answer_eating_location == 'hier opeten' or answer_eating_location == 'opeten':
    print('Bedankt voor uw bestelling en eet smakelijk in ons restaurant.')

if answer_eating_location == 'Meenemen' or answer_eating_location == 'meenemen':
    print('Bedankt voor uw bestelling, goede reis en eet smakelijk.')