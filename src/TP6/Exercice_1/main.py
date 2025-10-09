import datetime

from .emploi import Emploi
from .entreprise import Entreprise
from .personne import Personne

personne = Personne("Dupont", "Marie", 23, "Diplôme d'ingénieur de l'ENSAI", "")
entreprise = Entreprise("Entreprise préférée", "Lyon", 23_000_000)
emploi = Emploi(personne, entreprise, "CDI", datetime.date(2022, 9, 1), None)

print(f"Expérience professionnelle :\n{personne.experience_professionnelle}")
print("Est-ce que la personne a déjà démissionné ?", personne.demission)
print("Combien d'employés ont démissionné de l'entreprise ?", entreprise.nombre_demissions)
print()

emploi.rupture_contrat(datetime.date(2023, 8, 31), "démission")

print("Est-ce que la personne a déjà démissionné ?", personne.demission)
print("Combien d'employés ont démissionné de l'entreprise ?", entreprise.nombre_demissions)
print(f"Expérience professionnelle :\n{personne.experience_professionnelle}")
