numeros = [7,3,1,2,4,6,9,5,8]

def ordenamientoBurbuja(numeros):
    n = len(numeros)
    anterior = 0
    for i in range(n):
        for j in range(0, n-1): 
            if numeros[j] > numeros[j+1]:
                anterior = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = anterior
                
    return numeros

print(ordenamientoBurbuja(numeros))





def ordenamientoBurbuja2(numeros):
    anterior = 0
    n = len(numeros)
    for i in range(n):
        for j in range(0, n-1): 
            if numeros[j] > numeros[j+1]:     
                # print(f"entro: {numeros[j]} - {numeros[j+1]}")
                anterior = numeros[j]
                # print(f"anterior: {anterior}")
                numeros[j] = numeros[j+1]
                numeros[j+1] = anterior
            print(f"el ordenamiento va así...: {numeros}")
                
            # print(f"i:{i} - j:{j}")

                
        # break
    # return numeros    
print(ordenamientoBurbuja2(numeros))