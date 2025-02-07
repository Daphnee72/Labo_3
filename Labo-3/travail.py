#formulaire de mariage
#information
F1_Drivers = bool(input("vous etes un pilote de F1 ou F2 ou F1 academy:")) #il faut repondre oui ou non.
buy_me_food = bool(input("payer vous la bouffe en date:")) #il faut repondre oui ou non
nombres_de_point = int(input("entrer vos points en 2024:")) #il faut repondre par un nombre plus haut que 200
revenu = float(input("quelle est votre revenu par année:")) #il faut repondre par un nombre plus haut que 22 millions
Person = "C" #jai ajoter cette condition la pour le choix multiple plus bas

#reponse
while Person == "C": #le while pour qui fasse un loop
    if F1_Drivers and buy_me_food  and nombres_de_point > 200 and  revenu > 22000000: #Les conditions a respecter
        print ("vous pouvez me marier") #ecrire ce qui en parenthese
        break #si repond deja au condition arreter ici
    else: #si ya un non ou un enonce qui corespond pas afficher le print de la linge d'en bas
        print ("go to the next question")
        
    Person = input("R U: \n A) Kimi A.. B) Ollie B.. C) naur : ") #si non si tes kimi ou Ollie c'est correect
    if Person == "A": #si la personne ecrit la lettre A en majuscule
        print("Marry me right now")
    elif Person == "B": #si la personne ecrit la lettre B en majuscule
        print("You can")
    elif Person == "C": #si la personne ecrit la lettre C en majuscule
        print("Get out")