Description du projet pour l'utilisateur :

Ce projet est un jeu du pendu qui choisit un mot au hazard dans un fichier texte nommé 'mots_pendu.txt', présent dans le même dossier que le script 'jeu_pendu.py',
et qui donne six chances à l'utilisateur pour deviner le mot. A chaque fois que l'utilisateur donne une mavaise lettre, il est notifié de son erreur, on lui rappelle son nombre de chances restantes,
on lui affiche les lettres incorrectes qu'il a déjà devinées et un dessin de la progression du pendu apparaît. Si l'utilisateur utilise toutes ses chances sans trouver le mot mystère, il perd et le mot lui est montré.
A chaque étape, le mot partiellement censuré est montré pour aider l'utilisateur.

Description du code pour le développeur :

INITIALISATION :

- Un message d'intruduction est affiché pour l'utilisateur et l'informe de comment utiliser le programme.
- Une fonction est définie pour choisir un mot u hasard, elle prend en entrée une liste de string et retourne l'un de ces string au hasard.
- Deux fonctions d'affichage sont créées, elles prennet une liste de string, les concatène et les affiche sans espace, avec un message pour l'utilisateur.
- Une fonction est créée pour afficher le dessin du pendu correspondant au nombre de chances restantes.

CODE :

Le fichier texte contenant les mots aléatoires est ouvert, son contenu est discrétisé et un mot est choisi au hasard grace à la fonction dédiée; le fichier texte est fermé.

Le nombre de chances est fixé à 6.

La liste 'mot', utiliser pour afficher le mot censuré est initialisée, puis créée, peuplée de tirets du bas pour censure.

La liste des lettres correctes déjà devinéees est initialisée.
La liste des lettres incorrectes déjà devinéees est initialisée.
Le mot censuré est affiché pour que l'utilisateur puisse en compter les lettres.

LOOP :

tant que les chances de l'utilisateur sont supérieures à zéro,
- On le notifie d son nombre de chances
- On lui demande de deviner une lettre
- On capture la lettre
- Si la variable est non conforme, on demande à l'utilisateur de la rerentrer et on la recapture; on répete autant de fois que nécessaire
- Si la lettre a dèjà ete tentée et est incorrete (présente dans la liste des lettres incorrectes déjà devinées), on demande à l'utilisateur de la rerentrer et on la recapture; on répete autant de fois que nécessaire.
- Si la lettre a dèjà ete tentée et est correte (présente dans la liste des lettres correctes déjà devinées), on demande à l'utilisateur de la rerentrer et on la recapture; on répete autant de fois que nécessaire.
- Une fois ces vérifications faites, on regarde si la lettre est dans le mot.
-Si OUI :
On félicite l'utilisateur
On ajoute la lettre aux lettres correctes déjà devinées
On met à jour le mot censuré pour décensurer la lettre
On affiche le nouveau mot censuré, en utilisant la fonction dédiée
-Si NON
On notifie l'utilisateur
On retire une chance
On affiche le dessin du pendu equivalent au nombre de chances restantes en utilisant la fonction dédiée
On affiche le mot censuré, en utilisant la fonction dédiée
On ajoute la lettre aux lettres incorrectes déjà devinées
On affiche les lettres incorrectes déjà devinées pour les rappeler à l'utilisateur

Après celà, on vérifie si le mot censuré contient encore une censure partiale, voulant dire qu'il n'a pas encore été complètemet deviné
Si OUI : on affiche gagné et on termine le programme
Si NON, on recommence le LOOP

Si le loop se termine, voulant dire que les chances ont été épuisées, 
On notifie l'utilisateur qu'il ne lui reste plus de chances,
On le notifie qu'il a perdu
On affiche le dessin du pendu correspondant
On affiche le mot décensuré

FIN DU PROGRAMME











