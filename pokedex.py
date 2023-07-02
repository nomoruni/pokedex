from pokemon import Pokemon, t_tipo
from os import remove, rename

class Pokedex:
    
    def __init__(self):
        try:
            with open("amount") as num:
                self.numero = int(num.read())
        except FileNotFoundError:
            with open("amount", "w") as num:
                num.write("0")
            self.numero = 0
        
        
    def Insertar_Pokemon(self, imagen, nombre, tipo, tipo2, nivel, ps, naturaleza, descripcion):
        pokemon = Pokemon(imagen, nombre, tipo, tipo2, nivel, ps, naturaleza, descripcion)
        self.Escribir_Archivo_Pokemons(pokemon)
        print("Pokemon Agregado a la Pokedex")
        
    def Borrar_Pokemon_Indice(self, indice):
        remove("db/" + str(indice))
        for i in range(int(indice), self.numero):
            rename("db/" + str(i+1), "db/" + str(i))
        self.numero -= 1
        with open("amount", "w") as num:
            num.write(str(self.numero))
        print("Pokemon Borrado de la Pokedex")
    
    def Borrar_Pokemon_Nombre(self, nombre):
        confirm = 0
        for i in range(1, self.numero+1):
            with open("db/" + str(i)) as num:
                content = num.read()
                if content.find(str(nombre).title()):
                    remove("db/" + str(i))
                    if self.numero != 1:
                        for i in range(1, self.numero):
                            rename("db/" + str(i+1), "db/" + str(i))
                    self.numero -= 1
                    with open("amount", "w") as num:
                        num.write(str(self.numero))
                    confirm = 1
                    break
        if confirm == 1:
            print("Pokemon borrado de la Pokedex.")
        else:
            print("El Pokemon no existe.")
        
    
    def Escribir_Archivo_Pokemons(self, pokemon):
        
        with open("db/" + str(self.numero+1), "w") as file_object:
            file_object.write(pokemon.Escribir_Pokedex())
            self.numero += 1
                
        with open("amount", "w") as num:
            num.write(str(self.numero))
                
        print("Base de datos guardada")
    
    def Buscar_Pokemon_Pokedex(self, nombre):
        confirm = 0
        for i in range(1, self.numero+1):
            with open("db/" + str(i)) as num:
                content = num.read()
                if content.find(nombre):
                    confirm = 1
                    break
        if confirm == 1:
            return confirm
        else:
            return 0
    
    def __str__(self):
        try:
            for poke in range(1, self.numero+1):            
                with open("db/" + str(poke)) as file_text:
                    content = file_text.read()
                    print("No: " + str(poke) + " " +  content + "\n")
        except FileNotFoundError:
            print("El archivo no existe!!")
            return 0
    
    
            
            
            
        
        