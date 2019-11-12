# LeagueFootballResults

Goleadores de cada equipo según partido y temporada

El objetivo de este proyecto es saber quienes fueron los goleadores de cada equipo, según los parametros de entrada: equipo local, equipo visitante, temporada.

La informacion de los partidos jugados y el resultado se ha obtenido de un dataset online, se ha escrapeado de [FBREF](https://fbref.com/en/comps/12/1886/schedule/2018-2019-La-Liga-Fixtures) para sacar el link, anexarlo al dataset original, se va a escrapear según los parametros de entrada en el link correspondiente en el momento de la consulta.

Los goleadores se obtienen mediante escrapeo del link que se filtra con los datos de entrada.

Los parametros de entrada son:

- Equipo local.
- Equipo visitante.
- Temporada.
- Mail(para enviar resultados por mail a alguien(en PDF))

El resultado obtenido es:

- Tablas en formato csv en Outputs(de cada equipo seleccionado como local y visitante)

- Gráficas en png en Outputs(máximo y media de goles por cada uno de los equipos seleccionados siendo local y visitante,(gráficas de barras))

- PDF con el texto (resultado + quien marco para cada equipo + graficas del Outputs)
- Mail a la persona que se solicita por consola

### Próximos pasos

- Limpieza de más datasets para tener el resultado de más temporadas.