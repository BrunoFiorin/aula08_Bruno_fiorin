
from abc import ABC, abstractmethod



class Categoria:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Produto(ABC):

    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    @abstractmethod
    def cadastrar(self):
        pass

    
    def getInformacao(self):
        print("Modelo: " , self.modelo )
        print("Cor: " , self.cor)
        print("Preço: " , self.preco)
        print("Categoria: " , self.categoria.id ,", ", self.categoria.nome)


class Desktop(Produto):

    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self.__fonte = potenciaDaFonte

    def getInformacao(self):
        super().getInformacao()
        print("Fonte: " , self.__fonte)

    def setFonte(self, fonte):
        self.__fonte = fonte
        print("Fonte definida como " , self.__fonte)

    def cadastrar(self, lista):
        lista.append(self)

class Notebook(Produto):

    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacao(self):
        super().getInformacao()
        print("Fonte: " , self.__tempoDeBateria)

    def setBateria(self, bateria):
        self.__tempoDeBateria = bateria
        print("Duração de bateria definida como " , self.__tempoDeBateria)

    def cadastrar(self, lista):
        lista.append(self)