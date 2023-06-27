import json
from os import remove, rename

t_tipo=["planta", "fuego", "agua", "rayo", "lucha", "insecto", "siniestro", "psiquico", "tierra", "roca", "acero", "dragon", "hada", "hielo", "normal", "volador", "veneno"]
t_nat=["activa", "afable", "agitada", "alegre", "alocada", "amable", "audaz", "cauta", "dócil", "firme", "floja", "fuerte", "grosera", "huraña", "ingenua", "mansa", "miedosa", "modesta", "osada", "pícara", "rara", "serena", "seria", "tímida"]

class Pokemon():
    def __init__(self, nombre, tipo, tipo2, genero, descripcion):
        self.nombre = nombre.title()
        self.tipo = str(t_tipo[tipo - 1])
        self.tipo2 = str(t_tipo[tipo2 - 1])
        self.genero = genero
        self.descripcion = descripcion
        
    def __str__(self):
        return "Nombre: " + self.nombre + "Tipo: " + self.tipo + "Genero: " + self.genero + "Naturaleza: " + self.naturaleza + "Descripción: " + self.descripcion + "\n"

class Pokedex:
    
    def __init__(self):
        try:
            with open("amount.txt") as num:
                self.numero = int(num.read())
            self.pokemons = []
        except FileNotFoundError:
            with open("amount.txt", "w") as num:
                num.write("0")
            self.numero = 0
        
        
    def Insertar_Pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        self.numero += 1
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
            with open("db/" + str(self.numero), "w") as file_object:
                file_object.write(poke.__str__())
                self.numero += 1
                
        with open("amount", "w") as num:
            num.write(self.numero)
                
        print("Base de datos guardada")
    
    def __str__(self):
        try:
            for poke in range(0, self.numero+1):            
                with open("db/" + str(poke)) as file_text:
                    content += file.read()
        except FileNotFoundError:
            raise print("El archivo no existe!!")
        else:
            return content
    
    
            
            
            
        
        