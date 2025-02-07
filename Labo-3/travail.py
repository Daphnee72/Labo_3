#formulaire de mariage
#information
F1_Drivers = bool(input("vous etes un pilote de F1 ou F2 ou F1 academy:"))
buy_me_food = bool(input("payer vous la bouffe en date:"))
nombres_de_point = int(input("entrer vos points en 2024:"))
revenu = float(input("quelle est votre revenu par année:"))
Person = "C"

#reponse
while Person == "C":
    if F1_Drivers and buy_me_food  and nombres_de_point > 200 and  revenu > 22000000: #Les conditions a respecter
        print ("vous pouvez me marier")
        break #si repond deja au condition arreter ici
    else:
        print ("go to the next question")
        
    Person = input("R U: \n A) Kimi A.. B) Ollie B.. C) naur : ") #si non si tes kimi ou Ollie c'est correect
    if Person == "A":
        print("Marry me right now")
    elif Person == "B":
        print("You can")
    elif Person == "C": 
        print("Get out")