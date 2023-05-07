class PlanAhorro:
    #Variables de Clase
    cantCuotPlan = 60
    cantCuotlicit = 10
    #Variables de Instancia
    __cod = 0
    __vModel = ""
    __vVers = ""
    __vValue = 0.0
    def __init__(self, cod, model, version, value):
        self.__cod = cod
        self.__vModel = model
        self.__vVers = version
        self.__vValue = value
    def getCodigo(self):
        return self.__cod
    def getModelo(self):
        return self.__vModel
    def getVersion(self):
        return self.__vVers
    def getValor(self):
        return self.__vValue
    def getImporteCuota(self):
        return ((self.__vValue/self.cantCuotPlan)+(self.__vValue*0.10))
    def modificarImporte(self, newVal): #newVal = importe nuevo
        self.__vValue = newVal
    def getCuotLicit(self):
        return self.cantCuotlicit

    #valor cuota = (importe vehículo/cantidad de cuotas) + importe vehículo * 0.10
