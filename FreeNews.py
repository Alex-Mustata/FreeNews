import urllib.request
import json
import os
import GuardarInformacion # type: ignore
from  bs4 import BeautifulSoup # type: ignore

class UrlError(ValueError):
    pass

class LeerNoticias:
    
    portales_csv = []
    soup = ''
    noticia = ''
    url = ''

    def crear_carpeta():
        if not os.path.isdir('news'):
            os.mkdir('news')

    def desencriptar_noticia():

        LeerNoticias.crear_carpeta()
        LeerNoticias.url = input('Ingrese el enlace: ')
        req = urllib.request.Request(LeerNoticias.url)
        req.add_header('user-agent', 'Mozilla/5.0')

        with urllib.request.urlopen(req) as response:
            contenido = response.read() 
            LeerNoticias.noticia = contenido.decode('utf-8') 
                
        LeerNoticias.soup = BeautifulSoup(LeerNoticias.noticia, 'html.parser')

        texto = f'{LeerNoticias.soup.h1.text}.txt'
        
        #Elimina los carácteres que no pueden contener el nombre de un archivo
        CARACTERES_PROHIBIDOS = ['\n', '¿', '?', '<', '>', ':', '"', '\\', '/', '|', '*']
        for i in CARACTERES_PROHIBIDOS:
            if i in texto:
                texto = texto.replace(i, '')

        return 'news/'+texto #Devuelve ruta + titular


    def el_pais():
            try:

                noticia = LeerNoticias.desencriptar_noticia()

                if not 'elpais' in LeerNoticias.url:
                    raise UrlError
                else:
                    LeerNoticias.portales_csv.append('EL PAIS') 
                #Se consigue todos los scripts de ese tipo, ya que ahí se encuentra la noticia
                data = LeerNoticias.soup.find_all('script', type="application/ld+json")

                #iteramos en cada script hasta encontrar el indicado con la noticia
                for i in data:
                    jason = json.loads(i.text) #Como los scripts son tipo json, usamos json.loads para convertirlos en texto y leerlos
                    if isinstance(jason, dict) and "articleBody" in jason.keys(): #comprobamos si el json leido es dict y si contiene articleBody, la noticia, la escribimos
                        with open(noticia, 'a', encoding='utf-8') as f:
                            f.write(jason["articleBody"], )
            

            except UrlError:
                print('La URL no es de El Pais')
            except urllib.error.URLError:
                print('Internet no disponible')
            else:
                print('Operacion realizada con exito')
                GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            
    def diario_sur():
        try:
            
            noticia = LeerNoticias.desencriptar_noticia()

            if 'diariosur' not in LeerNoticias.url:
                raise UrlError
            else:
                    LeerNoticias.portales_csv.append('DIARIO SUR')

            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-p") 
            #busca los parrafos de la clase v-p, que contiene la noticia y algúna cosa inecesaria que eliminaremos después
            contador = 0


            with open(noticia, 'a', encoding='utf-8') as f:
                for i in parrafos:
                    if contador > 11:
                        f.write(f'{i.get_text()}\n')
                    contador += 1

        except UrlError:
            print('La URL no es del Diario Sur')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    def el_diario():
        try: 

            noticia = LeerNoticias.desencriptar_noticia()

            if 'eldiario' not in LeerNoticias.url:
                raise UrlError
            else:
                    LeerNoticias.portales_csv.append('EL DIARIO') 
            
            parrafos = LeerNoticias.soup.find_all("p", class_="article-text")

            with open(noticia, 'a', encoding='utf-8') as f:
                for i in parrafos:
                    x = i.get_text().lstrip()
                    f.write(x)

        except UrlError:
            print('La URL no es del El Diario')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    def abc():
        try:
            noticia = LeerNoticias.desencriptar_noticia()

            if 'abc' not in LeerNoticias.url:
                raise UrlError
            else:
                LeerNoticias.portales_csv.append('ABC') 

            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-d-p") 
            
            
            with open(noticia, 'a', encoding='utf-8') as f:
                for i in parrafos:
                    f.write(i.get_text())
        
        except UrlError:
            print('La URL no es del ABC')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

    
    def diario_vasco(): #Es el mismo código que diario sur
        try:
            
            noticia = LeerNoticias.desencriptar_noticia()

            if 'diariovasco' not in LeerNoticias.url:
                raise UrlError
            else:
                LeerNoticias.portales_csv.append('DIARIO VASCO') 

            parrafos = LeerNoticias.soup.find_all("p", class_ = "v-p") 
            #busca los parrafos de la clase v-p, que contiene la noticia y algúna cosa inecesaria que eliminaremos después
            contador = 0


            with open(noticia, 'a', encoding='utf-8') as f:
                for i in parrafos:
                    if contador > 11:
                        f.write(f'{i.get_text()}\n')
                    contador += 1

        except UrlError:
                print('La URL no es del Diario Sur')
        except ValueError:
            print('URL invalida')
        except urllib.error.URLError:
            print('Internet no disponible')
        else:
            GuardarInformacion.GuardarInformacion.crear_dataframe(noticia, LeerNoticias.url, LeerNoticias.portales_csv[-1])
            print('Operacion realizada con exito')

if __name__ == '__main__':
    objeto = LeerNoticias()
    while True:
        print('\nElija una opcion:\n' \
        '1.ElPais\n' \
        '2.DiarioSur\n' \
        '3.ElDiario\n' \
        '4.ABC\n' \
        '5.El Diario Vasco\n' \
        '6.Leer CSV\n' \
        '7.Salir\n')
        opcion = input()

        if opcion=='1':
            LeerNoticias.el_pais()
        elif opcion=='2':
            LeerNoticias.diario_sur()
        elif opcion=='3':
            LeerNoticias.el_diario()
        elif opcion=='4':
            LeerNoticias.abc()
        elif opcion=='5':
            LeerNoticias.diario_vasco()
        elif opcion=='6':
                leer_csv = GuardarInformacion.GuardarInformacion.leer_dataframe()
                print(leer_csv)
        elif opcion=='7':
            exit()
        else:
            print('Opcion invalida')
