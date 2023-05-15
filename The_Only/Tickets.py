class Ticket(object):
    def __init__(self, meia, idoso, aleijado, autista, inteira=40):
        self.inteira = inteira
        self.meia = meia
        self.idoso = idoso
        self.aleijado = aleijado
        self.autista = autista
    
    def get_inteira(self):
        return self.inteira
    def set_inteira(self, new):
        if isinstance(new, float):
            self.inteira = new
        else:
            print("Erro. Entrada inválida")
    def get_meia(self):
        return self.meia
    def set_meia(self, new):
        self.meia = self.get_inteira / 2
        if isinstance(new, float):
              self.meia = new
        else:
            print("Erro. Entrada inválida")
    def get_idoso(self):
        return self.idoso
    def set_idoso(self,  new):
        self.idoso = self.get_inteira / 
