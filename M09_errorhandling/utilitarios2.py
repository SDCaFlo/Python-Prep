class Utilitarios:
    def __init__(self, lista):
        if type(lista)==list:
            self.lista = lista
            for item in self.lista:
                if type(item)!=int:
                    raise TypeError("Se requiere que los elementos de la lista sean enteros")
                elif item<=0:
                    raise ValueError("Los numeros en la lista deben ser positivos")                   
        else:
            raise TypeError("Se requiere una lista como tipo de dato")
        
    # metodo que verifica por numero
    def es_primo_num(self, num):
        assert type(num)==int, "Se debe usar un número entero"
        assert num > 0, "El número debe ser positivo mayor que 0"
        for i in range(2, num):
            if num%i==0:
                return False
            else:
                return True
            
    # metodo que verifica por lista
    def es_primo_lista(self):
        lista_primos = []
        for num in self.lista:
            if self.es_primo_num(num):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos
    
    # cambiamos el método para que use la lista provista en la instancia.
    def encontrar_repetidos(self):
        count = 0
        numero = 0
        for num in self.lista:
            if self.lista.count(num)>count:
                numero = num
                count = self.lista.count(num)
        return numero, count
    

    # método usado para conversión de valores dados. 
    def conversion_temperatura(self, valor, escala_origen: str, escala_destino: str):
        """Convierte entre diferentes tipos de escalas de medición de temperatura.
        Las escalas de origen y destino se especifican con las letras: "C", "K" y "F". """
        if type(valor)!=int and type(valor)!=float:
            raise TypeError("El valor debe ser float o int")
        
        if type(escala_origen)!=str or type(escala_destino)!=str:
            raise TypeError("El valor de las escalas origen y destino debe ser string, (K/C/F)")
        escala_origen = escala_origen.casefold()
        escala_destino = escala_destino.casefold()
        resultado = 0

        # 1. convertir a Celsius.
        if escala_origen == "c":
            pass
        elif escala_origen == "k":
            valor -= 273
        elif escala_origen == "f":
            valor = (valor-32)*(5/9)
        else:
            raise ValueError("Por favor ingresar escala origen valida, \nKelvin: 'K/k'\nCelsius: 'C/c'\nFarenheit: 'F/f'")
        
        if escala_destino == "c":
            resultado = valor
        elif escala_destino == "k":
            resultado = valor + 273
        elif escala_destino == "f":
            resultado = (valor*9/5) + 32
        else:
            raise ValueError("Por favor ingresar escala destino valida")
        
        return resultado   

    # nuevo método para convertir valores de la lista.
    def conversion_temperatura_lista(self, escala_origen: str, escala_destino: str):
        for valor in self.lista:
            resultado = self.conversion_temperatura(valor, escala_origen, escala_destino)
            print(valor, escala_origen, "a ", escala_destino, "es igual a: ", resultado)    

    # calcula factorial para un solo numero.        
    def calcular_factorial(self, num):
        if num<1 or type(num)!=int:
            raise ValueError("Verificar la variable ingresada")

        if num>1:
            num = num * self.calcular_factorial(num-1)      # aqui es necesario agregar la palabra SELF.
        return num
    
    # calcula factoriales para la lista de numeros provistos en la definicion de la instancia.}

    def calcular_factorial_lista(self):
        for num in self.lista:
            factorial = self.calcular_factorial(num)
            print(f"El factorial de {num} es {factorial}")