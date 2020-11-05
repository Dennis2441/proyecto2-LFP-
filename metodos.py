import re
import math
import os

def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)


def posfija(cande):
    archivo = open('Ejemplo1.dot','w')
    archivo.write('digraph structs {\n')
    archivo.write('node [shape=record];\n')
    archivo.write('label="'+cande+'";')
    pila=[]
    m1=0
    m2=0
    numero=0
    nun=1
    simbolo1=""
    aux=[]
    con=""
    cande = cande.replace("[", "(").replace("]", ")")
    cande = cande.replace("+", "pos(+)")
    cande = cande.replace("-", "pos(-)")
    cande = cande.replace("*", "pos(*)")
    cande = cande.replace("/", "pos(/)")
    nexo = re.findall('\-\d*\.?\d+|\S+\+\d*\.?\d+|\d*\.?\d+|\w+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]',cande)
    inst = ""
    


    for i in nexo:
    
        if "fact" in i:
            m1=m1+1

        elif "sqrt" in i:
            m1=m1+1
            
        
        elif "pow" in i:
            m1=m1+1

        elif "pos(+)" in i:
            m2=m2+1

        elif "pos(/)" in i:
            m2=m2+1
            
        elif "pos(*)" in i:
            m2=m2+1

        elif "pos(-)" in i:
            m2=m2+1
            
        else:
            m1=m1+1
        

        archivo.write('sQ'+'[shape=record,label="{') 
        for i in range(m1-1):
                           
            archivo.write(""+'|')     
        archivo.write('}"];')




    for i in nexo:
    
        if "fact" in i:
            c1 = re.findall('[\d]',i)
            n =facto(int(c1[0]))
            pila.append(n)
            numero=numero+1
            aux.append(i)
            

        elif "sqrt" in i:
            c1 = re.findall('[\d]',i)
            n=math.sqrt(int(c1[0]))
            pila.append(n)
            numero=numero+1
            aux.append(i)
            
            
        
        elif "pow" in i:
            xx= re.findall('[\d]',i)
            n2 =pow(float(xx[0]),float(xx[1]))
            pila.append(n2)
            aux.append(i)
            numero=numero+1
            con+=i
            
            
    
        elif "pos(+)" in i:
            
            simbolo1="+"
            numero=numero+1
            

        elif "pos(*)" in i:
            simbolo1="*"
            numero=numero+1
            
            

        elif "pos(/)" in i:
            simbolo1="/"
            numero=numero+1
            
            

        elif "pos(-)" in i:
            simbolo1="-"
            numero=numero+1
            
            
        
        else:

            inst = i
            pila.append(inst)
            aux.append(inst)
            con+=i
            
            numero=numero+1

            inst=""
        

        
        if simbolo1=="+"or simbolo1=="-"or simbolo1=="*"or simbolo1=="/":
                    a2= float(pila.pop())
                    a1= float(pila.pop())
                    archivo.write('s'+str(nun)+'[shape=record,label="{') 
                    
                    for i in range(m1-len(aux)):
                        
                        archivo.write(""+'|')
                    
                    for i in range(len(aux)):
                        a=aux.pop()
                        archivo.write(str(a)+'|')
                   
                   
                    archivo.write('}"];')
                   
                    for i in range(len(aux)):
                        aux.pop()

                    con=""
                    nun=nun+1
                    if simbolo1=="+":
                        w=a1+a2
                        pila.append(w)
                        aux.append(w)
                        con+=str(w)
                        archivo.write('s'+str(nun)+'[shape=record,label="{') 
                        for i in range(m1-len(aux)):
                        
                            archivo.write(""+'|')

                        for i in range(len(aux)):
                            a=aux.pop()
                            archivo.write(str(a)+'|')
                        archivo.write('}"];')
                        aux.append(a)
                        nun=nun+1
                        
                        
                    
                    if simbolo1=="-":
                        w=a1-a2
                        pila.append(w)
                        aux.append(w)
                        con+=str(w)
                        archivo.write('s'+str(nun)+'[shape=record,label="{') 
                        for i in range(m1-len(aux)):
                           
                            archivo.write(""+'|')
                        
                        for i in range(len(aux)):
                            a=aux.pop()
                            archivo.write(str(a)+'|')
                        archivo.write('}"];')
                        aux.append(a)
                        nun=nun+1

                    if simbolo1=="*":
                        w=a1*a2
                        pila.append(w)
                        aux.append(w)
                        con+=str(w)
                        archivo.write('s'+str(nun)+'[shape=record,label="{') 
                        for i in range(m1-len(aux)):
                            
                            archivo.write(""+'|')
                       
                        for i in range(len(aux)):
                            a=aux.pop()
                            archivo.write(str(a)+'|')
                        archivo.write('}"];')
                        aux.append(a)
                        nun=nun+1

                    if simbolo1=="/":
                        w=a1/a2
                        pila.append(w)
                        aux.append(w)
                        con+=str(w)
                        archivo.write('s'+str(nun)+'[shape=record,label="{') 
                        for i in range(m1-len(aux)):
                            
                            archivo.write(""+'|')

                        for i in range(len(aux)):
                            a=aux.pop()
                            archivo.write(str(a)+'|')
                        archivo.write('}"];')
                        aux.append(a)
                        nun=nun+1
                    
                    
                    
                    numero=0
                    simbolo1=""
                
        
        
    print(pila)
    for i in range(len(pila)):
            pila.pop()



    archivo.write('}')
    archivo.close()
    os.system('dot -Tpdf grafica.dot -o gra.pdf')
    



def infija(entrada):
    entrada = entrada.replace("in:", "")
    entrada = entrada.replace(" ", "")
    entrada = entrada.replace("[", "(").replace("]", ")")
    nexo = re.findall( "\(|\)|\-\d*\.?\d+|\+\d*\.?\d+|\d*\.?\d+|\w+[(][^)]+[)]|\+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]|\-\d*\.?\d*|\*\d*\.?\d*|\d*\.?\d*|\w+[(][^)]*[)]|\*\w*[(][^)]*[)]|\*\w*[(][^)]*[)]|\/\d*\.?\d*|\/\d*\.?\d/|\d*\.?\d/|\w/[(][^)]*[)]|\*\w*[(][^)]*[)]|\*\w*[(][^)]*[)]",entrada)
    resltado = ""
    for i in nexo:
        if "fact" in i:
            analizador = re.findall("\d*\.?\d",i)
            rfa =facto(int(analizador[0]))
            if i[0:1] == "+" or i[0:1] == "-" or i[0:1] == "*" or i[0:1] == "/":
                resltado = resltado + i[0:1] + str(rfa)
            else:
                resltado = resltado + str(rfa)

        elif "sqrt" in i:
            analizador = re.findall("\d*\.?\d",i)
            raiz =math.sqrt(int(analizador[0]))
            if i[0:1] == "+" or i[0:1] == "-" or i[0:1] == "*" or i[0:1] == "/":
                resltado = resltado + i[0:1] + str(raiz)
            else:
                resltado = resltado + str(raiz)
        
        elif "pow" in i:
            analizador = re.findall("\d*\.?\d",i)
            rpow =pow(float(analizador[0]),float(analizador[1]))
            if i[0:1] == "+" or i[0:1] == "-" or i[0:1] == "*" or i[0:1] == "/":
                resltado = resltado + i[0:1] + str(rpow)
            else:
                resltado = resltado + str(rpow)
        else:
            resltado = resltado + i
    print(eval(resltado))


def notacion_posfija(cande):
    pilaaa=[]
    
    simbolo=""
    cande = cande.replace("post:", "")
    cande = cande.replace("[", "(").replace("]", ")")
    cande = cande.replace("+", "pos(+)")
    cande = cande.replace("-", "pos(-)")
    cande = cande.replace("*", "pos(*)")
    cande = cande.replace("/", "pos(/)")
    nexo = re.findall('\-\d*\.?\d+|\S+\+\d*\.?\d+|\d*\.?\d+|\w+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]',cande)
    inst = ""
    for i in nexo:

        if "fact" in i:
            c1 = re.findall('[\d]',i)
            n =facto(int(c1[0]))
            pilaaa.append(n)
            

        elif "sqrt" in i:
            c1 = re.findall('[\d]',i)
            n=math.sqrt(int(c1[0]))
            pilaaa.append(n)
            
            
        
        elif "pow" in i:
            c = re.findall('\d+|\-\d+|\+\d+',i)
            n1 =pow(float(c[0]),float(c[1]))
            pilaaa.append(n1)
            
        elif "pos(+)" in i:
            
            simbolo="+"

        elif "pos(*)" in i:
            simbolo="*"
            
        elif "pos(/)" in i:
            simbolo="/"
            
        elif "pos(-)" in i:
            simbolo="-"
            
        else:

            inst = i
            pilaaa.append(inst)
            inst=""
    
        if simbolo=="+"or simbolo=="-"or simbolo=="*"or simbolo=="/":
            can2= float(pilaaa.pop())
            can1= float(pilaaa.pop())
            if simbolo=="+":
                res=can1+can2
                pilaaa.append(res)
                
            if simbolo=="-":
                res=can1-can2
                pilaaa.append(res)

            if simbolo=="*":
                res=can1*can2
                pilaaa.append(res)

            if simbolo=="/":
                res=can1/can2
                pilaaa.append(res)
            
            simbolo=""
            
        
    print(pilaaa)
    for i in range(len(pilaaa)):
            pilaaa.pop()


def notacion_prefija(cande):
    pila1=[]
    simbolo2=""
    cande = cande.replace("pre:", "")
    cande = cande.replace("[", "(").replace("]", ")")
    cande = cande.replace("+", "pos(+)")
    cande = cande.replace("-", "pos(-)")
    cande = cande.replace("*", "pos(*)")
    cande = cande.replace("/", "pos(/)")
    cadena1 = re.findall('\-\d*\.?\d+|\S+\+\d*\.?\d+|\d*\.?\d+|\w+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]',cande)
    inst = ""
    for i in cadena1[::-1]:
    
        if "fact" in i:
            c1 = re.findall('[\d]',i)
            n =facto(int(c1[0]))
            pila1.append(str(n))
            
        elif "sqrt" in i:
            c1 = re.findall('[\d]',i)
            n=math.sqrt(float(c1[0]))
            pila1.append(str(n))
            
        elif "pow" in i:
            c = re.findall('\d+|\-\d+|\+\d+',i)
            n1 =pow(float(c[0]),float(c[1]))
            pila1.append(str(n1))
            
        elif "pos(+)" in i:
            simbolo2="+"

        elif "pos(*)" in i:
            
            simbolo2="*"
        elif "pos(/)" in i:
            simbolo2="/"

        elif "pos(-)" in i:
            simbolo2="-"
        
        else:

            inst = i
            pila1.append(inst)
            inst=""
        
        if simbolo2=="+"or simbolo2=="-"or simbolo2=="*"or simbolo2=="/":
            a1= float(pila1.pop())
            a2= float(pila1.pop())
            if simbolo2=="+":
                w=a1+a2
                pila1.append(w)
                
            if simbolo2=="-":
                w=a1-a2
                pila1.append(w)

            if simbolo2=="*":
                w=a1*a2
                pila1.append(w)

            if simbolo2=="/":
                w=a1/a2
                pila1.append(w)
            simbolo2=""
                    
    print(pila1)
    for i in range(len(pila1)):
            pila1.pop()
    
def grafica():
    simbolo=""
    pilar=[]
    pilax=[]
    print("INGRESE OPERACION A GRAFICAR")
    h = input()
    h1= h.lower()
    h1= h1.replace("(", "").replace(")", "")
    h1= h1.replace(", ", ",").replace(" ,", ",")
    h1= h1.replace("[ ", "[").replace(" ]", "]")
    h1=h1.split(sep=' ')
    z=""
    for i in h1:
        if i=="+" or i=="-"or i=="*" or i=="/":
            pilax.append(i)
            simbolo=i
            z="f"


        else:
            pilar.append(i)
            z="v"
        
            
        
        if simbolo=="/" or simbolo=="*":
            if z=="v":
                s=pilax.pop()
                pilar.append(s)
                simbolo=""
        
        

            
    for i in range(len(pilax)):
        s=pilax.pop()
        pilar.append(s)


    
    
    
    p=""
    for i in range(len(pilar)):
        p=pilar.pop()+" "+p

    posfija(p)
    
    



