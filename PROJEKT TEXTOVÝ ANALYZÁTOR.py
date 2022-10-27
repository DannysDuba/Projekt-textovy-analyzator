import pprint


"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Duba
email: duba.danny@gmail.com
discord: DannysDuba#3102
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# Registrovaní uživatelé

users = {"Bob": "123", "Ann": "pass123", "Mike": "password123", "liz": "pass123"}
separate = "-" * 40

# Vyžádá si od uživatele přihlašovací jméno a heslo

login = input("Please enter your username: ")
password = input("Please enter your password:")

# Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,r

if users.get(login) == password:

# Pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

    print(separate)
    print(f"Welcome {login}, you can analyze texts now.")
#pokud není registrovaný, upozorni jej a ukonči program.**

else:
    print(f" {login} your username/password is wrong! Exiting program. ")
    exit()

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

choose_text = input("Choose your text between 1 - 3: ")
print(separate)

# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
# Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

if choose_text.isnumeric() and int(choose_text) in range(1, 4):
    chosen_text = TEXTS[int(choose_text) - 1]

else:
    print("You entered wrong input, exiting the program.")
    exit()



# Prázdné listy
clean_words = list()
titleword = list()
upperword = list()
lowerword = list()
numbers = list()

# Pro vybraný text spočítá následující statistiky:
# Rozdělit slova a očistit od diakritiky
individual_words = chosen_text.split()

for word in individual_words:
    clean_words.append(word.strip(",-.:;"))

    if word.istitle():
        titleword.append(word)

    elif word.isalpha() and word.isupper():
        upperword.append(word)

    elif word.islower():
        lowerword.append(word)

    elif word.isnumeric():
        numbers.append(int(word))



# Počet slov

count_words = len(individual_words)
print(f"There are {count_words} word in the selected text.")

# Počet slov začínajících velkým písmenem,

count_title = len(titleword)
print(f"There are {count_title} titlecase word.")

# Počet slov psaných velkými písmeny,

count_upper = len(upperword)
print(f"There are {count_upper} uppercase words.")

# Počet slov psaných malými písmeny,

count_lower = len(lowerword)
print(f"There are {count_lower} lowercase words.")

# Počet čísel (ne cifer),

count_numbers = len(numbers)
print(f"There are {count_numbers} numeric strings.")


# Sumu všech čísel (ne cifer) v textu.

count_allnumbers = sum(numbers)
print(f"The sum of all the numbers is: {count_allnumbers}")



# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

print(separate)

print(f" {'LEN':3} | {'OCCURENCES':15} | {'NR':2}.", separate, sep="\n")


# spočítat délku jednotlivých slov

for order, word in enumerate(clean_words, 1):
    print(f" {order:3} | {word:13}   |{len(word):2}")

