
import random
print("Ceci est un jeu du pendu qui choisit un mot au hazard dans un fichier texte nommé 'mots_pendu.txt', présent dans le même dossier que le script,\n"
      "et qui donne six chances à l'utilisateur pour deviner le mot. A chaque fois que l'utilisateur perd, un dessin de la progression du pendu apparaît.\n")
#affiche un message qui explique à l'utilisateur comment utiliser le programme

# Fonction pour choisir un mot au hasard
def choisir_mot(mots):
    return random.choice(mots)
    #choisit un mot au hasard dans la liste 'mots'

def mot_word_print(liste):
    mot_sans_espace = "".join([element.strip() for element in liste])
    print(f"Etat actuel du mot devant être deviné : {mot_sans_espace}")
    #affiche un string sans espace + un message à partir d'une liste

def li_word_print(liste):
    mot_sans_espace = "".join([element.strip() for element in liste])
    print(f"Lettres incorrctes déjà devinées : {mot_sans_espace}")
    #affiche un string sans espace + un message à partir d'une liste

def pendu_drawing(chances):
    #créé une liste de dessins de pendus à chaque étape
    pendu = [
        '''
           +---+
               |
               |
               |
               |
         ========''',
        '''
           +---+
           O   |
               |
               |
               |
         ========''',
        '''
           +---+
           O   |
           |   |
               |
               |
         ========''',
        '''
           +---+
           O   |
          /|   |
               |
               |
         ========''',
        '''
           +---+
           O   |
          /|\  |
               |
               |
         ========''',
        '''
           +---+
           O   |
          /|\  |
          /    |
               |
         ========''',
        '''
           +---+
           O   |
          /|\  |
          / \  |
               |
         ========'''
    ]

    print(pendu[6-chances])


fichier = open("mots_pendu.txt", "r")
#ouvre le fichier texte contenant les mots aléatoires
contenu = fichier.read()
#lit le contenu du fichier texte
mots = contenu.split()
#discretise le contenu et crée une liste
fichier.close()
#ferme le fichier

mot_aleatoire = choisir_mot(mots)
#choisit un mot aléatoire dans la liste

chances = 6
#initie le nombre de chances données au joueur

mot=[]
for i in range(len(mot_aleatoire)):
    mot.append('_')
#créé une liste de string avec des tirets du bas pour représenter le mot censuré

lettres_correctes_deja_devinees=[]
#initie la liste des lettres correctes déjà devinées pour le while
lettres_incorrectes_deja_devinees=[]
#initie la liste des lettres incorrectes déjà devinées pour le while

mot_word_print(mot)
#affiche le mot censuré sous forme de string
while chances > 0:
    print(f'Vous avez présentement {chances} chances.')
    #notifie en début de loop l'utilisateur de son nombre de chances
    if lettres_incorrectes_deja_devinees != []:
        li_word_print(lettres_incorrectes_deja_devinees)
        #rappelle l'utilisateur des lettres incorrectes déjà devinées, seulement si la liste n'est pas vide (d'où la condition)
    print("S'il-vous plaît, entrez une lettre que vous pensez être présente dans le mot, en miniscule.")
    guess = str(input())
    #demande à l'utilisateur de rentrer une lettre et stock sa réponse dans la variable 'guess'
    while len(guess) != 1:
        print("Vous ne pouvez essayer qu'une seule lettre à la fois ! S'il vous plaît, réessayez")
        guess = str(input())
        #si la variable est non conforme, on demande à l'utilisateur de rerentrer une variable et on réenregistre la variable
        #un while est utilisé pour répéter l'operations autant de fois que necessaire
    while guess in lettres_incorrectes_deja_devinees:
        print("Lettre incorrecte déjà devinée, s'il-vous plaît entrez une autre lettre.")
        li_word_print(lettres_incorrectes_deja_devinees)
        guess = str(input())
        #une fois qu'on s'est assuré que la variable est conforme, on vérifi si elle a déjà été devinée en se référant à la liste des lettres incorrectes déjà devinées
        #on demande à l'utilisateur de rerentrer une autre variable si c'est le cas pour ne pas réduire son nombre de chances.
        #un while est utilisé pour répéter l'operations autant de fois que necessaire
    while guess in lettres_correctes_deja_devinees:
        print("Lettre correcte déjà devinée, s'il-vous plaît entrez une autre lettre.")
        guess = str(input())
        #on vérifie ensuite que la variable n'a pas déjà été devinée etait est dans le mot
        #si c'est le cas, on demande à l'utilisateur de rerentrer la variable et on la réenregistre
        # un while est utilisé pour répéter l'operations autant de fois que necessaire
    if guess in mot_aleatoire :
        #maintenant qu'on a vérifié que la variable est originale et valide, on vérifie si elle est dans le mot
        print(f"Félicitaions ! La lettre {guess}' est bien présente dans le mot.")
        print("")
        #si oui on notifie l'utilisateur
        lettres_correctes_deja_devinees.append(guess)
        #on ajoute la variable aux lettres déjà devinées présentes dans le mot à deviner
        for i in range(len(mot_aleatoire)):
            if mot_aleatoire[i] == guess:
                mot[i]=guess
        #on remplace le tiret dans le mot à afficher pour le décensurer
        mot_word_print(mot)
        #on affiche le mot partiellement décensuré
    else :
        print('echec')
        #si la lettre suposée n'est pas dans le mot, on affiche un message d'echec
        pendu_drawing(chances)
        #affiche le dessin du pendu correspondant au nombre de chances
        chances = chances-1
        #retire une chance
        mot_word_print(mot)
        #affiche les lettres déjà devinées
        if lettres_incorrectes_deja_devinees != []:
            lettres_incorrectes_deja_devinees.append(', ')
        #n'ajoute la virgule qu'à partir de la seconde lettre
        lettres_incorrectes_deja_devinees.append(guess)
        #on ajoute la variable à la liste des lettres incorrectes déjà devinées


    if '_' not in mot:
    #si toutes les lettres du mot ont été deviées (<pas de lettres cachées)
        print('gagné')
        #on affiche le message de victoire
        break
if chances == 0:
    # si les chances sont égales à zero (en sortie du while) on affiche le message de perte
    print('chances = 0')
    # on notifie l'utilisateur qu'il n'a plus de chances
    print('perdu')
    # on notifie l'utilisateur qu'il a perdu
    pendu_drawing(0)
    #on affiche le dessin final du pendu
    print(f'Le mot à deviner était : {mot_aleatoire}.')
    #on notifie l'utilisateur du mot qu'il devait deviner




