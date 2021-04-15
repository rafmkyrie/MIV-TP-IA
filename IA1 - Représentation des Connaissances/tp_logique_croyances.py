from pyds import MassFunction, powerset
import pandas as pd


def calcul_degres_croyances_plausibilite(m):
    ''' Fonction qui calcule les degrés de croyances et de plausibilités '''
    hypotheses = ['V', 'S', 'I', 'VI', 'VS', 'SI', 'SVI', '']
    ms = []
    beliefs = []
    plausibilities = []

    for hypothese in hypotheses:
        ms.append(m[hypothese])
        beliefs.append(m.bel(hypothese))
        plausibilities.append(m.pl(hypothese))

    df = pd.DataFrame(
        {"m" : ms,
        "Bel" : beliefs,
        "Pl" : plausibilities},
        index=hypotheses
        )

    return df   



########### EXERCICE 1

''' OMEGA = {Setosa (S), Versicolor (V), Virginica (I) } '''

# 1/ Modélisation des connaissances
m1 = MassFunction({'V':0.6, 'SVI':0.4})
m2 = MassFunction({'S':0.1, 'SI':0.5, 'SVI':0.4})
m3 = MassFunction({'SVI':1})

print("1/ Modélisation des connaissances :\n")
print('M1 : ' + str(m1))
print('M2 : ' + str(m2))
print('M3 : ' + str(m3)+"\n\n\n")

# 2/ Calcul des degrés de croyance et des degrés de plausibilité du premier expert
df_m1 = calcul_degres_croyances_plausibilite(m1)

print("2/ Calcul des degrés de croyance et des degrés de plausibilité du premier expert\n")
print(df_m1.to_markdown())
print("\n\n\n")


# 4/ Combinaison de m1 avec m2 et m3
print("4/ Combinaison de m1 avec m2 et m3 : \n")
m123 = m1 & m2 & m3
print("M123 : " + str(m123) +"\n")

df_m123 = calcul_degres_croyances_plausibilite(m123)
print(df_m123.to_markdown())
print("\n\n")