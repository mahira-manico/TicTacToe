#matrice qui permet de numéroter chaque grille
matrice=[
   [0,1,2],
   [3,4,5],
   [6,7,8]
]

#fonction d'affichage de la grille
def affichage_grille():
   print(f" |{matrice[0][0]}|{matrice[0][1]}|{matrice[0][2]}| ")
   print("---------")
   print(f" |{matrice[1][0]}|{matrice[1][1]}|{matrice[1][2]}| ")
   print("---------")
   print(f" |{matrice[2][0]}|{matrice[2][1]}|{matrice[2][2]}| ")
   print("---------")

#fonction qui permet de vérifier une victoire
def verification(choix):
  for a in range(3):
    if matrice[a][0]==choix and matrice[a][1]==choix and matrice[a][2]==choix:
      return True
  for b in range(3):
    if matrice[0][b]==choix and matrice[1][b]==choix and matrice[2][b]==choix:
      return True
    if matrice[0][0]==choix and matrice[1][1]==choix and matrice[2][2]==choix:
      return True
    if matrice[0][2]==choix and matrice[1][1]==choix and matrice[2][0]==choix:
     return True
    
    return False
    
def match_nul():
  plein= True
  for a in range(3):
    for b in range(3):
      if matrice[a][b]!="x" and matrice[a][b]!="o":
        plein=False
  if plein:
    print("match nul!")
    return True
  return False
    
#fonction du jeu 
def jeu_morpion():
   
#le joueur1 choisis son camp
   joueur1=input("choissez votre camp: x ou o:")
   if joueur1=="x":
      joueur2="o"
   elif joueur1=="o":
        joueur2="x"
   if joueur1!="x" and joueur1!="o":
    return print("erreur, choississez x ou o")
 
   print(f"Joueur2, puisque joueur1 à choisi {joueur1} vous êtes {joueur2}!")       

#tour du joueur1
   for tour in range(8):
      choix1=int(input("Joueur1, choisissez un nombre entre 0 et 8:"))
      if choix1>8 or choix1<0:
        print("erreur, choissez un nombre compris entre 0 et 8")
        continue
      for a in range(3):
        for b in range(3):
         if choix1==matrice[a][b]:
          matrice[a][b]=joueur1
          affichage_grille()
      if verification(joueur1):
       print("Joueur1 à gagné!")
       return

#vérification de match nul
      if match_nul():
        return

#tour du joueur2
      choix2=int(input("Joueur2, choisissez un nombre entre 0 et 8:"))
      if choix2>8 or choix2<0:
        print("erreur, choississez un nombre compris entre 0 et 8")
        continue 
      for a in range(3):
            for b in range(3):
              if choix2==matrice[a][b]:
               matrice[a][b]=joueur2
               affichage_grille()
      if verification(joueur2):
       print("Joueur2 à gagné!")
       return
      
jeu_morpion()
 



  




  