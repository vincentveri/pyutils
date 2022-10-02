class Documento:

    def __init__(self, numero, data) -> None:
        self.numero = numero
        self.data = data

    
    def __repr__(self) -> str:
        return f"doc. del {self.data} - {self.numero}"