t_tipo=("planta", "fuego", "agua", "rayo", "lucha", "insecto", "siniestro", "psiquico", "tierra", "roca", "acero", "dragon", "hada", "hielo", "normal", "volador", "veneno", "fantasma")
t_nat=("activa", "afable", "agitada", "alegre", "alocada", "amable", "audaz", "cauta", "dócil", "firme", "floja", "fuerte", "grosera", "huraña", "ingenua", "mansa", "miedosa", "modesta", "osada", "pícara", "rara", "serena", "seria", "tímida")
t_ps=("bajos", "medios", "altos")

class Pokemon():
    def __init__(self, imagen, nombre, tipo, tipo2, nivel, ps, naturaleza, descripcion):
        self.imagen = imagen
        self.nombre = nombre.title()
        self.tipo = str(t_tipo[tipo - 1])
        if int(tipo2) != 0:
            self.tipo2 = str(t_tipo[tipo2 - 1])
        else:
            self.tipo2 = "-"
        self.nivel = str(nivel)
        self.ps = str(t_ps[ps - 1])
        self.naturaleza = str(t_nat[naturaleza-1])
        self.descripcion = descripcion
        
    def __str__(self):
        with open(self.imagen, encoding="utf8") as img:
            content = img.read()
            return content + "\n Mote: " + self.nombre + "\n Tipo #1: " + self.tipo + "\n Tipo #2: " + self.tipo2 + "\n Naturaleza: " + self.naturaleza + "\n Descripción: " + self.descripcion + "\n"
    def Escribir_Pokedex(self):
         with open(self.imagen, encoding="utf8") as img:
            content = img.read()
            return "\n Nombre: " + content + "\n Tipo #1: " + self.tipo + "\n Tipo #2: " + self.tipo2 + "\n Descripción: " + self.descripcion + "\n"
    def Get_Nombre(self):
        return self.nombre
    def Get_Tipo1(self):
        return self.tipo
    def Get_Tipo2(self):
        return self.tipo2
    def Get_Nivel(self):
        return self.nivel
    def Get_Ps(self):
        return self.ps
    def Get_Naturaleza(self):
        return self.naturaleza
    def Get_Descripcion(self):
        return self.descripcion