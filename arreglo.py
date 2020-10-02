#2 
class Array3D:
    def __init__(self, depth, rows, cols):
        self.__depth=depth
        self.__cols=cols
        self.__rows=rows
        self.__arreglo=[[[0 for j in range(cols)] for i in range(rows)] for k in range(depth)]
            

    def get_num_depth(self):
        return self.__depth
    
    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols
    
    def set_item(self,depth,row,col,value):
        self.__arreglo[depth][row][col]=value

    def get_item(self,depth,rows,cols):
        return self.__arreglo[depth][rows][cols]
    def clearing(self,value):
        for i in range(self.__depth):    
            for j in range(self.__rows):
                for k in range (self.__cols):
                    self.__arreglo[i][j][k]= value
    def to_string(self):
        capa=0
        for layer in self.__arreglo:
            print(f"---- Capa { capa } -----")
            for ren in layer:
                print(ren)
            capa +=1
