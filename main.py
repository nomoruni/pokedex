from clases import Pokemon, Pokedex

def main():
    pokedex = Pokedex()
    num=0
    while(num==0):
        print("Bienvenido a la Pokedex en consola! \n Que desea hacer?\n\n")
        print("1-Visualizar Pokemons creados\n")
        print("2-Insertar un Pokemon nuevo\n")
        print("3-Borrar un Pokemon de la lista\n\n")
        
        num = int(input("Ingrese un número de 1-3:"))
        
        if num == 1:
            if pokedex.__str__() == 0:
                num = 0
                print("No existe ningun pokemon en la pokedex aún. Cree uno!\n \n")
            num = 0
            
        if num == 2:
            nombre = input("Inserte el nombre del pokemon: \n")
            
            tipo = input("Elija el tipo: \n 1-planta\n 2-fuego\n 3-agua\n 4-rayo\n 5-lucha\n 6-insecto\n 7-siniestro\n 8-psiquico\n 9-tierra\n 10-roca\n 11-acero\n 12-dragon\n 13-hada\n 14-hielo\n 15-normal\n 16-volador\n 17-veneno\n")
            lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "14", "15", "16", "17"]
            
            tipo2 = input("Entre el tipo secundario, si tiene solo uno entre 0: \n 1-planta\n 2-fuego\n 3-agua\n 4-rayo\n 5-lucha\n 6-insecto\n 7-siniestro\n 8-psiquico\n 9-tierra\n 10-roca\n 11-acero\n 12-dragon\n 13-hada\n 14-hielo\n 15-normal\n 16-volador\n 17-veneno\n")
            
            if tipo not in lista or tipo == 0 or tipo2 not in lista:  
                print("Debe entrar un número valido!! \n")
                num = 0
                continue    
            elif tipo2 == tipo:
                tipo2 = 0
            
            descripcion = input("Por ultimo, escriba una breve descripción del Pokemon: \n")
            
            pokemon = Pokemon(nombre, int(tipo), int(tipo2), genero, descripcion)
            pokedex.Insertar_Pokemon(pokemon)
            pokedex.Escribir_Archivo_Pokemons()
            num = 0
        if num == 3:
            choise = input("Que metodo desea usar: \n 1-Borrar por número de Pokedex \n 2-Borrar por nombre")
            if choise == 1:
                indice = input("Entre el número de Pokemon: \n")
                pokedex.Borrar_Pokemon_Indice(indice)
                num = 0
            if choise == 2:
                nombrep = input("Entre el nombre del Pokemon: \n")
                pokedex.Borrar_Pokemon_Nombre(nombrep)
                num = 0
            else: 
                print("Escoja una opcion válida!!")
                num = 0
                continue
                
    
if __name__ == "__main__":
    main()