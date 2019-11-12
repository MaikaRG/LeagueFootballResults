import argparse
import subprocess
from scraping_por_equipos import resultado
import pandas as pd
import warnings
warnings.simplefilter(action='ignore')
from fpdf import FPDF
from pdf import createPDF
from tablas_y_graficas import tablasLocalVisitante, pintarMaxGolesEnSuRol,pintarMediaGolesEnSuRol
from pruebamail import mail

def recibeParametros():
    parser = argparse.ArgumentParser(description='Conocer resultado y goleadores')
    parser.add_argument('--local',help='Equipo Local entre comillas',type=str)
    parser.add_argument('--visitante',help='Equipo Visitante entre comillas',type=str)
    parser.add_argument('--mail',help='mail al que enviarlo entre comillas',type=str)
    parser.add_argument('--temporada', help='2018-2019')             
    args = parser.parse_args()
    return args

def main():
    parametros = recibeParametros()
    filename = '../Inputs/{}.csv'.format(parametros.temporada)
    df_final=pd.read_csv(filename)
    resultado(parametros.local,parametros.visitante,df_final)
    a = resultado(parametros.local,parametros.visitante,df_final)
    print(a)
    dfEquipLocalLocal, dfEquipVisitanteLocal, dfEquipLocalVisitante, dfEquipVisitanteVisitante = tablasLocalVisitante(parametros.local,parametros.visitante,df_final)
    print(dfEquipLocalLocal)
    print(dfEquipVisitanteLocal)
    print(dfEquipLocalVisitante)
    print(dfEquipVisitanteVisitante)
    pintarMaxGolesEnSuRol(parametros.local,parametros.visitante,df_final)
    pintarMediaGolesEnSuRol(parametros.local,parametros.visitante,df_final)
    createPDF(a,parametros.local,parametros.visitante)
    mail(parametros.mail,parametros.local,parametros.visitante)
    
if __name__=="__main__":
    main()