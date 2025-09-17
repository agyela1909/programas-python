#PROGRAMA22
#CarolAgyelaGonzalezOchoa

print("VENTA RESTAURANTE")
print("hamburguesas")
hamburguesa=int(input("CANTIDAD DE HAMBURGUESAS"))
costo_hamburguesas=35
multi=hamburguesa*costo_hamburguesas

print("refresco")
refresco=int(input("CANTIDAD DE REFRESCOS"))
costo_refresco=15
oper=refresco*costo_refresco

print("cerveza")
cerveza=int(input("CANTIDAD DE CERVEZAS"))
costo_cerveza=30
opera=cerveza*costo_cerveza

print("ensalada")
ensalada=int(input("CANTIDAD DE ENSALADAS"))
costo_ensalada=25
operaci=ensalada*costo_ensalada

print("postre")
postre=int(input("CANTIDAD DE POSTRES"))
costo_postre=28
calculo=postre*costo_postre

sumtotal=multi+oper+opera+operaci+calculo
print("VENTA DE HAMBURGUESAS ES:", multi)
print("VENTA DE REFRESCOS ES:", oper)
print("VENTA DE CERVEZAS ES:", opera)
print("VENTA DE ENSALADAS:", operaci)
print("VENTA DE POSTRES:", calculo)
print("EL TOTAL DE GANANCIAS ES:", sumtotal)