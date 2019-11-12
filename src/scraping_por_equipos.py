import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

def resultado(local,visitante,df_final):
    df_consulta = df_final[df_final["Local"]==local]
    df_consulta = df_consulta[df_final["Visitor"]==visitante]
    res = requests.get(list(df_consulta["Links"])[0])
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    golesPaginaB = soup.select('.scorebox > div:nth-child(5)')
    listaGoalCard=[]
    for e in golesPaginaB:
        e1 = e.text
        e1 = (e1.strip().split('\n'))
        e2 = e.select('.event_icon')
        for e in e2:
            e = str(e)
            listaGoalCard.append(e)
    visitorEvents=list(zip(listaGoalCard,e1))
    listGolesVisitante=[]
    for e in visitorEvents:
        for i in e:
            if re.search("goal",i):
                a=''.join(e[1])
                a = a.split('·')
                b = 'en el minuto'.join(a)
                listGolesVisitante.append(re.sub('&rsquor',"'",b))
    golesPaginaA = soup.select('.scorebox > div:nth-child(4)')
    listaGoalCard=[]
    for e in golesPaginaA:
        e1 = e.text
        e1 = (e1.strip().split('\n'))
        e2 = e.select('.event_icon')
        for e in e2:
            e = str(e)
            listaGoalCard.append(e)
    localEvents=list(zip(listaGoalCard,e1))
    listGolesLocal=[]
    for e in localEvents:
        for i in e:
            if re.search("goal",i):
                a=''.join(e[1])
                a = a.split('·')
                b = 'en el minuto'.join(a)
                listGolesLocal.append(re.sub('&rsquor',"'",b))
    header = "Resultado: "+local+" "+str(len(listGolesLocal))+"-"+str(len(listGolesVisitante))+" "+visitante
    goles_local = pintaGoles(local,listGolesLocal)
    goles_visitante = pintaGoles(visitante, listGolesVisitante)
    res = "{} \n{} \n{}".format(header, goles_local, goles_visitante)
    return res

def pintaGoles(equipo, goleadores):
    res = ""
    if len(goleadores)>0:
        res = "Para el "+equipo+" ha marcado "+','.join(goleadores)
    else:
        res = "El "+equipo+" no ha marcado"
    return res