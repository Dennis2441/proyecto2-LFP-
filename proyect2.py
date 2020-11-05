import pandas as pd
import numpy as np
import webbrowser
import os

lista_tokens = []
listalista=[]
listamatriz=[]
listatabla=[]
defectonombre=""
defectocolor=""
class token:
    def __init__ (self, id, lexem, row, column,descripcion):
        self.id = id
        self.lexem = lexem
        self.row = row
        self.column = column
        self.descripcion=descripcion
class grafica:
    def __init__ (self, id, lexem):
        self.id = id
        self.lexem = lexem
class nombreslista:
    def __init__ (self, lexem):
        self.lexem = lexem
        

def analizar(cadena):
    estado = 0
    char = '' #caracter actual
    next_char = '' #caracter siguiente
    lexema = ""
    ff=1 #filas
    cc=0 #columnas
    n1=1
    
    for i in range(len(cadena)):
        char = cadena[i]
                
        try:
            next_char = cadena[i+1]
            
        except:
            next_char = " "
        #print(estado, ":", char,":", next_char)
        if(cc==0 and n1==1):
            cc=cc+1
            n1=n1+1
        else:
            cc=cc+1
        print(char)
        print(cc)
        if (estado==0):
            if (char.isalpha() and next_char.isalpha()):
                estado=1
                lexema=lexema+char
                print(lexema)
            elif (char.isdigit()):
                if (next_char.isdigit()):
                    estado=2
                    lexema=lexema+char
                else:
                    lexema=lexema+char
                    lista_tokens.append(token("numero",lexema,ff,cc,"número"))
                    lexema=""
            elif (char=="("):
                lexema=lexema+char
                lista_tokens.append(token("(",lexema,ff,cc,"Corchete Abierto"))
                lexema=""
            elif (char==")"):
                lexema=lexema+char
                lista_tokens.append(token(")",lexema,ff,cc,"Corchete Cerrado"))
                lexema=""
            elif (char=="{"):
                lexema=lexema+char
                lista_tokens.append(token("{",lexema,ff,cc,"LLave abierta"))
                lexema=""
            elif (char=="}"):
                lexema=lexema+char
                lista_tokens.append(token("}",lexema,ff,cc,"LLave cerrada"))
                lexema=""
            elif (char==";"):
                lexema=lexema+char
                lista_tokens.append(token(";",lexema,ff,cc,"Punto y Coma"))
                lexema=""
            elif (char=="#"):
                lexema=lexema+char
                lista_tokens.append(token("#",lexema,ff,cc,"Numeral"))
                lexema="" 
            elif (char==","):
                lexema=lexema+char
                lista_tokens.append(token(",",lexema,ff,cc,"coma"))
                lexema="" 
            elif (char=="/" and next_char=="/"):
                estado=11
                print(char)
            elif (char=="'"):
                estado=12
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 0
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            else:
                    estado=0
                    lista_tokens.append(token("error",char,ff,cc,"Caracter Desconocido :"+char+""))    
                    lexema=""      
        elif (estado==1):
            print(lexema)
            if(char.isalpha() and next_char.isalpha()):
                lexema=lexema+char
                print(lexema)
            elif (char.isalpha() and next_char.isdigit()):
                lexema=lexema+char
            elif (char.isdigit() and next_char.isalpha()):
                lexema=lexema+char
            elif (char.isdigit() and next_char.isdigit()):
                lexema=lexema+char
            else:     
                lexema=lexema+char
                print(lexema)
                if (lexema.casefold()=="lista"):
                    estado=0
                    lista_tokens.append(token("lista",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="matriz"):
                    estado=0
                    lista_tokens.append(token("matriz",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="tabla"):
                    estado=0
                    lista_tokens.append(token("tabla",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="fila"):
                    estado=0
                    lista_tokens.append(token("fila",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="defecto"):
                    estado=0
                    lista_tokens.append(token("defecto",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="falso"):
                    estado=0
                    lista_tokens.append(token("falso",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="verdadero"):
                    estado=0
                    lista_tokens.append(token("verdadero",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="nodo"):
                    estado=0
                    lista_tokens.append(token("nodo",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="encabezados"):
                    estado=0
                    lista_tokens.append(token("encabezados",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="nodos"):
                    estado=0
                    lista_tokens.append(token("nodos",lexema,ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="circulo" or lexema.casefold()=="rectangulo" or lexema.casefold()=="triangulo" or lexema.casefold()=="punto" or lexema.casefold()=="hexagono" or lexema.casefold()=="diamante"):
                    estado=0
                    lista_tokens.append(token("forma",lexema,ff,cc,"Palbra Reservada"))
                    lexema="" 
                elif (lexema.casefold()=="azul"):
                    estado=0
                    lista_tokens.append(token("color","blue2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="azul2"):
                    estado=0
                    lista_tokens.append(token("color","blue2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="azul3"):
                    estado=0
                    lista_tokens.append(token("color","blue3",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="rojo"):
                    estado=0
                    lista_tokens.append(token("color","red",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="rojo2"):
                    estado=0
                    lista_tokens.append(token("color","red2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="rojo3"):
                    estado=0
                    lista_tokens.append(token("color","red3",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="amarillo"):
                    estado=0
                    lista_tokens.append(token("color","yellow",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="amarillo2"):
                    estado=0
                    lista_tokens.append(token("color","yellow2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="amarillo3"):
                    estado=0
                    lista_tokens.append(token("color","yellow3",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="anaranjado"):
                    estado=0
                    lista_tokens.append(token("color","orange",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="anaranjado2"):
                    estado=0
                    lista_tokens.append(token("color","orange2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="anaranjado3"):
                    estado=0
                    lista_tokens.append(token("color","orange3",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="cafe"):
                    estado=0
                    lista_tokens.append(token("color","brown",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="cafe2"):
                    estado=0
                    lista_tokens.append(token("color","brown2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="cafe3"):
                    estado=0
                    lista_tokens.append(token("color","brown3",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="gris"):
                    estado=0
                    lista_tokens.append(token("color","grey",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="gris2"):
                    estado=0
                    lista_tokens.append(token("color","gray",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="gris3"):
                    estado=0
                    lista_tokens.append(token("color","gray54",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="morado"):
                    estado=0
                    lista_tokens.append(token("color","purple",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="morado2"):
                    estado=0
                    lista_tokens.append(token("color","purple2",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="morado3"):
                    estado=0
                    lista_tokens.append(token("color","purple",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="verde"):
                    estado=0
                    lista_tokens.append(token("color","palegreen",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="verde2"):
                    estado=0
                    lista_tokens.append(token("color","green1",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="verde3"):
                    estado=0
                    lista_tokens.append(token("color","green4",ff,cc,"Palbra Reservada"))
                    lexema=""
                elif (lexema.casefold()=="blanco"):
                    estado=0
                    lista_tokens.append(token("color","white",ff,cc,"Palbra Reservada"))
                    lexema=""                 
                else:
                    estado=0
                    lista_tokens.append(token("error",lexema,ff,cc,"Caracter Desconocido :"+lexema+""))    
                    lexema=""
                         
        elif (estado==11):
            if (cadena[i-1]=="/" and char=="/"):
                estado==11
            elif (char.isspace()):
                lexema=lexema+char
                if(char=='\n'):
                    estado=0
                    lista_tokens.append(token("Comentario",lexema,ff,cc,"Comentario"))
                    lexema=""
                    ff=ff+1
                    cc=0
            else:
                lexema=lexema+char
        elif (estado==12):
            print(lexema)
            if (char!="'"):
               lexema=lexema+char
            else:
                 estado=0
                 lista_tokens.append(token("nombre",lexema,ff,cc,"Nombre o Etiqueta"))
                 lexema=""
        elif (estado==2):
            if (char.isdigit()):
                lexema=lexema+char
            else:
                estado=0
                lista_tokens.append(token("numero",lexema,ff,cc,"número"))
                lexema=""
    for obj in lista_tokens:
        print(obj.lexem, obj.id)

def sintactico():
    estado = 0
    tipo=""
    global defectonombre
    global defectocolor
    for obj in lista_tokens: 
        print(obj.id, estado)   
        if (estado==0):
            tipo=""
            if (obj.id.casefold()=="lista"):
                listalista.append(grafica("lista",obj.lexem))
                estado=1
                tipo=obj.id
            if (obj.id.casefold()=="tabla"):
               # MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\matriz"+str(lis1)+".dot", 'w')
                
                mat1=mat1+1
                estado=1
                tipo=obj.id
            if (obj.id.casefold()=="matriz"):
                #MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\tabla"+str(lis1)+".dot", 'w')
                
                tab1=tab1+1
                estado=1
                tipo=obj.id
        elif (estado==1):
            if (obj.id.casefold()!="("):
                if (tipo.casefold()=="lista"):
                    lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+" despues de Lista"))
                    estado=0
                elif (tipo.casefold()=="tabla"):
                    lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+" despues de Tabla"))
                    estado=0
                elif (tipo.casefold()=="matriz"):
                    lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+" despues de matriz"))
                    estado=0   
            else:
                if (tipo.casefold()=="lista"):
                    estado=2
                elif (tipo.casefold()=="tabla"):
                    estado=3
                elif (tipo.casefold()=="matriz"):
                    estado=4
        elif (estado==2):
            if (obj.id.casefold()=="nombre"):
                if (tipo.casefold()=="lista"):
                    listalista.append(grafica("nombre",obj.lexem))  
                    estado=21
                elif (tipo.casefold()=="tabla"):
                    
                    estado=3
                elif (tipo.casefold()=="matriz"):
                    
                    estado=21
            else:
                pass
        elif (estado==21):
            if (obj.id.casefold()=="forma"):
                if (tipo.casefold()=="lista"):
                    listalista.append(grafica("forma",obj.lexem))
                    estado=22
                elif (tipo.casefold()=="matriz"):
                    
                    estado=22
                elif (obj.id.casefold()==","):
                   
                    estado=21
        elif (estado==22):
            if (obj.id.casefold()=="verdadero"):
                listalista.append(grafica("verdadero",obj.lexem))
                estado=22
            elif (tipo.casefold()=="falso"):
                listalista.append(grafica("falso",obj.lexem))
                estado=22
            elif (obj.id.casefold()==","):
                estado=22
            elif (obj.id.casefold()==")"):
                if (tipo.casefold()=="lista"):
                    estado=23
                elif (tipo.casefold()=="matriz"):
                    estado=4
        elif (estado==23):
            if (obj.id.casefold()=="nodo"):
                listalista.append(grafica("nodo",obj.lexem))
                estado=24
            elif (obj.id.casefold()=="nodos"):
                listalista.append(grafica("nodos",obj.lexem))
                estado=24
            elif (obj.id.casefold()=="defecto"):
                listalista.append(grafica("defecto",obj.lexem))
                estado=26
        elif (estado==24):
            if (obj.id.casefold()=="("):
                estado=24
            elif (obj.id.casefold()=="nombre"):
                listalista.append(grafica("nombre",obj.lexem))
                estado=24
            elif (obj.id.casefold()=="numero"):
                listalista.append(grafica("numero",obj.lexem))
                estado=24
            elif (obj.id.casefold()==")"):
                estado=25
            elif (obj.id=="#"):
                listalista.append(grafica("#",obj.lexem))
                estado=24
            elif (obj.id.casefold()==","):
                estado=24
            else:
                lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+""))
        elif (estado==25):
            if (obj.id.casefold()=="color"):
                listalista.append(grafica("color",obj.lexem))
                estado=25
            elif (obj.id.casefold()==";"):
                estado=23
            elif (obj.id=="#"):
                listalista.append(grafica("#",obj.lexem))
                estado=25
            else:
                lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+""))
        elif (estado==26):
            if (obj.id.casefold()=="("):
                estado=26
            elif (obj.id.casefold()=="nombre"):
                listalista.append(grafica("#",obj.lexem))
                defectonombre=obj.lexem
                estado=26
            elif (obj.id.casefold()==")"):
                estado=27
            else:
                lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+""))
        elif (estado==27):
            if (obj.id.casefold()=="color"):
                listalista.append(grafica("#",obj.lexem))
                defectocolor=obj.lexem
                estado=27
            elif (obj.id.casefold()==";"):
                listalista.append(grafica(";",obj.lexem))
                estado=0
            else:
                lista_tokens.append(token("error",obj.id,obj.row,obj.column,"No se esperaba: "+obj.id+""))
    
    no=1
    no2=1 
    cantidad=[]
    listale=[]
    listafil=[]
    listacol=[]
    listade=[]                          
    for obj in lista_tokens:
        print(obj.lexem,obj.id) 
        if (obj.id=="error"):
            print("")
        else:
            cantidad.append(no)
            no=no+1
            listale.append(obj.lexem)
            listafil.append(obj.row)
            listacol.append(obj.column)
            listade.append(obj.descripcion)
    jk={'Lexema': listale,'Fila': listafil,'Columna': listacol,'Descripcion': listade}
    df=pd.DataFrame(data=jk, index=cantidad)
    sk=str(df.to_html())
    f = open(r'C:\Users\denni\OneDrive\Desktop\Tokens.html','w')

    message = "<html> <head></head> <body>"+ sk +"</body> </html>"

    f.write(message)
    f.close()

    #webbrowser.open_new_tab(r'C:\Users\Dennis\OneDrive\Desktop\Tokens.html')
    cantidad=[]
    listale=[]
    listafil=[]
    listacol=[]
    listade=[]   
    for obj in lista_tokens:
        print(obj.lexem,obj.id) 
        if (obj.id=="error"):
            cantidad.append(no2)
            no2=no2+1
            listale.append(obj.lexem)
            listafil.append(obj.row)
            listacol.append(obj.column)
            listade.append(obj.descripcion)
    jk={'Lexema': listale,'Fila': listafil,'Columna': listacol,'Descripcion': listade}
    df=pd.DataFrame(data=jk,index=cantidad)
    sk=str(df.to_html())
    f = open(r'C:\Users\denni\OneDrive\Desktop\Error.html','w')

    message = "<html> <head></head> <body>"+ sk +"</body> </html>"

    f.write(message)
    f.close()

def graficarlista():
    print("===============================")
    estado=0
    lis1=1
    mat1=1
    tab1=1
    quotes = '"'
    nombre=""
    nombres=[]
    numero=1
    numero1=1
    anterior=""
    reversa=[]
    doble=""
    global defectonombre
    global defectocolor
    if listalista==[]:
        input("Error, no se ha cargado ningun archivo para graficar lista, vaya a la opcion 1 y cargue un archivo primero")
    else:
        for obj in listalista:
            print(obj.lexem,obj.id)
            if (estado==0):
                MapaRuta = open(r"C:\Users\denni\OneDrive\Desktop\lista"+str(lis1)+".dot", 'w')
                MapaRuta.write('digraph {' + "\n")
                MapaRuta.write('rankdir = LR;' + "\n")
                lis1=lis1+1
                estado=1
            elif (estado==1):
                if (obj.id.casefold()==";"):
                    if (doble.casefold()=="falso"):
                        MapaRuta.write('}')
                        MapaRuta.close()
                        os.system("dot -Tjpg "r"C:\Users\denni\OneDrive\Desktop\lista"+str(lis1)+".dot -o "r"C:\Users\denni\OneDrive\Desktop\lista"+str(lis1)+".jpg")
                        estado=0
                    elif (doble.casefold()=="verdadero"):
                        reversa.reverse()
                        for jk in reversa:
                            print()
                elif (obj.id.casefold()=="nombre"):
                    MapaRuta.write("label="+quotes+obj.lexem+quotes+";" + "\n")
                elif (obj.id.casefold()=="forma"):
                    if (obj.lexem.casefold()=="circulo"):
                        MapaRuta.write("node[shape =circle]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                    elif (obj.lexem.casefold()=="rectangulo"):
                        MapaRuta.write("node[shape =box]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                    elif (obj.lexem.casefold()=="triangulo"):
                        MapaRuta.write("node[shape =triangle]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                    elif (obj.lexem.casefold()=="punto"):
                        MapaRuta.write("node[shape =point]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                    elif (obj.lexem.casefold()=="hexagono"):
                        MapaRuta.write("node[shape =hexagon]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                    elif (obj.lexem.casefold()=="diamante"):
                        MapaRuta.write("node[shape =diamond]; fontsize=100; graph [bgcolor=skyblue];" + "\n")
                elif (obj.id.casefold()=="verdadero"):
                    print("")
                    doble=obj.lexem
                elif (obj.id.casefold()=="falso"):
                    print("")
                    doble=obj.lexem
                elif (obj.id.casefold()=="nodo"):
                    estado=2
                elif (obj.id.casefold()=="nodos"):
                    estado=3
            elif (estado==2):
                if (obj.id.casefold()=="nombre"):
                    if (anterior==""):
                        nombre=obj.lexem
                        reversa.append(nombreslista(nombre))
                    else:
                        nombre=obj.lexem
                        reversa.append(nombreslista(nombre))
                    estado=21
                elif (obj.id=="#"):
                    if (anterior==""):
                        nombre=defectonombre
                        reversa.append(nombreslista(nombre))
                    else:
                        nombre=defectonombre
                        reversa.append(nombreslista(nombre))
                    estado=21
                
            elif (estado==21):
                if (obj.id.casefold()=="color"):
                    if (anterior==""):
                        anterior=nombre
                        MapaRuta.write(nombre + "" + "[style=filled,fillcolor="+obj.lexem+ "]" + "\n")
                        nombre=""
                        estado=1
                    else:
                        MapaRuta.write(nombre + "" + "[style=filled,fillcolor="+obj.lexem+ "]" + "\n")
                        MapaRuta.write(anterior+"->"+nombre + "\n")
                        anterior=nombre
                        nombre=""
                        estado=1 
                elif (obj.id=="#"):
                    if (anterior==""):
                        anterior=nombre
                        MapaRuta.write(nombre + "" + "[style=filled,fillcolor="+defectocolor+ "]" + "\n")
                        nombre=""
                        estado=1
                    else:
                        MapaRuta.write(nombre + "" + "[style=filled,fillcolor="+defectocolor+ "]" + "\n")
                        MapaRuta.write(anterior+"->"+nombre + "\n")
                        anterior=nombre
                        nombre=""
                        estado=1     
            elif (estado==3):
                if (obj.id.casefold()=="numero"):
                    numero=int(obj.lexem)
                else:
                    while numero>=numero1:
                        print(obj.lexem)
                        nombres.append(nombreslista(obj.lexem+ str(numero1)))
                        reversa.append(nombreslista(obj.lexem+ str(numero1)))
                        numero1=numero1+1
                    estado=4
                    numero1=1
            elif (estado==4):
                if (obj.id.casefold()=="color"):
                    for i in nombres:
                        if (anterior==""):
                            print(i)
                            anterior=i.lexem 
                            MapaRuta.write(i.lexem + "" + "[style=filled,fillcolor="+obj.lexem+ "]" + "\n")
                        else:
                            MapaRuta.write(i.lexem  + "" + "[style=filled,fillcolor="+obj.lexem+ "]" + "\n")
                            nombre=i.lexem 
                            MapaRuta.write(anterior+"->"+nombre + "\n")
                            anterior=nombre
                            nombre=""
                    estado=1



                        
                                    
            
                
                
                
                
                    
                

            

    
def opcion1():
    print("_______________________________________")
    print("| 1) INTRODUCIR RUTA DE ARCHIVO       |")
    print("| 2) REGRESAR AL MENU                 |")
    print("_______________________________________")
    try:
        opcion = int(input("Opcion:"))
    except:
        main()
                
    if opcion == 1:
        ruta = input("Ingrese Ruta:")  
        archivo = open(ruta, "r",encoding='utf-8') #Leer        
        analizar(archivo.read())
        archivo.close()
        sintactico() 
    elif opcion == 2:
        main()
   
def main():    
    opcion = 0
    while(opcion != 4):
        print("  _______________________________________ ")
        print("|Dennis Alexnader Gamboa Stokes 201700747|")
        print("| _______________________________________|")
        print("|                                        |")
        print("| 1) CARGAR ARCHIVO                      |")
        print("| 2) GRAFICAR RUTA                       |")
        print("| 3) SALIR                               |")
        print("| >> ESCOGA OPCION                       |")
        print("| _______________________________________|")         
        try:
            opcion = int(input("Opcion:"))
        except:
            main()
        
        if opcion == 1: # CARGAR ARCHIVO
            opcion1()

        elif opcion == 2: # GRAFICAR ARCHIVO   <
            print("_______________________________________")   
            graficarlista()
            main()
        elif opcion == 3: # GRAFICAR ARCHIVO   <
            print("BYE")
            exit()           
        else:
            print("Valor erroneo")
    #analizador("CARGAR archivo1, archivo_2, archivo3")

if __name__ == "__main__":
    main()