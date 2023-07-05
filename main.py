from pokedex import Pokedex
from pokemon import Pokemon
from equipo import Equipo
from pokeball import Pokeball, Superball, Masterball, Ultraball
import random
import time

def main():
    pokedex = Pokedex()
    equipo = Equipo()
   
    with open("images/pokemon", encoding="utf8") as poke:
        content = poke.read()
        print(content)
    
    num = 0
    while(num == 0):
        print("\nTe encuentras sano y salvo en tu casa...\n")
        time.sleep(1)
        print("\n ¿Que desea hacer? Elija una opción:")
        print("\n 1-¡Atrapar un Pokémon!")
        print("\n 2-Abrir la Pokedex")
        print("\n 3-Borrar un Pokémon de la Pokedex")
        print("\n 4-Visualizar Equipo")
        num = input("\n")
        
        if int(num) == 1:
            print("Antes de adentrarte en las altas yerbas, has agarrado un puñado de pokeballs de la mesa...\n")
            ty = random.randint(1, 4)
            
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".\n")
            
            if ty == 4:
                cant = 1
                print("Haz adquirido: 1 x Masterball")
                pokeballs = Masterball()
            else:
                cant = random.randint(1, 5)
                if ty == 1:
                    print("Haz adquirido: " + str(cant) + " x Pokeballs")
                    pokeballs = Pokeball(cant)
                elif ty == 2:
                    print("Haz adquirido: " + str(cant) + " x Superballs")
                    pokeballs = Superball(cant)
                elif ty == 3:
                    print("Haz adquirido: " + str(cant) + " x Ultraballs")
                    pokeballs = Ultraball(cant)
            print("\n")
            
            num2 = 0
            while (num2 == 0 ):
                print("Te has adentrado en las yerbas altas...")

                clock = random.randint(1, 10)
                for i in range(0, clock):
                    print(".")
                    time.sleep(1)
                print("\n¡¡¡ HA APARECIDO UN POKÉMON !!!\n\n")

                img = random.randint(1, 17)
                ps = random.randint(1, 3)
                nivel = random.randint(1, 10)
                
                num3 = 0
                while(num3 == 0):
                    with open("images/" + str(img), encoding="utf8") as im:
                        imagen = im.read()
                        print(imagen)

                    if ps == 1:
                        print("\nTiene los PS(Puntos de Salud) bajos\n")
                    elif ps == 2:
                        print("\nTiene los PS(Puntos de Salud) a la mitad\n")
                    elif ps == 3:
                        print("\nTiene los PS(Puntos de Salud) altos\n")
                    
                    print("y su nivel es NV: " + str(nivel))
                    time.sleep(1)
                
                
                    print("\n\n ¡¿ Qué vas a hacer?! \n 1-Lanzar una pokeball \n 2-¡Huir!")
                    option = input("\n")

                    if int(option) == 1:
                        ind = pokeballs.Lanzar_Pokeball()
                        
                        if ind == 0:
                            print("El Pokémon ha escapado...\n")
                            print("Te marchas a casa...\n")
                            num2 = 1
                            num = 0
                            num3 = 1
                            break
                        else:
                            plus = random.randint(0, 2)
                            if img == 7:
                                for i in range(0, 2):
                                    print(".")
                                    time.sleep(1)
                                with open("images/untrap", encoding="utf8") as im:
                                    untrap = im.read()
                                    print(untrap)
                                print("\n¡El Pokémon se ha liberado de la pokeball!\n")
                                print("El Pokémon ha escapado...\n")
                                num3 = 1
                                continue
                            elif ps + plus > ind:
                                for i in range(0, 2):
                                    print(".")
                                    time.sleep(1)
                                with open("images/untrap", encoding="utf8") as im:
                                    untrap = im.read()
                                    print(untrap)
                                print("\n¡El Pokémon se ha liberado de la pokeball!\n")
                                num3 = 0
                                continue
                            elif ps + plus > ind and plus == 2:
                                for i in range(0, 2):
                                    print(".")
                                    time.sleep(1)
                                with open("images/untrap", encoding="utf8") as im:
                                    untrap = im.read()
                                    print(untrap)
                                print("\n¡El Pokémon se ha liberado de la pokeball!\n")
                                print("El Pokémon ha escapado...\n")
                                num3 = 1
                                continue
                            elif ps + plus <= ind:
                                for i in range(0, 2):
                                    print(".")
                                    time.sleep(1)
                                print("¡¡Has atrapado al Pokémon!!\n")
                                
                                with open("images/trap", encoding="utf8") as im:
                                    trap = im.read()
                                    print(trap)

                                nombre = input("\n ¿Qué mote desea ponerle al Pokémon\n")
                                tipo = int(input("Elija el Tipo #1 del Pokémon: \n 1-planta\n 2-fuego\n 3-agua\n 4-rayo\n 5-lucha\n 6-insecto\n 7-siniestro\n 8-psiquico\n 9-tierra\n 10-roca\n 11-acero\n 12-dragon\n 13-hada\n 14-hielo\n 15-normal\n 16-volador\n 17-veneno\n 18-fantasma\n"))
                                tipo2 = int(input("Elija el Tipo #2 del Pokémon: \n 0-No tiene\n 1-planta\n 2-fuego\n 3-agua\n 4-rayo\n 5-lucha\n 6-insecto\n 7-siniestro\n 8-psiquico\n 9-tierra\n 10-roca\n 11-acero\n 12-dragon\n 13-hada\n 14-hielo\n 15-normal\n 16-volador\n 17-veneno\n 18-fantasma\n"))
                                naturaleza = random.randint(1, 24)
                                descripcion = input("\n Escriba una descripción, sobre el Pokémon capturado, para la Pokedex: \n")
                                
                                pokemon = Pokemon("images/"+str(img), nombre, tipo, tipo2, nivel, ps, naturaleza, descripcion)
                                
                                if pokedex.Buscar_Pokemon_Pokedex(imagen[0:15]) == 1:
                                    print("El Pokémon capturado ya se encuentra en la Pokedex")
                                else:
                                    pokedex.Insertar_Pokemon(pokemon)
                        
                                equipo.Insertar_Pokemon(pokemon)
                                
                                print("¿Quieres volver a casa? S=Sí , N=No\n")
                                opt = input()
                                if opt.capitalize() == "S":
                                    num3 = 1
                                    num2 = 1
                                    num = 0
                                    break
                                else:
                                    num3 = 1
                                    continue                   
                                
                    elif int(option) == 2:     
                        print("\nHas escapado con exito!\n")
                        time.sleep(1)
                        print("¿Quieres volver a casa? S=Sí , N=No\n")
                        opt = input()
                        if opt.capitalize() == "S":
                            num3 = 1
                            num2 = 1
                            num = 0
                            break
                        else:
                            num3 = 1
                            continue
                    
                    else:
                        print("Debe entrar un número valido!!")
                        num3 = 0
                        continue
        
        elif int(num) == 2:
            print("\nHas Abierto la Pokedex...\n")
            for i in range(0, 2):
                print(".")
                time.sleep(1)
            pokedex.__str__()
            num = 0
            continue
        
        elif int(num) == 3:
            print("\n ¿Cómo desea borrar el Pokémon? \n 1-Por su número de Pokedex\n 2-Por su nombre\n")
            opt = input()
            if int(opt) == 1:
                print("\nEscriba el número de Pokedex del Pokémon a borrar:\n")
                num = input()
                pokedex.Borrar_Pokemon_Indice(int(num))
                num = 0
                continue
            elif int(opt) == 2:
                print("\nEscriba el nombre del Pokémon a borrar:\n")
                nom = input()
                pokedex.Borrar_Pokemon_Nombre(nom)
                num = 0
                continue
        elif int(num) == 4:
            equipo.Mostrar_Equipo() 
            num = 0
            continue
                                   
                    
            
            
            
            
            
if __name__ == "__main__":
    main()