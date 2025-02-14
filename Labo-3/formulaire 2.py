#formulaire 2.1
# Initialisation des points
score = 0  

# Entrées utilisateur
F1_Drivers = input("Êtes-vous un pilote de F1, F2 ou F1 Academy? (yes/no): ").strip().lower() == "yes"
if F1_Drivers:
    score += 10  # Ajoute des point si tes un pilote

buy_me_food = input("Payez-vous la bouffe en date? (yes/no): ").strip().lower() == "yes"
if buy_me_food:
    score += 5  # Ajoute des points si tu paye la bouffe

nombres_de_point = int(input("Entrez vos points en 2024: "))
score += nombres_de_point  # Ajoute les point si tes eu beaucoyp de points en f1

revenu = float(input("Quel est votre revenu par année: "))
if revenu > 20000000:
    score += 15  # Ajoute des points pour un bon revenu

Person = "C"

# Première boucle while
while Person == "C":
    if F1_Drivers and buy_me_food and nombres_de_point < 200 and revenu < 22000000:
        print("Vous pouvez me marier")
        score += 20  # Bonus pour remplir les condition de mariage
        break  
    else:
        print("Go to the next question")

    # Entrée utilisateur pour choisir un pilote
    Person = input("R U: \n A) Kimi A.. \n B) Ollie B.. \n C) Naur : ").strip().upper()

    if Person == "A" or Person == "B":
        print("You can")
        score += 10  # Ajoute des points si la réponse est A ou B
    elif Person == "C":
        print("What r u doing")
        score -= 5  # Enlève des points si la réponse est C

# Deuxième boucle while : Poser plusieurs questions pour accumuler des points
counter = 0
while counter < 3:
    response = input("Aimez-vous la F1? (yes/no): ").strip().lower()
    
    if response == "yes":
        print("a dimache ig")
        score += 5  # Ajoute des points si tu aime la F1
    elif response == "no":
        print("tu devrais commencer")
        score -= 2  # Enlève des points si tu n'aime pas la F1
    else:
        print("... nothing just an inchident")

    counter += 1

# Première boucle for : Afficher les points obtenus
print("\nDécompte des points que vous avez gagnés :")
for i in range(1, nombres_de_point + 1, 10):  #nombre de points
    print(f"Vous avez maintenant {i} points.")

# Deuxième boucle for : Afficher les pilotes favoris
favorite_drivers = ["Lando Norris", "Max Verstappen", "Charles Leclerc", "Oscar Piastri"]
print("\nVoici quelques pilotes que j'aime :")
for driver in favorite_drivers:
    print(f"- {driver}")

# Troisième bloc de conditions basé sur le revenu
if revenu > 50000000:
    print("like Verstappen ")
    score += 20
elif 20000000 <= revenu <= 50000000:
    print("not bad but not good")
    score += 10
else:
    print("sois dans une meilleur equipe")
    score += 5

# Affichage du score final
print(f"\nVotre score total est de : {score} points ! ")*