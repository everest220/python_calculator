liste_tache = []
while True:
    action_tache = input("MENU : afficher (1), ajouter (2), modifier (3) ou supprimer (4) si tu veux sortir tape L : ")
    if action_tache == "1":
        print("Voici la liste de tache :", liste_tache)
    elif action_tache == "2":
        nouvel_article = input("Entre un article à ajouter dans ta liste : ")
        liste_tache.append(nouvel_article)
        print("Voici la liste de tache :", liste_tache)
    elif action_tache == "4":
        print("Voici la liste de tache :", liste_tache)
        number_task_to_delete = input("Entre le numéro de la tache à supprimer (la liste commence par le numéro 0): ")
        number_task_to_delete_int = int(number_task_to_delete)
        del liste_tache[number_task_to_delete_int]
        print("Voici la liste de tache :",liste_tache)
    elif action_tache == "3":
        print("Voici la liste de tache :", liste_tache)
        nombre_tache_a_modifier = input("Entre le numéro de la tache à modifier (la liste commence par le numéro 0): ")
        nombre_tache_a_modifier_int = int(nombre_tache_a_modifier)
        article_a_remplacer = input("Mets le mot que tu mettre dans ta liste et que tu veux supprimer : ")
        liste_tache[nombre_tache_a_modifier_int] = article_a_remplacer
        print("Voici la liste de tache :", liste_tache)
    elif action_tache == "L":
        break
    else:
        print("Seriously you need to not be yourself... Oh Please... Euh you need to not stare...")
        break
