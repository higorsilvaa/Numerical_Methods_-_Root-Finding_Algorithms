import math
import pandas as pd

def f(x):
    return #definir a função

sinal = lambda x: '+' if x >= 0.0 else '-'

def biss(a, b, t): #Onde a e b delimitam o intervalo([a,b]), t é a precisão e f é a função
    if f(a) * f(b) < 0:
        # temos uma raiz nesse intervalo
        fa, fb = f(a), f(b)

        k = math.ceil(((math.log(b-a)-math.log(t))/math.log(2)))

        print('Quantidade de iterações estimada = %i\n'%k)

        table = pd.DataFrame({'a':a, 'b':b, 'x':[(a+b)/2], 'f(x)':[f((a+b)/2)], 'f(a)':[f(a)], 'f(b)':[f(b)], '|b - a|':[abs(b-a)]})
        table.index.names = ['it']

        while abs(b - a) > t and abs(f((a+b)/2)) > t:
            x, y = (a+b)/2, f((a+b)/2)

            if fa * y > 0:
                a, fa = x, y
            else:
                b, fb = x, y
            
            table.loc[len(table)] = [a, b, (a+b)/2, f((a+b)/2), f(a), f(b), abs(b-a)] # Adicionando mais uma linha no dataframe
        
        table['f(a)'], table['f(b)'] = table['f(a)'].apply(sinal), table['f(b)'].apply(sinal)
		
        print('Tabela de execuções (Bisseção)\n')
        print(table, '\n')
        
        return x

    print('Intervalo ruim...')
