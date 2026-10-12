# Nombre de matières
nombre_matieres = int(input("Combien de matières avez-vous ? "))

somme_notes = 0
somme_coefficients = 0

# Boucle pour saisir les matières
for i in range(nombre_matieres):

    nom_matiere = input("Nom de la matière : ")
    note = float(input("Moyenne de nom_matiere : ",nom_matiere))
    coefficient = float(input("Coefficient de : ",nom_matiere))

    somme_notes += note * coefficient
    somme_coefficients += coefficient

# Calcul de la moyenne
moyenne = somme_notes / somme_coefficients

print("La moyenne générale est :", round(moyenne, 2))