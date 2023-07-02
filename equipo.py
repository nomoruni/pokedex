class Equipo:
    def __init__(self):
        self.pokemons = []
    
    def Insertar_Pokemon(self, pokemon):
        if len(self.pokemons) == 6:
            print("Ha exedido el número máximo de Pokémons en el Equipo, el Pokémon será enviado al PC")    
        else:
            self.pokemons.append(pokemon)
            print("Ahora " + pokemon.nombre + " forma parte de tu equipo!")
    
    def Mostrar_Equipo(self):
        print("Este es tu Equipo: \n\n")
        for poke in self.pokemons:
            poke.__str__()
            print("\n")
        