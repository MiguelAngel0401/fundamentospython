#Funciones
#def name_function():
#  code

#Funciones sin parametros
#Funciones sin retorno
def saluda():
    print("Hola Developers!")

saluda()

#Parametros, sin retorno
def duplica(number):
    print(number*2)

duplica(23)

def suma(num1,num2):
    print(num1 + num2)

suma(12,34)

#Parametros Opcionales
def lista_drinks(d1 = "beer", d2 = "water"):
    print(d1)
    print(d2)

lista_drinks("tequila", "juice")
lista_drinks("tequila")
lista_drinks()
lista_drinks(d2 = 'soda' , d1= "codka")

#Funciones con retorno
#return

def get_list():
    return[1,2,3]

list_gotten=get_list()
print(list_gotten)

def resta(num1, num2):
    return num1-num2

result= resta(13,2)
print(result)

def duplica_lista(lista):
    new_list=[]
    for item in lista:
        new_list.append(item*2)
    return new_list

my_list= [1,2,3,4,5]
print(my_list)
new_list=duplica_lista(my_list)
print(new_list)
