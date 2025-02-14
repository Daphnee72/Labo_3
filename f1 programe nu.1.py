# Entrées utilisateur
F1_Drivers = input("Êtes-vous un pilote de F1, F2 ou F1 Academy? (yes/no): ").strip().lower() == "yes"
buy_me_food = input("Payez-vous la bouffe en date? (yes/no): ").strip().lower() == "yes"
nombres_de_point = int(input("Entrez vos points en 2024: "))
revenu = float(input("Quel est votre revenu par année: "))

Person = "C"

# Première boucle while
while Person == "C":
    if F1_Drivers and buy_me_food and nombres_de_point < 200 and revenu < 22000000:
        print("Vous pouvez me marier")
        break  # Sort de la boucle si les conditions sont remplies
    else:
        print("Go to the next question")

    # Entrée utilisateur pour choisir un pilote
    Person = input("R U: \n A) Kimi A.. \n B) Ollie B.. \n C) Naur : ").strip().upper()

    # Deuxième bloc de conditions
    if Person == "A" or Person == "B":
        print("You can")
    elif Person == "C":
        print("What r u doing")

# Deuxième boucle while (autre logique)
counter = 0
while counter < 3:
    response = input("Aimez-vous la F1? (yes/no): ").strip().lower()
    
    if response == "yes":
        print("Cool! La F1 c'est génial.")
    elif response == "no":
        print("Dommage! Peut-être qu'un jour...")
    else:
        print("Je ne comprends pas votre réponse.")
    
    counter += 1

# Première boucle for : Afficher les points obtenus
print("\nDécompte des points que vous avez gagnés :")
for i in range(1, nombres_de_point + 1, 10):  # Incrémente par 10 pour éviter trop d'affichage
    print(f"Vous avez maintenant {i} points.")

# Deuxième boucle for : Afficher les pilotes favoris
favorite_drivers = ["Lando Norris", "Max Verstappen", "Charles Leclerc", "Oscar Piastri"]
print("\nVoici quelques pilotes célèbres :")
for driver in favorite_drivers:
    print(f"- {driver}")

# Troisième bloc de conditions basé sur le revenu
if revenu > 50000000:
    print("Vous devez etre perfoment en F1 !")
elif 20000000 <= revenu <= 50000000:
    print("Vous êtes un pilote bien payé !")
else:
    print("Sois dans une meilleure equipe !")