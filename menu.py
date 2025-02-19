import methods 
import os
import inspect 

def cls():
    os.system("cls")

def menu():
    cls()
    print("MENU: \n1.- Ver todos los metodos\n2.- Salir")
    
def methods_list(func):
    return inspect.getmembers(func, inspect.isfunction)

def methods_list_name(func):
    cls()
    methods = methods_list(func)
    for id, name in enumerate(methods):
        print(f"{id + 1}.- {name[0]}")

def methods_func(func, num):
    cls()
    methods = methods_list(func)
    funcion_name = methods[num - 1][0]
    funcion = getattr(func, funcion_name)
    return funcion

def funcion_name(func, num):
    cls()
    methods = methods_list(func)
    funcion_name= methods[num - 1][0]
    print(f"-----{funcion_name.capitalize()}-----\n")

def list_parameters(func):
    parameters = inspect.signature(func).parameters
    print(f"Cantidad de parametros: {len(parameters)}\n")
    for nombre, param in parameters.items():
        print(f"Nombre del parametro: {nombre}")
        print(f"Tipo de dato del parametro: {param.annotation}\n")
    return len(parameters)

def type_parameter(func):
    parameters = inspect.signature(func).parameters
    return [param.annotation for _, param in parameters.items()]

def result(len, type_param, function):
    if len == 1:
        param = input("Escribe el dato del parametro: ")
        if type_param[0] is int:
            print(function(int(param)))
        else:
            print((param))
    else:
        param1 = input("Escribe el dato del primer parametro: ")
        param2 = input("Escribe el dato del segundo parametro: ")
        if (type_param[0] is str) and (type_param[1] is str):
            print(function(param1, param2)) 
        else:
            print(function(param1, int(param2)))

while True:
    try:
        menu()
        option = int(input("Elegir opcion: "))
        if option > 3 or option <= 0: continue
         
        if option == 1:
            methods_list_name(methods)
            option = int(input("Elegir opcion: "))
            if option > 16: continue

            function = methods_func(methods, int(option))
            funcion_name(methods, int(option))
            len_param = list_parameters(function)
            type_param = type_parameter(function) 

            result(len_param, type_param, function)
        elif option == 2:
            cls()
            print("Finalizacion del programa")
            break

    except Exception as err:
        print(f"ERROR: {err}")
    input("\nContinuar(precione Enter): ")