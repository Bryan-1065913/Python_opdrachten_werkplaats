# List of Games

games_list = ['Player’s Unknown Battle Ground (PUBG) - 50 Million 2018', 'Fortnite Battle Royale - 39 Million 2017', 'Apex Legends - 50 Million (1 Month) 2019', 'League of Legends (LOL) - 27 Million 2009', 'Counter Strike; Global Offensive - 32 Million 2014', 'Heartstone - 29 Million 20120', 'Minecraft - 91 Million 2011', 'DOTA 2 - 5 million 2015', 'The Division 2 - N/A 2019', 'The Splatoon 2']
print(games_list)

# Opdracht A
games_list[4] = '5] (Counter Strike)'
print(games_list)

# Opdracht B
length_list_item = len(games_list[7])
print(length_list_item)

# Opdracht C
length_games_list = len(games_list)
print(f'Er zitten {length_games_list} games in de lijst.')

# Opdracht D
games_list.insert(1, "Snake")
print(games_list)

# Opdracht E
games_list_last_position = games_list[10]
print(f'Helaas heeft de game {games_list_last_position} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {games_list_last_position}.')

# Opdracht F
games_list[5] = 'Heartstone - 29 Million 2012'
print(games_list)

# Tuple with computer suppliers

computer_suppliers = ('Apple', 'Asus', 'Dell', 'Lenovo', 'Acer', 'Samsung', 'MSI', 'Hewlett-Packard (HP)', 'Toshiba', 'Microsoft', 'Chuwi', 'Sony')
print(computer_suppliers)

# Opdracht A
length_tuple = len(computer_suppliers)
print(f'De tuple bevat {length_tuple} computer leveranciers.')

#Opdracht B
computer_supplier_item = computer_suppliers[7]
length_tuple_item = len(computer_suppliers[7])
print(f'De naam van {computer_supplier_item} bestaat uit {length_tuple_item} karakters.')

#Opdracht C
computer_supplier_10_item = computer_suppliers[9]
print(f'De naam van de 10de leverancier is {computer_supplier_10_item}')

# Dictionaries

film_dictonary = {
    'The Simpsons': '636-555-3226',
    'Vegas Vacation': '555-0100',
    'Ghostbusters': '555-23678',
    'Billy Madison': '555-0840',
    'Swingers': '213-555-4679',
    'Bruce Almighty': '555-0123',
    'Seinfeld': '555-FILK',
    'Arrested Development': '555-0113',
    'Die Hard With a Vengeance': '555-0001',
    'The A-Team': '555-6162'
}
print(film_dictonary)

# Opdracht A

phone_number_bruce = film_dictonary.get('Bruce Almighty')
print(f'Het telefoonnummer van Bruce Almighty is {phone_number_bruce}.')

# Opdracht B

film_dictonary['Harry Potter'] = '605-475-6961'
print(film_dictonary)

# Opdracht C

phone_number_ghostbusters = film_dictonary.get('Ghostbusters')
updated_phone_number = film_dictonary.update({'Ghostbusters': '555-2368'})
updated_phone_number_ghostbusters = film_dictonary.get('Ghostbusters')
print(f'Het telefoonnummer {phone_number_ghostbusters} van de Ghostbusters is gewijzigd naar {updated_phone_number_ghostbusters}]')

# Opdracht D

removed_value = film_dictonary.pop('Seinfeld')
print(film_dictonary)
print(f'Telefoonnummer {removed_value} van Seinfeld is verwijderd.')

# Opdracht E

count_keys_film_dictionary = len(film_dictonary)
print(f'In de dictionary zitten {count_keys_film_dictionary} telefoonnummers.')