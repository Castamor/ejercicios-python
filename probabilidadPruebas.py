

def LimiteInfSup(i, clases, iteracion):
    Li = min(clases[iteracion])
    Ls = max(clases[iteracion]) if (i == len(clases)-1) else max(clases[iteracion])+1
    return (Li, Ls)