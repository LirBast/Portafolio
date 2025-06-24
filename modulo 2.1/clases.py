class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

# Creación de objeto
mi_perro = Perro("Fido", 3)
perr2=Perro("firulay",2)
# Acceder a un atributo
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años")
print(f"{perr2.nombre} es un perro travieso de {mi_perro.edad} años")

# Invocar a un método del objeto
mi_perro.ladrar()
perr2.ladrar()