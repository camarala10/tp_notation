nombre_matieres = int(input("Combien de matières avez-vous ? "))

matieres = []
notes = []
coefficients = []

for i in range(nombre_matieres):
    matiere = input("Nom de la matière : ")
    note = float(input("Moyenne : "))
    coefficient = float(input("Coefficient : "))

    matieres.append(matiere)
    notes.append(note)
    coefficients.append(coefficient)

somme = 0
total_coefficients = 0

for i in range(nombre_matieres):
    somme += notes[i] * coefficients[i]
    total_coefficients += coefficients[i]

moyenne = somme / total_coefficients

print("Votre moyenne générale est :", round(moyenne, 2))