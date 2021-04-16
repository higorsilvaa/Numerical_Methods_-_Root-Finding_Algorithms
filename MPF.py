import pandas as pd

def f(x):
    return #definir a função

def fi(x):
	  #fi nada mais é do que o ilosamento de um x
    #Ex.: Dada a função y = x²-x+9, fi¹(x) poderia ser x²+9, onde isolamos -x e fi²(x) poderia ser ²v(x-9), ou seja, raiz quadrada de x-9.
    return #definir a função de isolamento de x

def dfi(x):
    return #definir a derivada de fi(x)

def MPF(x, t): #Onde x é o chute inicial e t é a precisão, f é a função de x, fi é a função onde isolamos um x e dfi é a derivada de fi
    a, x0 = dfi(x), x
    
    if abs(a) <= 1.0: #Condição de convergência
        print('Derivada dfi(x): %f\n' % a)
        
        table = pd.DataFrame({'x':[x0], 'fi(x)':[fi(x0)], 'f(x)':[f(x0)], '|x - x0|':[abs(fi(x0)-x0)]})
        table.index.names = ['it']
        
        while True:
            x1 = fi(x0)
            
            if abs(f(x1)) < t or abs(x1 - x0) < t:
                break
    
            x0 = x1

            table.loc[len(table)] = [x0, fi(x0), f(x0), abs(fi(x0)-x0)] # Adicionando mais uma linha no dataframe
    
        print('Tabela de execuções (MPF)\n')
        print(table, '\n')
    
        return x1
    else:
        print("Não possui raiz nesse intervalo!")
