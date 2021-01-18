class NodoArbol:
  def __init__(self,value,left=None,rigth=None):
    self.data=value
    self.left=left
    self.rigth=rigth
    self.ban=0

def recorrido(arb):
    mov=[]
    bandera=0
    lis1=[]#Nodos hoja
    lis2=[]#niveles
    
    while bandera==0:
        bandera2=0
        aux=arb
        for i in mov:
            if i=="L":
                aux=aux.left
            if i=="R":
                aux=aux.rigth
        if len(mov)==0 and arb.left.ban==1 and arb.rigth.ban==1:
            bandera=1
        if len(mov)==0 and arb.left==None and arb.rigth==None:
            bandera=1
        if aux.left!= None and aux.left.ban==0 and bandera2==0:
            aux=aux.left
            aux.ban=1
            mov.append("L")
            bandera2=1
        if aux.rigth!=None and aux.rigth.ban==0 and bandera2==0:
            aux=aux.rigth
            aux.ban=1
            mov.append("R")
            bandera2=1
        if aux.rigth==None and aux.left==None:
            lis1.append(aux.data)
            lis2.append(len(mov))
            mov.pop()
        if aux.left!=None and aux.rigth!=None and aux!=arb:
            if aux.left.ban==1 and aux.rigth.ban==1:
                mov.pop()
        if aux.rigth!=None:        
            if aux.left==None and aux.rigth.ban==1:
                mov.pop()
        if aux.left!=None:
            if aux.left.ban==1 and aux.rigth==None:
                mov.pop()
    for i in range(len(lis2)-1):
      for j in range(i):
        if lis2[j]>lis2[j+1]:
          aux=lis1[j]
          lis1[j]=lis1[j+1]
          lis1[j+1]=aux
          aux2=lis2[j]
          lis2[j]=lis2[j+1]
          lis2[j+1]=aux2
    print("----------------------------------------------------------------")
    for i in range(len(lis2)):
      if lis2[i]==lis2[len(lis2)-1]:
        print("Nodo",lis1[i],"en el nivel",lis2[i])
    print("----------------------------------------------------------------")  
print("***********ArboL Uno**********") 
arbol=NodoArbol("4",NodoArbol("2",NodoArbol("1"),NodoArbol("3")),NodoArbol("8",NodoArbol("9")))
recorrido(arbol)
print("**********Arbol dos **********")
arbol2=NodoArbol("A",NodoArbol("D",NodoArbol("L"),NodoArbol("K")),NodoArbol("M",NodoArbol("I"),NodoArbol("E")))
recorrido(arbol2)
print("**********Arbol Tres**********")
arbol3=NodoArbol("2",NodoArbol("7",NodoArbol("2"),NodoArbol("6",NodoArbol("5"),NodoArbol("11"))),NodoArbol("5",None,NodoArbol("9",NodoArbol("4"))))
recorrido(arbol3)
print("**********Arbol Cuatro**********")
arbol4=NodoArbol("55",NodoArbol("53",NodoArbol("48",NodoArbol(None,NodoArbol("51"))),NodoArbol("54")),NodoArbol("59",NodoArbol("56",NodoArbol(None,NodoArbol("57"))),NodoArbol("63",NodoArbol("61"),NodoArbol("70"))))
recorrido(arbol4)
        
            
        
