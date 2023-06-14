comidas=[]

def show_comidas():
    for comida in comidas:
        print(f"Comida {comida}")

def add_comida(comida):
     comidas.append(comida)

def del_comida(comida):
  try:
     comidas.remove(comida)
  except Exception:
     print("No se encuentra en la lista")

text_menu='''
            Elige una opcion:
            1-Agregar Comida
            2-Eliminar Comida
            3-Mostrar comidas
            4-Salir
            '''
while True:
    choice_user=int(input(text_menu))
    if choice_user==1:
        comida=input("Escribe una comida:")
        add_comida(comida)
    elif choice_user==2:
        comida=input("Escribe una comida:")
        del_comida(comida)
    elif choice_user==3:
        show_comidas()
    elif choice_user==4:
        break
    else:
        print("Escribe bien :/")
            
   