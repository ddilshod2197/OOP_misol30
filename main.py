class Mashina:
    def __init__(self, nom, yil, yuk=0):
        self.nom = nom
        self.yil = yil
        self.yuk = yuk
    
    def yuk_qosh(self, kg):
        if kg > 0:
            self.yuk += kg
            print(f"📦 {kg} kg yuk qo‘shildi. Joriy yuk: {self.yuk} kg")
        else:
            print("Xato: Yuk musbat bo‘lishi kerak!")
    
    def malumot(self):
        print(f"🚚 Mashina: {self.nom} ({self.yil})")
        print(f"Joriy yuk: {self.yuk} kg")

# Test
mashina = Mashina("KamAZ", 2022)
mashina.yuk_qosh(2500)
mashina.yuk_qosh(1800)
mashina.malumot()
