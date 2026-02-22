import os
import pandas as pd # type: ignore
import FreeNews as fn
import datetime

#Crearemos un archivo .csv para guardar la siguiente información:
#ruta + titular, enlace, portal de noticias, fecha de acción realizada.

class GuardarInformacion:
    
    

    def crear_dataframe(titular, enlace, portal):
        
        if not os.path.exists('informacion.csv'):
            with open('informacion.csv', 'w'):
                pass

        columnas = {
        'TITULAR' : titular,
        'ENLACE' : enlace,
        'PORTAL' : portal,
        'FECHA' : [datetime.datetime.now()]
        }

        datos = pd.DataFrame(columnas)

        
        if os.path.getsize('informacion.csv') == 0: 
            #getsize recupera la cantidad de bytes de un archivo
            #si es 0 significa que se encuentra vacío
            datos.to_csv('informacion.csv', index=False)
        else:
            datos.to_csv('informacion.csv', mode='a',index=False, header = False)
        

    def leer_dataframe():
        if not os.path.exists('informacion.csv'):
            return 'csv inexistente'
        if os.path.getsize('informacion.csv') == 0: 
            return 'csv vacío'
        datos = pd.read_csv('informacion.csv')
        return datos


