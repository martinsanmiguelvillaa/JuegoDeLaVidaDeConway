def tablero_de_inicio (filas: int, columnas: int) -> list[list[int]]:
    tablero = []
    for fila in range(filas):
        tablero.append([])
        for columna in range(columnas):
            tablero[fila].append(0)
    return tablero

def ciclo_de_la_vida(tablero: list[list[int]]) -> list[list[int]]:
    copia_tablero: list[list[int]] =[]
    for fila in tablero:
        copia_tablero.append(fila.copy())

    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if celula_vive(tablero,[i,j], len(tablero), len(tablero[0])) == True:
                copia_tablero[i][j]=1
            else:
                copia_tablero[i][j]=0
    return copia_tablero


def posicion_valida(coordenadas: tuple[int, int], filas: int, columnas: int) -> bool:
   if coordenadas[0] >= filas or coordenadas[0] < 0 or coordenadas[1] >= columnas or coordenadas[1] < 0:
       return False
   else:
       return True
   
def celula_vive (tablero:list[list[int]], celula:tuple[int,int], filas: int, columnas: int) -> bool:
     res=0
     movimientos=[(-1,-1),(-1,0),(-1,1),
                  (0,-1),        (0,1),
                  (1,-1), (1,0), (1,1)]
     for movimiento in movimientos:
           nueva_posicion: tuple[int, int] = (celula[0] + movimiento[0], celula[1] + movimiento[1])
           if posicion_valida(nueva_posicion, filas, columnas) and tablero[nueva_posicion[0]][nueva_posicion[1]] == 1:
                res+=1
     if tablero[celula[0]][celula[1]] == 1:
          if res != 2 and res != 3:
              return False 
          else:
               return True
    
     else: 
         if res == 3:
             return True 
         else:
             return False