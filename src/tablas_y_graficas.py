import matplotlib.pyplot as plt

def tablasLocalVisitante(local,visitante,df_final):
    df_consulta = df_final[df_final["Local"]==local]
    df_consultaVis = df_final[df_final["Visitor"]==local]
    df_consulta2 = df_final[df_final["Local"]==visitante]
    df_consultaVis2 = df_final[df_final["Visitor"]==visitante]
    dfEquipLocalLocal=(df_consulta[['Date','Local','GoalsLocal','GoalsVisitor','Visitor']])
    dfEquipVisitanteLocal=(df_consultaVis[['Date','Local','GoalsLocal','GoalsVisitor','Visitor']])
    dfEquipLocalVisitante=(df_consulta2[['Date','Local','GoalsLocal','GoalsVisitor','Visitor']])
    dfEquipVisitanteVisitante=(df_consultaVis2[['Date','Local','GoalsLocal','GoalsVisitor','Visitor']])
    dfEquipLocalLocal.to_csv('../Outputs/{}comolocal.csv'.format(local))
    dfEquipVisitanteLocal.to_csv('../Outputs/{}comovisitante.csv'.format(local))
    dfEquipLocalVisitante.to_csv('../Outputs/{}comolocal.csv'.format(visitante))
    dfEquipVisitanteVisitante.to_csv('../Outputs/{}comovisitante.csv'.format(visitante))
    return dfEquipLocalLocal, dfEquipVisitanteLocal, dfEquipLocalVisitante, dfEquipVisitanteVisitante
    
def pintarMaxGolesEnSuRol(local,visitante,df_final):
    df_consulta = df_final[df_final["Local"]==local]
    df_consultaVis = df_final[df_final["Visitor"]==local]
    a =(df_consulta['GoalsLocal'].max())
    b =(df_consultaVis['GoalsVisitor'].max())
    df_consulta2 = df_final[df_final["Local"]==visitante]
    df_consultaVis2 = df_final[df_final["Visitor"]==visitante]
    c =(df_consulta2['GoalsLocal'].max())
    d =(df_consultaVis2['GoalsVisitor'].max())
    x=(local+" loc.",visitante+" loc.",local+" vis.",visitante+" vis.")
    y=(a,c,b,d)
    plt.bar(x,y)
    plt.title('Máximo número de goles en su rol(local/visitante)', fontsize=17, color='Blue')
    plt.xlabel("Equipos")
    plt.ylabel("Media")
    plt.savefig('../Outputs/maxGoles{}{}.png'.format(local,visitante))

def pintarMediaGolesEnSuRol(local,visitante,df_final):
    df_consulta = df_final[df_final["Local"]==local]
    df_consultaVis = df_final[df_final["Visitor"]==local]
    f =(df_consulta['GoalsLocal'].mean())
    g =(df_consultaVis['GoalsVisitor'].mean())
    df_consulta2 = df_final[df_final["Local"]==visitante]
    df_consultaVis2 = df_final[df_final["Visitor"]==visitante]
    h =(df_consulta2['GoalsLocal'].mean())
    i =(df_consultaVis2['GoalsVisitor'].mean())
    x=(local+" loc.",visitante+" loc.",local+" vis.",visitante+" vis.")
    y=(f,h,g,i)
    plt.bar(x,y)
    plt.title('Media de goles en su rol(local/visitante)', fontsize=17, color='Blue')
    plt.xlabel("Equipos")
    plt.ylabel("Media")
    plt.savefig('../Outputs/mediaGoles{}{}.png'.format(local,visitante))