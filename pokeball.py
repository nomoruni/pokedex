class Pokeball:
    def __init__(self, cantidad = 1, ind_cap = 1):
        self.cantidad = cantidad
        self.ind_cap = ind_cap
    
    def Lanzar_Pokeball(self):
        if self.cantidad >= 1:
            print("Has lanzado una Pokeball")
            self.cantidad -= 1
            return self.ind_cap
        else:
            print("Ya no te quedan Pokeballs")
            return 0
        

class Superball(Pokeball):
    
    def __init__(self, cantidad, ind_cap = 3):
        super().__init__(cantidad, ind_cap)
    
    def Lanzar_Pokeball(self):
        if self.cantidad >= 1:
            print("Has lanzado una Superball")
            self.cantidad -= 1
            return self.ind_cap
        else:
            print("Ya no te quedan Superballs")
            return 0
        
class Ultraball(Pokeball):
    
    def __init__(self, cantidad, ind_cap = 5):
        super().__init__(cantidad, ind_cap)
    
    def Lanzar_Pokeball(self):
        if self.cantidad >= 1:
            print("Has lanzado una Ultraball")
            self.cantidad -= 1
            return self.ind_cap
        else:
            print("Ya no te quedan Ultraballs")
            return 0

class Masterball(Pokeball):
    
    def __init__(self, cantidad = 1, ind_cap = 10):
        super().__init__(cantidad, ind_cap)
    
    def Lanzar_Pokeball(self):
        if self.cantidad >= 1:
            print("Has lanzado la Masterball\n")
            self.cantidad -= 1
            return self.ind_cap
        else:
            print("Ya has gastado la Masterball\n")
            return 0  
    

       
        