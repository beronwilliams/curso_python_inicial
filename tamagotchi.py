

#tamagotchi actividad POO
raza = ("Guerrero", "Mago", "Asesino")
nivel = 1


class tamagotchi():
    
    def __init__(self, nombre):
        self.nombre = "Player"
        self.raza = "Debe subir al nivel 2 para elejir la raza de su Tamagotchi"
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.nivel = 1
        self.nivel_fuerza = 10
        self.nivel_agilidad = 10
        self.nivel_mana = 10
        self.humor = "indiferente"
        self.esta_vivo = True
        
    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Estado de humor: {self.humor}")
        print(f"Clase: {raza}")
        print(f"Nivel del jugador: {nivel}")
        print(f"Fuerza: {self.nivel_fuerza}")
        print(f"Aguilidad: {self.nivel_agilidad}")
        print(f"Mana: {self.nivel_mana}")
        
    def alimentar(self):
        if self.esta_vivo:
            self.nivel_hambre -= 10
            self.nivel_energia -= 15
            if self.nivel_hambre < 0:
                self.nivel_hambre = 0
            if self.nivel_energia < 0:
                self.nivel_energia = 0
            print(f"{self.nombre} tamagotchi alimentado.")


    def jugar(self):
        if self.esta_vivo:
            self.nivel_felicidad += 20
            self.nivel_energia -= 18
            self.nivel_hambre += 10
            if self.nivel_felicidad > 100:
                self.nivel_felicidad = 100
            if self.nivel_energia < 0:
                self.nivel_energia = 0
                
            print(f"{self.nombre} Tamagotchi jugo")
            
            while self.nivel_hambre <= 20:
                    self.nivel_energia - 20
                    self.nivel_felicidad -30
                    break


    def dormir(self):
        if self.esta_vivo:
            self.nivel_energia += 40
            self.nivel_hambre += 5
            if self.nivel_energia > 100:
                self.nivel_energia = 100
            print(f"{self.nombre} durmio y recuperado energías.")
            
            while self.nivel_hambre <= 20:
                    self.nivel_energia - 20
                    self.nivel_felicidad -30
                    break


    def obtener_humor(self):
        if self.nivel_felicidad < 20:
            self.humor = "enojado"
        elif self.nivel_felicidad < 40:
            self.humor =  "triste"
        elif self.nivel_felicidad < 60:
            self.humor =  "indiferente"
        elif self.nivel_felicidad >= 80 or self.nivel_felicidad <= 100:
            self.humor =  "feliz"
        elif self.nivel_felicidad > 101:
            self.humor =  "eufórico"

    def elejir_raza(self):
        if nivel <= 2:
            while True:
                raza = int(input("seleccione la raza de su Tamagotchi: 'Guerrero' , 'Mago' o 'Asesino'"))
                if raza == "Guerrero":
                    self.nivel_fuerza = 100
                    self.nivel_agilidad = 50
                    self.nivel_mana = 25
                    
                    while self.nivel_hambre <= 20:
                        self.nivel_energia - 20
                        self.nivel_felicidad -30
                        break
                    
                    
                elif raza == "Mago":
                    self.nivel_fuerza = 25
                    self.nivel_agilidad = 50
                    self.nivel_mana = 100
                    
                    
                    while self.nivel_hambre <= 20:
                        self.nivel_energia - 20
                        self.nivel_felicidad -30
                        break
                    
                    
                    
                elif raza == "Asesino":
                    self.nivel_fuerza = 50
                    self.nivel_agilidad = 100
                    self.nivel_mana = 50
                    
                    
                    while self.nivel_hambre <= 20:
                        self.nivel_energia - 20
                        self.nivel_felicidad -30
                        break
                    
                    
                else:
                    print ("Opcion incorrecta, vueva a intentar")
                    continue
        
    def subir_de_nivel(self):
        nivel =+ 1
        if nivel < 2:
            nivel_fuerza += 10
            nivel_aguilidad += 10
            nivel_energia += 10
            print ("Felicitaciones has subido de Nivel !")
            print ("ahora puedes elejir la raza de si Tamagotchi")
        elif nivel < 3:
            nivel_fuerza += 10
            nivel_aguilidad += 10
            nivel_energia += 10
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 4:
            nivel_fuerza += 10
            nivel_aguilidad += 10
            nivel_energia += 10
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 5:
            nivel_fuerza += 10
            nivel_aguilidad += 10
            nivel_energia += 10
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 6:
            nivel_fuerza += 10
            nivel_aguilidad += 10
            nivel_energia += 10
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 7:
            nivel_fuerza += 20
            nivel_aguilidad += 20
            nivel_energia += 20
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 8:
            nivel_fuerza += 20
            nivel_aguilidad += 20
            nivel_energia += 20
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 9:
            nivel_fuerza += 20
            nivel_aguilidad += 20
            nivel_energia += 20
            print ("Felicitaciones has subido de Nivel !")
        elif nivel < 10:
            nivel_fuerza += 20
            nivel_aguilidad += 20
            nivel_energia += 20
            print ("Felicitaciones tu Tamagotchi es Nivel Maximo !")
        else:
            nivel = 1
    def verificar_estado(self):
        if self.nivel_energia > 0:
            self.esta_vivo = True
        else:
            self.esta_vivo = False
            
            
