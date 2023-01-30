from texts import TEXTS

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Duba
email: duba.danny@gmail.com
discord: DannysDuba#3102
"""


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
# pokud není registrovaný, upozorni jej a ukonči program.**

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
lenght_of_all_words = list()
count_words_by_lenght = {}

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
print(f"There are {len(individual_words)} word in the selected text.")

# Počet slov začínajících velkým písmenem
print(f"There are {len(titleword)} titlecase word.")

# Počet slov psaných velkými písmeny
print(f"There are {len(upperword)} uppercase words.")

# Počet slov psaných malými písmeny
print(f"There are {len(lowerword)} lowercase words.")

# Počet čísel (ne cifer)
print(f"There are {len(numbers)} numeric strings.")

# Sumu všech čísel (ne cifer) v textu
print(f"The sum of all the numbers is: {sum(numbers)}")


print(separate)

print(f" {'LEN':3} | {'OCCURENCES':15} | {'NR':2}.", separate, sep="\n")


# Tento kód spočítá četnost různých délek slov a zobrazí sloupcový graf

lenght_words = [(len(word)) for word in clean_words if word in clean_words]
number_lenght = {i: lenght_words.count(i) for i in set(lenght_words)}

for wordlenght, info in number_lenght.items():
    wordscount = info
    graph = wordscount * "*"

    print(f"{wordlenght:<3}|{graph:<18} |{wordscount:>5}")
