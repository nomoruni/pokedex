import json
from os import remove, rename

t_tipo=["planta", "fuego", "agua", "rayo", "lucha", "insecto", "siniestro", "psiquico", "tierra", "roca", "acero", "dragon", "hada", "hielo", "normal", "volador", "veneno"]
#t_nat=["activa", "afable", "agitada", "alegre", "alocada", "amable", "audaz", "cauta", "dócil", "firme", "floja", "fuerte", "grosera", "huraña", "ingenua", "mansa", "miedosa", "modesta", "osada", "pícara", "rara", "serena", "seria", "tímida"]

class Pokemon():
    def __init__(self, nombre, tipo, tipo2, descripcion):
        self.nombre = nombre.title()
        self.tipo = str(t_tipo[tipo - 1])
        if int(tipo2) != 0:
            self.tipo2 = str(t_tipo[tipo2 - 1])
        else:
            self.tipo2 = "-"
        self.descripcion = descripcion
        
    def __str__(self):
        return " Nombre: " + self.nombre + " Tipo #1: " + self.tipo + " Tipo #2: " + self.tipo2 + " Descripción: " + self.descripcion + "\n"

class Pokedex:
    
    def __init__(self):
        try:
            with open("amount") as num:
                self.numero = int(num.read())
            self.pokemons = []
        except FileNotFoundError:
            with open("amount", "w") as num:
                num.write("0")
            self.numero = 0
            self.pokemons = []
        
        
    def Insertar_Pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("Pokemon Agregado a la Pokedex")
        
    def Borrar_Pokemon_Indice(self, indice):
        remove("db/" + str(indice))
        for i in range(indice, self.numero+1):
            rename("db/" + str(i+1), "db/" + str(i))
        self.numero -= 1
        print("Pokemon Borrado de la Pokedex")
    
    def Borrar_Pokemon_Nombre(self, nombre):
        confirm = 0
        for i in range(0, self.numero+1):
            with open("db/" + i) as num:
                content = num.read()
                if conten.find(str(nombre).title()):
                    remove("db/" + i)  
                    for i in range(indice, self.numero+1):
                        rename("db/" + str(i+1), "db/" + str(i))
                    self.numero -= 1
                    confirm = 1
                    break
        if confirm == 1:
            print("Pokemon borrado de la Pokedex.")
        else:
            print("El Pokemon no existe.")
        
    
    def Escribir_Archivo_Pokemons(self):
        
        for poke in self.pokemons:
            with open("db/" + str(self.numero+1), "w") as file_object:
                file_object.write(poke.__str__())
                self.numero += 1
                
        with open("amount", "w") as num:
            num.write(str(self.numero))
                
        print("Base de datos guardada")
    
    def __str__(self):
        try:
            for poke in range(1, self.numero+1):            
                with open("db/" + str(poke)) as file_text:
                    content = file_text.read()
                    print("No: " + str(poke) + " " +  content + "\n")
        except FileNotFoundError:
            print("El archivo no existe!!")
            return 0
    
    
            
            
            
        
        