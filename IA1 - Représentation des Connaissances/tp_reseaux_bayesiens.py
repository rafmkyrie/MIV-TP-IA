from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np


# Initialisation du modèle
bayesNet = BayesianModel()

### Ajout des noeuds
bayesNet.add_node("M")
bayesNet.add_node("U")
bayesNet.add_node("R")
bayesNet.add_node("B")
bayesNet.add_node("S")

### Ajout des arcs
bayesNet.add_edge("M", "R")
bayesNet.add_edge("U", "R")
bayesNet.add_edge("B", "R")
bayesNet.add_edge("B", "S")
bayesNet.add_edge("R", "S")

# Ajout des probabilités ##  CPD = Conditional Probablities Distribution 

cpd_A = TabularCPD('M', 2, values=[[.95], [.05]])
cpd_U = TabularCPD('U', 2, values=[[.85], [.15]])
cpd_H = TabularCPD('B', 2, values=[[.90], [.10]])

cpd_S = TabularCPD('S', 2, values=[[0.98, .88, .95, .6], [.02, .12, .05, .40]],
                   evidence=['R', 'B'], evidence_card=[2, 2])

cpd_R = TabularCPD(variable='R', variable_card=2,
                   values=[[0.96, .86, .94, .82, .24, .15, .10, .05], [.04, .14, .06, .18, .76, .85, .90, .95]],
                   evidence=['M', 'B', 'U'], evidence_card=[2, 2, 2])
bayesNet.add_cpds(cpd_A, cpd_U, cpd_H, cpd_S, cpd_R)

# vérifie si le modèle est correctement créé
bayesNet.check_model()


# Création du solveur qui permettra d'inférer notre réseau
solver = VariableElimination(bayesNet)

# Calcul de P(R)
result = solver.query(variables=['R'])
print("\n\n\n\nP(R) = ", result.values[1])
print("\n\n\n")

# Calcul de P(R|M)
result = solver.query(variables=['R'], evidence={'M': 1})
print("\n\n\n\nP(R|M) = ", result.values[1])
print("\n\n\n")

# Calcul de P(S|B^R)
result = solver.query(variables=['S'], evidence={'B': 1, 'R': 1})
print("\n\n\n\nP(S|B^R) = ", result.values[1])
print("\n\n\n")