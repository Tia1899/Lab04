class Stand:
    def __init__(self,codice,metriquadri,padiglione,costo):
        self.codice = codice
        self.metriquadri = metriquadri
        self.padiglione = padiglione
        self.costo = costo
    def __str__(self):
        return f"{self.codice} {self.metriquadri} {self.padiglione} {self.costo}"