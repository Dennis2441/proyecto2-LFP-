import pandas as pd
import numpy as np
import webbrowser
import os

lista_tokens = []
class token:
    def __init__ (self, id, lexem, row, column,descripcion):
        self.id = id
        self.lexem = lexem
        self.row = row
        self.column = column
        self.descripcion=descripcion

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
        print(lexema)
        print(cc)
        if(estado == 0): #ESTADO -------------------------------------------------------------- 0
            if (char == "<" and next_char.isalpha()):

                lista_tokens.append(token("<","<",ff,cc,"<"))
                estado = 1

                      
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 0
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            else:
                lexema=lexema+char
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                lexema=""
        elif (estado==1):
            if (char.isalpha() and next_char.isalpha()):  
                lexema=lexema+char
            elif (char.isalpha() and next_char.isalpha()==">"):
                lexema=lexema+char
                lista_tokens.append(token("error",next_char,ff,cc,"Desconocido"))                  
            else:
                if (char.isspace()):
                    print(lexema)
                    if (lexema.casefold()=="nombre"):
                        lista_tokens.append(token("nombre",lexema,ff,cc,"Palabra Reservada"))
                        if (next_char==">"):                        
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=2
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):                        
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=2
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag nombre de Mapa")
                            main()
                    elif(lexema.casefold()=="ruta"):
                        lista_tokens.append(token("ruta",lexema,ff,cc,"Palabra Reservada"))
                        if (next_char==">"):                        
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=3
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):                        
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=3
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag Ruta")
                            main()   
                    elif(lexema.casefold()=="estacion"):
                        
                        if (next_char==">"):      
                            lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                  
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=4
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):  
                                    lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                      
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=4
                                    lexema=""
                                else:
                                    estado=1
                        elif (next_char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(next_char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):      
                                    lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                  
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=4
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag estacion")
                            main() 
                    else:
                        estado=0
                else:                 
                    lexema=lexema+char
                    print(lexema)
                    if (lexema.casefold()=="nombre"):
                        lista_tokens.append(token("nombre",lexema,ff,cc,"Palabra Reservada"))
                        if (next_char==">"):                        
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=2
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):                        
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=2
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag nombre de Mapa")
                            main()
                    elif(lexema.casefold()=="ruta"):
                        lista_tokens.append(token("ruta",lexema,ff,cc,"Palabra Reservada"))
                        if (next_char==">"):                        
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=3
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):                        
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=3
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag Ruta")
                            main()   
                    elif(lexema.casefold()=="estacion"):
                        
                        if (next_char==">"):      
                            lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                  
                            lista_tokens.append(token(">",">",ff,cc,">"))
                            estado=4
                            lexema=""
                        elif (char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):  
                                    lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                      
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=4
                                    lexema=""
                                else:
                                    estado=1
                        elif (next_char.isspace()): # IGNORAR LOC ESPACIOS
                            estado = 1
                            if(next_char=='\n'):
                                ff=ff+1
                                cc=0
                                if (next_char==">"):      
                                    lista_tokens.append(token("estacion",lexema,ff,cc,"Palabra Reservada"))                  
                                    lista_tokens.append(token(">",">",ff,cc,">"))
                                    estado=4
                                    lexema=""
                                else:
                                    estado=1
                        else:
                            lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                            print("No se puede Completar hay un error en tag estacion")
                            main() 
                    else:
                        estado=0
        elif(estado==2):
            if(char=="<" and next_char=="/"):
                if(cadena[i+8]==">"):
                    lista_tokens.append(token("NombreMapa",lexema,ff,cc,"NombreMapa"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("nombre","nombre",ff,cc,"Palabra Reservada"))                    
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""
                    
                else:
                    print("Tag Nombre del mapa no cerrada")
                    main()
            elif (char==">"):
                if (lexema.casefold()=="nombre"):
                    print("aqui")
                    estado=0
                    lexema=""
                else:
                    estado=2
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 2
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            elif (char=="/"):
                print("")        
            else:
                lexema=lexema+char
        elif(estado==3):
            print(char)
            
            
            if (char == "<" and next_char.isalpha()):
                lista_tokens.append(token("<","<",ff,cc,"<"))
                estado=31
            elif (char.isalpha()):
                print(lexema)
            elif (char==">"):
                if (lexema.casefold()=="ruta"):
                    print("aqui")
                    estado=0
                    lexema=""
                else:
                    estado=3
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 3
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            elif (char=="/"):
                print("")
            elif(char=="<" and next_char=="/"):
                if (cadena[i+2].casefold()=="r" and cadena[i+3].casefold()=="u" and cadena[i+4].casefold()=="t" and cadena[i+5].casefold()=="a" and cadena[i+6].casefold()==">"):
                   lexema="ruta"
                   lista_tokens.append(token("<","<",ff,cc,"<"))
                   lista_tokens.append(token("/","/",ff,cc,"/"))
                   lista_tokens.append(token("rutac",lexema,ff,cc,"Palabra Reservada"))
                   lista_tokens.append(token(">",">",ff,cc,">"))
                elif (char.isspace()): # IGNORAR LOC ESPACIOS
                    estado = 3
                    if(char=='\n'):
                        ff=ff+1
                        cc=0
                else:
                    print("Tag ruta no esta cerrada completamente")
                    estado=0 
            elif (char.casefold()=="r" and next_char.casefold()=="u" and cadena[i+2].casefold()=="t" and cadena[i+3].casefold()=="a" and cadena[i+4].casefold()==">"):
                   lexema="ruta"
                   lista_tokens.append(token("<","<",ff,cc,"<"))
                   lista_tokens.append(token("/","/",ff,cc,"/"))
                   lista_tokens.append(token("rutaC",lexema,ff,cc,"Palabra Reservada"))
                   lista_tokens.append(token(">",">",ff,cc,">"))                
            else:
                lexema=lexema+char
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                lexema=""
                
        elif(estado==31):
            print(char)
            if (char.isalpha() and next_char.isalpha()):  
                lexema=lexema+char                  
            else:
                lexema=lexema+char
                print(lexema)
                if (lexema.casefold()=="nombre"):
                    lista_tokens.append(token("nombre",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=32
                        lexema=""
                    elif (char.isspace()): # IGNORAR LOC ESPACIOS
                        estado = 1
                        if(char=='\n'):
                            ff=ff+1
                            cc=0
                            if (next_char==">"):                        
                                lista_tokens.append(token(">",">",ff,cc,">"))
                                estado=32
                                lexema=""
                            else:
                                estado=1
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag NombreRUta")
                        main() 
                elif(lexema.casefold()=="peso"):
                    lista_tokens.append(token("peso",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=33
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag peso")
                        main() 
                elif(lexema.casefold()=="inicio"):
                    lista_tokens.append(token("inicio",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=34
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag inicio")
                        main() 
                        estado=34
                    lexema=""
                elif(lexema.casefold()=="fin"):
                    lista_tokens.append(token("fin",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=35
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag fin")
                        main() 
                        estado=34
                    lexema=""
                else:
                    lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                    estado=3
        elif(estado==32):
            if(char.isalpha() or char=="@" or char=="#" or char=="_" or char.isdigit()):
               lexema=lexema+char
                
            elif(char=="<" and next_char=="/"):
                if(cadena[i+8]==">"):
                    lista_tokens.append(token("nombreruta",lexema,ff,cc,"NombreRuta"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("nombre","nombre",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    print("Tag Nombre de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 32
                if(char=='\n'):
                    ff=ff+1
                    cc=0   
            elif (char==">"):
                if (lexema.casefold()=="nombre"):
                    estado=3
                    lexema=""
                else:
                    estado=32
                
            else:
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
        elif (estado==33):
            print(char)
            print(lexema)
            if (char.isdigit() or char=="."):
                lexema=lexema+char
            elif (char.isalpha()):
                lexema=lexema+char
            elif(char=="<" and next_char=="/"):
                if(cadena[i+6]==">"):
                    lista_tokens.append(token("peso",lexema,ff,cc,"Peso"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("<","/",ff,cc,"/"))
                    lista_tokens.append(token("pesoc","peso",ff,cc,"Palabra Reservada"))
                   
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""   
                  
                else:
                    print("Tag peso de la ruta no cerrada o hay algun problema con el tag")
            elif(char=="/"):
                print("")
            elif (char==">"):
                if (lexema=="peso"):
                    estado=3
                    lexema=""
                else:
                    estado=33
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 33
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            else:
                lexema=lexema+char
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                lexema=""
        elif (estado==34):
            if (char=="<" and next_char=="/"):
                if(cadena[i+8]==">"):
                    lista_tokens.append(token("nombreestacion",lexema,ff,cc,"NombreEstacion"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("<","/",ff,cc,"/"))
                    lista_tokens.append(token("inicioc","inicio",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    print("Tag inicio de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 34
                if(char=='\n'):
                    ff=ff+1
                    cc=0   
            elif (char==">"):
                if (lexema.casefold()=="inicio"):
                    estado=3
                    lexema=""
                elif(next_char.isspace()==False):
                    estado=345
                else:
                    estado=34                    
            else:
                lexema=lexema+char
        elif (estado==345):
             lexema=lexema+char
             lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
             lexema=""
             estado=34
        elif (estado==354):
             lexema=lexema+char
             lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
             lexema=""
             estado=35
        elif (estado==35):
            if (char=="<" and next_char=="/"):
                if(cadena[i+5]==">"):
                    lista_tokens.append(token("nombreestacion",lexema,ff,cc,"NombreEstacion"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("finc","fin",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    print("Tag inicio de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 35
                if(char=='\n'):
                    ff=ff+1
                    cc=0      
            elif (char==">"):
                if (lexema.casefold()=="fin"):
                    estado=3
                    lexema=""
                elif(next_char.isspace()==False):
                    estado=354
                else:
                    estado=35                 
            else:
                lexema=lexema+char
                
        elif (estado==4):
            print(char)
            
            
            if (char == "<" and next_char.isalpha()):
                lista_tokens.append(token("<","<",ff,cc,"<"))
                estado=41
            elif (char.isalpha()):
                print(lexema)
            elif (char==">"):
                if (lexema.casefold()=="estacion"):
                    print("aquix2")
                    estado=0
                    lexema=""
                else:
                    estado=4
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 4
                if(char=='\n'):
                    ff=ff+1
                    cc=0
            elif (char=="/"):
                print("")
            elif(char=="<" and next_char=="/"):
                if (cadena[i+2].casefold()=="e" and cadena[i+3].casefold()=="s" and cadena[i+4].casefold()=="t" and cadena[i+5].casefold()=="a" and cadena[i+6].casefold()=="c" and cadena[i+7].casefold()=="i" and cadena[i+8].casefold()=="o" and cadena[i+9].casefold()=="n" and cadena[i+10].casefold()==">"):
                   lexema="estacion"
                   lista_tokens.append(token("<","<",ff,cc,"<"))
                   lista_tokens.append(token("/","/",ff,cc,"/"))
                   lista_tokens.append(token("estacionc",lexema,ff,cc,"Palabra Reservada"))
                   lista_tokens.append(token(">",">",ff,cc,">"))
                elif (cadena[i+2].isspace()): # IGNORAR LOC ESPACIOS
                    estado = 4
                    if(char=='\n'):
                        ff=ff+1
                        cc=0
                else:
                    print("Tag Estacion no esta cerrada completamente") 
                    estado=0   
            elif (char.casefold()=="e" and next_char.casefold()=="s" and cadena[i+2].casefold()=="t" and cadena[i+3].casefold()=="a" and cadena[i+4].casefold()=="c" and cadena[i+5].casefold()=="i" and cadena[i+6].casefold()=="o" and cadena[i+7].casefold()=="n" and cadena[i+8].casefold()==">"):
                   lexema="estacion"
                   lista_tokens.append(token("<","<",ff,cc,"<"))
                   lista_tokens.append(token("/","/",ff,cc,"/"))
                   lista_tokens.append(token("estacionc",lexema,ff,cc,"Palabra Reservada"))
                   lista_tokens.append(token(">",">",ff,cc,">"))            
            else:
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                
        elif (estado==41):
            print(char)
            if (char.isalpha() and next_char.isalpha()):  
                lexema=lexema+char                  
            else:
                lexema=lexema+char
                print(lexema)
                if (lexema.casefold()=="nombre"):
                    lista_tokens.append(token("nombre",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=42
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag NombreRUta")
                        main() 
                elif(lexema.casefold()=="color"):
                    lista_tokens.append(token("color",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=43
                        lexema=""
                elif(lexema.casefold()=="estado"):
                    lista_tokens.append(token("estado",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=44
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag color")
                        main() 
                elif(lexema.casefold()=="estado"):
                    lista_tokens.append(token("estado",lexema,ff,cc,"Palabra Reservada"))
                    if (next_char==">"):                        
                        lista_tokens.append(token(">",">",ff,cc,">"))
                        estado=43
                        lexema=""
                    else:
                        lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                        print("No se puede Completar hay un error en tag estado")
                        main() 
                else:
                    lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))
                    estado=0
        elif (estado==42):
            if(char=="<" and next_char=="/"):
                if(cadena[i+8]==">"):
                    lista_tokens.append(token("nombrestacion",lexema,ff,cc,"NombreEstacion"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("nombre","nombre",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    
                    print("Tag Nombre de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 42
                if(char=='\n'):
                    ff=ff+1
                    cc=0   
            elif (char==">"):
                if (lexema.casefold()=="nombre"):
                    estado=4
                    lexema=""
                else:
                    estado=42
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 42
                if(char=='\n'):
                    ff=ff+1
                    cc=0
                    
            else:
                lexema=lexema+char
        elif (estado==43):
            print(char)
            if (char=="#"):
                lexema=lexema+char
            elif (char.isalpha()):
                lexema=lexema+char
                print(lexema)
            elif(char.isdigit()):
                lexema=lexema+char
                print("AQUI",cadena[i+7])
            elif (char=="<" and next_char=="/"):
                print(lexema)
                if(cadena[i+7]==">"):
                    lista_tokens.append(token("color#",lexema,ff,cc,"color#"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("color","color",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    print("Tag Nombre de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 43
                if(char=='\n'):
                    ff=ff+1
                    cc=0   
            elif (char==">"):
                if (lexema.casefold()=="color"):
                    estado=4
                    lexema=""
                else:
                    estado=43
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 43
                if(char=='\n'):
                    ff=ff+1
                    cc=0
        elif(estado==44):
            if(char=="<" and next_char=="/"):
                if(cadena[i+8]==">"):
                    lista_tokens.append(token("estados",lexema,ff,cc,"Estado"))
                    lista_tokens.append(token("<","<",ff,cc,"<"))
                    lista_tokens.append(token("/","/",ff,cc,"/"))
                    lista_tokens.append(token("estado","estado",ff,cc,"Palabra Reservada"))       
                    lista_tokens.append(token(">",">",ff,cc,">"))
                    lexema=""         
                else:
                    print("Tag Nombre de la ruta no cerrada")
            elif(char=="/"):
                print("")
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 44
                if(char=='\n'):
                    ff=ff+1
                    cc=0   
            elif (char==">"):
                if (lexema.casefold()=="estado"):
                    estado=4
                    lexema=""
                else:
                    estado=44
            elif (char.isspace()): # IGNORAR LOC ESPACIOS
                estado = 44
                if(char=='\n'):
                    ff=ff+1
                    cc=0
                    
            elif (char.isalpha()):
                lexema=lexema+char 
            else:
                lista_tokens.append(token("error",lexema,ff,cc,"Desconocido"))       
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

    #webbrowser.open_new_tab(r'C:\Users\Dennis\OneDrive\Desktop\Error.html')      

    
    

def main():    
    opcion = 0
    while(opcion != 4):
        print("  _______________________________________ ")
        print("|Dennis Alexnader Gamboa Stokes 201700747|")
        print("| _______________________________________|")
        print("|                                        |")
        print("| 1) CARGAR ARCHIVO                      |")
        print("| 2) GRAFICAR RUTA                       |")
        print("| 3) GRAFICAR MAPA                       |")
        print("| 4) SALIR                               |")
        print("| >> ESCOGA OPCION                       |")
        print("| _______________________________________|")         
        opcion = int(input("Ingrese opción: "))
        if opcion == 1: # CARGAR ARCHIVO
            print("_______________________________________")
            print("| 1) INTRODUCIR RUTA DE ARCHIVO       |")
            print("_______________________________________")
            ruta = input("Ruta de Archivo: ")    
            archivo = open(ruta, "r",encoding='utf-8') #Leer        
            analizar(archivo.read())
            archivo.close()
        elif opcion == 2: # GRAFICAR ARCHIVO   <
            print("_______________________________________")
            print("| 1) PRIMERA ESTACION                 |")
            print("|                                     |")
            print("_______________________________________")
            ruta = input("Primera Estacion: ")

            print("_______________________________________")
            print("| 1) ULTIMA  ESTACION                 |")
            print("|                                     |")
            print("_______________________________________")
            rutas = input("Estacion Final: ")  
            
        elif opcion == 3: # GRAFICAR ARCHIVO   <
            contador=1
            ar=open(r'C:\Users\Dennis\OneDrive\Desktop\Map.dot','w')
            ar.write('Diagraph {')
            for obj in lista_tokens:
                if (obj.id.casefold()=='nombrestacion'):
                    ar.write(obj.lexem+" "+ "[lable="+obj.lexem+"]")
                    contador=contador+1
            for obj in lista_tokens:
                if (obj.id.casefold()=='ruta'):
                    print("j")    
            ar.write('}')
            ar.close()
            os.system("dot -Tpng \""+os.getcwd()+"\\Map.dot\" -o \""+os.getcwd()+"\\Map.png\"")
            os.system("explorer \""+os.getcwd()+"\\Map.png\"")
           
        elif opcion == 4: #SALIR
            print("BYE")
            exit()
        else:
            print("Valor erroneo")
    #analizador("CARGAR archivo1, archivo_2, archivo3")

if __name__ == "__main__":
    main()