import math
import pandas as pd

def f(x):
    return #definir a função

sinal = lambda x: '+' if x >= 0.0 else '-'

def false_position(a, b, t, lim): #Onde a e b delimitam o intervalo([a,b]), t é a precisão, lim é o limite de iterações permitida para evitar loop e f é a função
    x = (a*f(b) - b*f(a))/(f(b) - f(a))
    
    table = pd.DataFrame({'a':[a], 'b':[b], 'x':[x], 'f(x)':[f(x)], 'f(a)':[f(a)], 'f(b)':[f(b)], '|b - a|':[abs(b-a)]})
    table.index.names = ['it']

    while abs(f(x)) > t and len(table) < lim:
        if abs(b-a) < t:
            if abs(f(a)) < t:
                x = a
            else:
                x = b
            break

        if f(a) * f(x) > 0:
            a = x
        else:
            b = x
        
        x = (a*f(b) - b*f(a)) / (f(b) - f(a))

        table.loc[len(table)] = [a, b, x, f(x), f(a), f(b), abs(b-a)] # Adicionando mais uma linha no dataframe       

    table['f(a)'], table['f(b)'] = table['f(a)'].apply(sinal), table['f(b)'].apply(sinal) 
    
    print('Tabela de execuções (Falsa Posição)\n')
    print(table, '\n')
         
    return x
