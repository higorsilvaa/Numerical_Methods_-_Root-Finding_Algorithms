import pandas as pd

def f(x):
    return #definir a função

def fi(x,y):
    return (x*f(y) - y*f(x)) / (f(y) - f(x))

def sec(x0, x1, t): #Onde x0 e x1 são os chutes iniciais, fi eh uma função constante, t é a precisão e f é a função
    x2 = fi(x0,x1)
    
    table = pd.DataFrame({'x0':[x0], 'x1':[x1], 'x':[x2], 'f(x)':[f(x2)], '|x - x1|':[abs(x2-x1)]})
    table.index.names = ['it']

    while abs(f(x2)) > t and abs(x2-x1) > t:
        x0 = x1
        x1 = x2
        x2 = fi(x0,x1)
        
        table.loc[len(table)] = [x0, x1, x2, f(x2), abs(x2-x1)] # Adicionando mais uma linha no dataframe

    print('Tabela de execuções (Secante)\n')
    print(table, '\n')
    
    return x2
