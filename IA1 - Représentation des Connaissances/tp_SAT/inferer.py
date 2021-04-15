def clause_to_list(clause):
    '''
        Fonction qui transforme une clause en liste de littéraux
    '''
    clause_list = clause.replace("0","").split()
    clause_list = [int(i) for i in clause_list]
    return clause_list

def lister_clauses(file):
    '''
        Fonction qui transforme un fichier CNF en une liste de clauses
    '''
    cnf = file.strip().split("\n")
    nb_var = int(cnf[0].split()[-2])
    del cnf[0]
    nb_clauses = len(cnf)
    cnf_clauses = []
    for i in range(nb_clauses):
        cnf_clauses.append(clause_to_list(cnf[i]))
    return cnf_clauses


def solve_cnf(cnf_file):
    '''
        Fonction qui applique le solveur SAT sur le CNF donné en paramètre
    '''
    import os
    f = open('cnf_file_tmp.cnf', 'w')
    f.write(cnf_file)
    f.close()
    os.system('ubcsat -alg saps -i cnf_file_tmp.cnf -solve > tmp')
    output = open('tmp', 'r').read()
    os.remove('tmp')
    os.remove('cnf_file_tmp.cnf')

    if "# Solution found for -target 0" in output:
        return True
    elif "# No Solution found for -target 0" in output:
        return False
    else:
        print(output)
        return None


def count_variables(clauses):
    '''
        Fonction qui compte le nombre de variables présentes dans une liste de clauses
    '''
    variables = []
    for clause in clauses:
        for litteral in clause:
            if abs(litteral) not in variables:
                variables.append(abs(litteral))
    return len(variables)


def make_cnf_file(clauses):
    '''
        Fonction qui crée un fichier CNF à partir de clauses données en paramètres
    '''
    nb_variables = count_variables(clauses)
    nb_clauses = len(clauses)
    file = "p cnf "+str(nb_variables)+" "+str(nb_clauses)+"\n"
    for clause in clauses:
        for litteral in clause:
            file += str(litteral)+ " "
        file += "0\n"
    return file 


def test_inference(bc_cnf_file, litteral):
    '''
        Fonction qui teste l'inférence d'une BC sur un littéral
    '''
    file = open(bc_cnf_file, 'r')
    data = file.read()
    file.close()
    print(data)

    clauses = lister_clauses(data)
    print(clauses)

    clauses.append(clause_to_list(litteral))
    print(clauses)

    file = make_cnf_file(clauses)
    print(file)

    solution = solve_cnf(file)

    #return
    if solution is not None:
        if solution == True:
            print("La BC \""+ bc_cnf_file +"\" n'infère pas le littéral "+litteral)
        else:
            print("La BC \""+ bc_cnf_file +"\" infère le littéral "+litteral)


if __name__ == "__main__":
    test_inference("test1.cnf", "2 0")
    #test_inference("test1.cnf", "3 0")
