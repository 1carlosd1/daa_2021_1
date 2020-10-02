import xlrd
from arreglo import *
def main():
    a3=Array3D(34,33,14)
    for anio in range(2017,2018,1):
        ruta="./lluvia/"+str(anio)+"Precip.xls"
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,34,1):
            for c in range(0,14,1):
                a3.set_item(anio-2017,r-1,c,hoja.cell_value(r,c))
   
    a=int(imput("digite un año:"))
    e=int(imput("digite un estado:"))
    m=int(imput("digite un estado:"))
    print("En el año",a,"en el mes de",a3.get_item(a-2017,0,m),"en el estado",a3.get_item(a-2017,e,0),"promedio",a3.get_item(a-2017,e,m))
    print()

                    
main()
