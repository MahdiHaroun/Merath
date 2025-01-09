
mother = False
father = False
kids = False
M_kids = False
F_kids = False
G_father = False
G_mother = False
husband_wife = False


money = int(input("amount of money: "))
mother_input = input("Is mother True or False? (Enter True/False): ").strip().lower()
father_input = input("Is father True or False? (Enter True/False): ").strip().lower()
kids_input = input("Are kids True or False? (Enter True/False): ").strip().lower()
if kids_input == "true":
    M_kids = input("Are M_kids True or False? (Enter True/False): ").strip().lower()
    F_kids = input("Are F_kids True or False? (Enter True/False): ").strip().lower()
else:
    kids_input = "false"
husband_wife = input("are husband wife true or false ").strip().lower()



mother = mother_input == "true"
father = father_input == "true"
kids = kids_input == "true"
M_kids = M_kids == "true"
F_kids = F_kids == "true"
husband_wife = husband_wife == "true"



match mother, father, kids, M_kids, F_kids , husband_wife:
    case (False, False , False, False, False , True):
        money =money // 2 
        print("mother will get : ", money)
    case (True, False , False, False, False , False): 
        print("Mother is True, Father is False.")
    case (False, True , False, False, False , False):
        print("Father is True, Mother is False.")
    case (True, True , False, False, False , False):
        print("Mother and Father are True.")