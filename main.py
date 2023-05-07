from classPlanAhorro import PlanAhorro
import csv
#print("{:.2f}".format(planes[0].getImporteCuota()))

if __name__ == '__main__':
    planes = []
    archivo = open('C://Users//csv//planes.csv', 'r')
    reader = csv.reader(archivo, delimiter=";")
    for fila in reader:
        cod = int(fila[0])
        mod = fila[1]
        ver = fila[2]
        val = float(fila[3])
        xPlan = PlanAhorro(cod, mod, ver, val)
        planes.append(xPlan)
    archivo.close
    j=0
    while j==0:
        print("Menu")
        print("1. Actualizar Valor de los Planes")
        print("2. Mostrar datos de planes inferiores al valor de cuota ingresado")
        print("3. Mostrar monto a pagar para licitar vehiculo")
        print("4. Ingresar codigo de plan, actualizar cuotas para licitar")
        print("0. Cerrar")
        opcion = int(input())
        if opcion==0:
            exit()
        elif opcion==1:
            for i in range(len(planes)):
                print("Codigo {}\nModelo: {}\nVersion del vehiculo: {}\nValor actual del plan: {}".format(planes[i].getCodigo(), planes[i].getModelo(), planes[i].getVersion(), planes[i].getValor()))
                newVal = input("Ingrese nuevo valor del plan: ")
                planes[i].modificarImporte(newVal)
        elif opcion==2:
            indVal = input("Ingrese el valor: ")
            print(f"Vehiculos cuyo valor de cuotas es inferior a {indVal} pesos")
            l=0
            while l<=len(planes) and l!=5:
                if planes[l].getImporteCuota() < int(indVal):
                    print("Codigo {}\nModelo: {}\nVersion del vehiculo: {}".format(planes[l].getCodigo(), planes[l].getModelo(), planes[l].getVersion()))
                l+=1
        elif opcion==3:
            for i in range(len(planes)):
                print(f"El monto necesario a pagar para licitar el vehiculo {planes[i].getVersion()} es de {(planes[i].getCuotLicit() * planes[i].getImporteCuota()):.2f}")
        elif opcion==4:
            xCod = input("Ingrese codigo del plan a buscar: ")
            k = 0
            while k<=len(planes):
                if xCod==planes[k].getCodigo():
                    PlanAhorro.cantCuotlicit = input("Ingrese nueva cantidad de cuotas para licitar: ")
                    print(f"La nueva cantidad de cuotas para licitar del plan codigo: {planes[k].getCodigo()}, es {planes[k].getCuotLicit()}")
                else:
                    k+=1