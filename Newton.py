import pandas as pd

def f(x):
    return #definir a função
 
def fl(x):
    return #definir a derivada de f(x)

def fi(x):
	return x - f(x)/fl(x)

def newton(x, t): #Onde x é o chute inicial e t é a precisão, fi é uma função constante, f é a função e fl é a derivada dela
    aux = x
    x = aux - (f(aux)/fl(aux))

    table = pd.DataFrame({'x':[aux], 'f(x)':[f(aux)], 'fi(x)':[x], 'f(fi(x))':[f(x)], '|x - fi(x)|':[abs(aux-x)]})
    table.index.names = ['it']
    
    while abs(aux-x) > t and abs(f(x)) > t:
        aux = x
        x = fi(aux)
        
        table.loc[len(table)] = [aux, f(aux), x, f(x), abs(aux-x)] # Adicionando mais uma linha no dataframe

    print('Tabela de execuções (Newton)\n')
    print(table, '\n')

    return x
