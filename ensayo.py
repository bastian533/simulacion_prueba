import os

CARGOS = ["CEO", "Desarrollador", "Analista de datos"]

def registrar_trabajador():

    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")  
    cargo = input("Ingrese el cargo del trabajador (CEO, Desarrollador, Analista de datos): ") 
    while cargo not in CARGOS:

        print("Cargo no válido. Los cargos válidos son:", ", ".join(CARGOS))
        cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    os.system("cls")
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    os.system("cls")
    print("\nRegistro exitoso: ")
    print("Nombre y Apellido:", nombre, apellido)
    print("Cargo:", cargo)
    print("Sueldo Bruto:", sueldo_bruto)
    print("Descuento Salud:", desc_salud)
    print("Descuento AFP:", desc_afp)
    print("Líquido a pagar:", liquido_pagar)
    return nombre, apellido, cargo, sueldo_bruto, desc_salud, desc_afp, liquido_pagar
os.system("cls") 

def listar_trabajadores(trabajadores):
    print("\nLista de Trabajadores:")
    os.system("cls")

    for trabajador in trabajadores:

        print("Nombre y Apellido:", trabajador[0], trabajador[1])
        print("Cargo:", trabajador[2])
        print("Sueldo Bruto:", trabajador[3])
        print("Descuento Salud:", trabajador[4])
        print("Descuento AFP:", trabajador[5])
        print("Líquido a pagar:", trabajador[6])
        print()

def imprimir_planilla(trabajadores):
    seleccion = input("Ingrese el cargo para imprimir la planilla (CEO, Desarrollador, Analista de datos): ")
    while seleccion not in CARGOS:
        print("Cargo no válido. Los cargos válidos son:", ", ".join(CARGOS))
        seleccion = input("Ingrese el cargo para imprimir la planilla: ")
    filename = f"planilla_{seleccion}.txt"
    with open(filename, "w") as file:
        file.write(f"Planilla de Sueldos para el cargo de {seleccion}:\n\n")
        for trabajador in trabajadores:
            if trabajador[2] == seleccion:
                file.write(f"Nombre y Apellido: {trabajador[0]} {trabajador[1]}\n")
                file.write(f"Cargo: {trabajador[2]}\n")
                file.write(f"Sueldo Bruto: {trabajador[3]}\n")
                file.write(f"Descuento Salud: {trabajador[4]}\n")
                file.write(f"Descuento AFP: {trabajador[5]}\n")
                file.write(f"Líquido a pagar: {trabajador[6]}\n\n")
    print(f"Se ha generado el archivo '{filename}' con la planilla de sueldos para el cargo de {seleccion}")


def main():
    trabajadores = []
    while True:
        print("\n--- Menú ---")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del Programa")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            trabajadores.append(registrar_trabajador())
        elif opcion == "2":
            if trabajadores:
                listar_trabajadores(trabajadores)
            else:
                print("No hay trabajadores registrados.")
        elif opcion == "3":
            if trabajadores:
                imprimir_planilla(trabajadores)
            else:
                print("No hay trabajadores registrados.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
