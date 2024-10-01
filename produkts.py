class Produkts:
    def __init__(self, name, amount, pvaip = 0 ):
        self.skaits = amount
        self.vards = name
        self.pvaid = pvaip
    
    def mainit_skaitu(self, jaunais_skaits):
        self.skaits = jaunais_skaits
        self.info()

    def mainit_pvaid(self, jaunais_pvaid):
        self.pvaid = jaunais_pvaid
        self.info()
    
    def mainit_vardu(self, jaunais_vards):
        self.vards = jaunais_vards
        self.info()
    
    def mainit_pvaid(self, jaunais_pvaid = ""):
        if jaunais_pvaid == "":
            if self.pvaid == "d":
                self.pvaid = "p"
            else:
                self.pvaid = "d"
        else:
            self.pvaid = jaunais_pvaid
        self.info()

    def info(self):
        if self.pvaid == "p":
            teksts = "programma"
        elif self.pvaid == "d":
            teksts = "detaļa"
        else:
            teksts = self.pvaid
        print("Nosaukums : {}. Skaits : {} Programma vai detaļa : {}.".format(self.vards, self.skaits, teksts))
        return "Nosaukums : {}. Skaits : {} Programma vai detaļa : {}.".format(self.vards, self.skaits, teksts)
    



class Dators(Produkts):
    def __init__(self, name, manufacturer, age = 0):
        super().__init__(name,"d", age)
        self.razotajs = manufacturer
        self.info()

    def info(self):
        super().info()
        print("Ražotājs :", self.razotajs)