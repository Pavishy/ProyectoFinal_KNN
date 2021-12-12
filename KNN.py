def Mode(list):
    rep = 0
    mode = []
    for i in list:
        temp = list.count(i)
        if temp > rep:
            rep = temp
    for i in list:
        temp = list.count(i)
        if temp == rep and i not in mode:
            mode.append(i)
    if len(mode) != len(list):
        return mode
    else:
        return -1

archivo = open("Instancia_Entrenamiento.txt","r")
contenido = archivo.readlines()
lista = [linea.split("\t") for linea in contenido]
instancia = [[list(map(float,x[:4])), x[4]] for x in lista]
archivo = open("instancia_Prueba.txt","r")
contenido = archivo.readlines()
lista = [linea.split("\t") for linea in contenido]
for arr in lista:
    arr[4]= arr[4].replace("\n", "")
prueba = [[ list(map(float,x[:4])),x[4].replace("\n", "")] for x in lista]
K = 5
import metricas as m
contAciertos = 0
for registroNC in prueba:
    print("Clasificación del registro: ")
    print(registroNC)
    NC = registroNC[0]
    estructuraDatos = {}
    for contador, i in enumerate(instancia):
        distancia_NC_i = m.Manhatan(NC, i[0])
        distancia_NC_i = m.Euclidiana(NC, i[0])
        distancia_NC_i = m.Coseno(NC, i[0])
        estructuraDatos[contador] = distancia_NC_i
    ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1])
    temporalK = []
    for i in range(K):
        etiqueta = ordenado[i][0]
        registro = instancia[etiqueta]
        temporalK.append(registro[1].replace("\n",""))
    print("Clases de los vectores más cercanos a el registro NC:")
    print(temporalK)
    print("\n\n")
    moda = Mode(temporalK)
    respKnn = moda[0]
    print("Clase asignada por el KNN: "  + str(respKnn))
    print("Clase Real: " + registroNC[1])
    if str(respKnn) == registroNC[1]:
        contAciertos += 1
print("Total de aciertos: " + str(contAciertos))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(contAciertos/len(prueba)*100))

