# Lista para almacenar los datos de las personas
people = []

# Solicitar el número de personas a registrar con validación
while True:
    try:
        number = int(input("Ingrese la cantidad de personas que desea registrar: "))
        if number <= 0:
            print("Debe ingresar un número positivo.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Ingresar los datos de cada persona
for i in range(number):
    print(f"\nRegistro de la persona {i + 1}:")
    name = input("Ingrese el Nombre: ")
    
    while True:
        try:
            age = int(input("Ingrese la Edad: "))
            if age <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")

    while True:
        try:
            note = float(input("Ingrese la Nota: "))
            if note < 0 or note > 10:
                print("La nota debe estar entre 0 y 10.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la nota.")

    people.append((name, age, note))

# Mostrar lista original
print("\nListado de personas ingresadas:")
for person in people:
    print(f"Nombre: {person[0]}, Edad: {person[1]}, Nota: {person[2]}")

# Ordenar la lista por nota de mayor a menor
people.sort(key=lambda x: x[2], reverse=True)

# Mostrar lista ordenada por nota
print("\nListado ordenado por nota (de mayor a menor):")
for person in people:
    print(f"Nombre: {person[0]}, Edad: {person[1]}, Nota: {person[2]}")
