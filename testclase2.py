
edad : int
nombre : str
profesion : str

print("Ingrese sus datos")
nombre = input("cual es su nombre?: ")
edad = int(input("Ingresar edad: "))
profesion = input("Ingresar profesion: ")

print("Datos ingresados")
print("Edad: " + str(edad), "nombre: "+ nombre, "profesion: " + profesion)

print("Numeros pares")

for i in range(10) :
    if i%2==0 :
        print(i)