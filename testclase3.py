
numero1 : int
numero2 : int
resultado : float

#Funciones definidas para su posterior utilizacion
def sumar(a,b) :
  resultado = int(a + b)
  return resultado

def resta(a,b) :
  resultado = int(a-b)
  return resultado

def multiplicar(a,b) :
  resultado = int(a*b)
  return resultado

def dividir(a,b) :
  
    resultado = a/b 
  
    return resultado
  

def menu():
  option = 0

  while True :
   try:
      print("Calculadora")
      print("1) SUMA")
      print("2) RESTA")
      print("3) MULTIPLICACION")
      print("4) DIVISION")
      print("5) SALIR")
      option = int(input("Seleccione el numero de operacion: "))
   
      match option:
        case 1:
          
            numero1 = int(input("Ingresar primer numero: "))
            numero2= int(input("Ingrese el segundo numero: "))
            resultado = sumar(numero1,numero2)
            print(f"el resultado es: {resultado}")
         
        case 2:
         
           numero1 = int(input("Ingresar primer numero: "))
           numero2= int(input("Ingrese el segundo numero: "))
           resultado = resta(numero1,numero2)
           print(f"el resultado es: {resultado}")
         
        case 3:
         
            numero1 = int(input("Ingresar primer numero: "))
            numero2= int(input("Ingrese el segundo numero: "))
            resultado = multiplicar(numero1,numero2)
            print(f"el resultado es: {resultado}")
         
        case 4:
            try :
              numero1 = int(input("Ingresar primer numero: "))
              numero2= int(input("Ingrese el segundo numero: "))
              resultado = dividir(numero1,numero2)
              print(f"el resultado es: {resultado}")
            except ZeroDivisionError:
              print("No se puede dividir por 0")
         
        case 5:
          print(f"Gracias por usar la calculadora")
          print(f"Fin del programa")

      if option == 5 :
        break

       # case default:
        #  print(f"Opcion incorrecta") 
   except ValueError:
     print("Opcion no válida")  

     
  
