
class Veiculo:
    def movimentar(self):
          print(f'Sou um veículo e me desloco')

    def __init__(self, fabricante, modelo) :
         self.__fabricante = fabricante
         self.__modelo = modelo
         
    def get_fabricante(self):
     print(f' Fabricante: {self.__fabricante}. \n')
    def get_modelo(self):
     print(f' Modelo: {self.__modelo}. \n')


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac') 
    meu_veiculo.movimentar()
    print(meu_veiculo.get_fabricante())
    print(meu_veiculo.get_modelo())