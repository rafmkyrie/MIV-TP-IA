from simpful import *
import matplotlib.pyplot as plt 

fig, ax = plt.subplots() 

FS = FuzzySystem()

###### Technologie de la Cyber-criminalité (TC)

O_AV = TriangleFuzzySet(20, 35, 45, term="avancee")
O_AC = TriangleFuzzySet(35, 45, 60, term="acceptable")
O_IN = TriangleFuzzySet(45, 60, 80, term="insuffisante")

LV_TC = LinguisticVariable([O_AV, O_AC, O_IN], universe_of_discourse=[20,80])
FS.add_linguistic_variable("TC", LV_TC)

'''LV_TC.draw(ax)
ax.set_xlabel("Technologie de la Cyber-criminalité")
ax.set_ylabel("%")
plt.show()'''


###### Normes de la cyber sécurité (NC) 

O_DN = TrapezoidFuzzySet(9, 24, 40, 55, term="dans_les_normes")
O_HN = TrapezoidFuzzySet(40, 55, 60, 70, term="hors_normes")

LV_NC = LinguisticVariable([O_DN, O_HN], universe_of_discourse=[0, 80])

FS.add_linguistic_variable("NC", LV_NC)

'''LV_NC.draw(ax)
ax.set_xlabel("Normes de la cyber sécurité")
ax.set_ylabel("%")
plt.show()'''


###### Portée de l'information (PI) 

O_TG = TrapezoidFuzzySet(5, 10, 15, 20, term="tres_grande")
O_GR = TrapezoidFuzzySet(15, 20, 25, 30, term="grande")
O_MO = TrapezoidFuzzySet(25, 30, 35, 40, term="moyenne")
O_FA = TrapezoidFuzzySet(35, 40, 45, 50, term="faible")

LV_PI = LinguisticVariable([O_TG, O_GR, O_MO, O_FA], universe_of_discourse=[0, 55])

FS.add_linguistic_variable("PI", LV_PI)

'''LV_PI.draw(ax)
ax.set_xlabel("Portée de l'information")
ax.set_ylabel("%")
plt.show()'''


###### Risques de la cybercriminalité (RC)

O_TF = TriangleFuzzySet(-80, -50, -10,   term="tres_fort")
O_FO = TriangleFuzzySet(-50, -10, 10,  term="fort")
O_MOrc = TriangleFuzzySet(-10, 10, 40, term="moyen")
O_FArc = TriangleFuzzySet(10, 40, 70, term="faible")

LV_RC = LinguisticVariable([O_TF, O_FO, O_MOrc, O_FArc], universe_of_discourse=[-90,80])
FS.add_linguistic_variable("RC", LV_RC)

'''LV_RC.draw(ax)
ax.set_xlabel("Risques de la cybercriminalité")
ax.set_ylabel("%")
plt.show()'''


###### Ajout des règles

FS.add_rules([
    "IF (NC IS dans_les_normes) AND (TC IS avancee) AND (PI IS tres_grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS avancee) AND (PI IS grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS avancee) AND (PI IS moyenne) THEN (RC IS moyen)",
    "IF (NC IS dans_les_normes) AND (TC IS avancee) AND (PI IS faible) THEN (RC IS fort)",

    "IF (NC IS dans_les_normes) AND (TC IS acceptable) AND (PI IS tres_grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS acceptable) AND (PI IS grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS acceptable) AND (PI IS moyenne) THEN (RC IS moyen)",
    "IF (NC IS dans_les_normes) AND (TC IS acceptable) AND (PI IS faible) THEN (RC IS fort)",

    "IF (NC IS dans_les_normes) AND (TC IS insuffisante) AND (PI IS tres_grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS insuffisante) AND (PI IS grande) THEN (RC IS faible)",
    "IF (NC IS dans_les_normes) AND (TC IS insuffisante) AND (PI IS moyenne) THEN (RC IS moyen)",
    "IF (NC IS dans_les_normes) AND (TC IS insuffisante) AND (PI IS faible) THEN (RC IS fort)",



    "IF (NC IS hors_normes) AND (TC IS avancee) AND (PI IS tres_grande) THEN (RC IS moyen)",
    "IF (NC IS hors_normes) AND (TC IS avancee) AND (PI IS grande) THEN (RC IS moyen)",
    "IF (NC IS hors_normes) AND (TC IS avancee) AND (PI IS moyenne) THEN (RC IS fort)",
    "IF (NC IS hors_normes) AND (TC IS avancee) AND (PI IS faible) THEN (RC IS tres_fort)",

    "IF (NC IS hors_normes) AND (TC IS acceptable) AND (PI IS tres_grande) THEN (RC IS moyen)",
    "IF (NC IS hors_normes) AND (TC IS acceptable) AND (PI IS grande) THEN (RC IS fort)",
    "IF (NC IS hors_normes) AND (TC IS acceptable) AND (PI IS moyenne) THEN (RC IS fort)",
    "IF (NC IS hors_normes) AND (TC IS acceptable) AND (PI IS faible) THEN (RC IS tres_fort)",

    "IF (NC IS hors_normes) AND (TC IS insuffisante) AND (PI IS tres_grande) THEN (RC IS moyen)",
    "IF (NC IS hors_normes) AND (TC IS insuffisante) AND (PI IS grande) THEN (RC IS fort)",
    "IF (NC IS hors_normes) AND (TC IS insuffisante) AND (PI IS moyenne) THEN (RC IS tres_fort)",
    "IF (NC IS hors_normes) AND (TC IS insuffisante) AND (PI IS faible) THEN (RC IS tres_fort)"
    ])  

FS.set_variable("TC", 52)
FS.set_variable("NC", 42)
FS.set_variable("PI", 17)

rc_inference_value = FS.inference()

print("Pour TC = 52, NC = 42 et PI = 17, RC est égal à " + str(rc_inference_value['RC'])) 
print("\n\n")