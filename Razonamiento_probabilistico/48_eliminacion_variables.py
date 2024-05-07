

def eliminacion_variable(factor_1,factor_2,eliminar):
    # Eliminar variable de factor 1

    res = {}
    for key, valor_1 in factor_1.items():
        for key_2, valor_2 in factor_2.items():
            if eliminar in key and eliminar in  key_2 and key.index(eliminar)==key_2.index(eliminar):
                nuevo = tuple(v for i, v in enumerate(key)if  i!= key.index(eliminar))
                res.update({**dict(zip(nuevo, [valor_1 * valor_2])), **{'valor': valor_1 * valor_2}})

    return res

factor_1= {('A', 'B', 'C'): 0.3, ('A', 'B', '~C'): 0.7}
factor_2 = {('A', 'C', 'D'): 0.8, ('A', '~C', 'D'): 0.2}

res= eliminacion_variable(factor_1,factor_2,'A')

print(f'se elimino la variable a: {res}')