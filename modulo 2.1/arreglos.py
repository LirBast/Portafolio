class Perro:
    def __init__(self, nombre):  # Método especial llamado constructor
        self.nombre = nombre     # Atributo del objeto

    def ladrar(self):            # Método normal
        print(f"{self.nombre} está ladrando")
