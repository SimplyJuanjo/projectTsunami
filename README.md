# projectTsunami
[ENG]:
In this project we will develop a multi platform app for easily organizing and managing "table soccer tournaments" / classic Spanish "Futbolín"

- This app is designed to help the tournament organizers save time while managing all the teams and games. 
- The app is not expected to have internet connection or cloud functionalities at first. Maybe in a future we can develop an upgrade if the local version fit the market.
## Features to add:
- The start screen would be a display with a selection of classic tournaments preset. (TODO)
- The start screen would have a button to create new customizable tournaments. (TODO)
- The customized tournaments would be saveable. (TODO)
- Presets and saved tournaments could be chosen, modified and deleted by the user. (TODO)

- When creating a new tournament the following features may be modifiable:
    - Number of categories: (Pro, Pro + Master, Pro + Master + Advanced).
    - Create Teams and select their respective category (if more than 1 category selected).
    - Choose if you want only to randomize and play a group phase prior to the brackets
        or the brackets will be directly randomized.
    - Choose the number of groups, the games played in each group and the goals needed to win a game.
    - Choose if the groups are played 1 by 1 or all groups together.
    - Choose how many teams will get classified from each group.
    - Choose how many loses each team can have in each category (single KO or double KO) and the goals needed to win per game in each category.
    - Choose if the matches are played to best of 1 or best of 3. (maybe not needed)

- Once the tournament is configured the app should randomize the groups trying to put the same amount of teams from each category in each group to keep them evenly matched.
- The app should ordered the games to be played while trying to make the teams wait the same amount of time between matches whenever possible.
- Results from the games should be introduced and saved in the app.
- Group rankings will be shown when needed with the Wins, Losses and Goal Difference of each team.
- TBC

[ESP]:
En este proyecto desarrollaremos una app multiplataforma para organizar y gestionar fácilmente "torneos de futbolín"

- Esta aplicación está diseñada para ayudar a los organizadores de torneos a ahorrar tiempo en la gestión de todos los equipos y partidos. 
- Al principio no se espera que la aplicación tenga conexión a Internet o funcionalidades en la nube. Tal vez en un futuro podamos desarrollar una actualización si la versión local encaja en el mercado.
## Características a añadir:
- La pantalla de inicio sería una pantalla con una selección de torneos clásicos preestablecidos. (TODO)
- La pantalla de inicio tendría un botón para crear nuevos torneos personalizables. (TODO)
- Los torneos personalizados se podrían guardar. (TODO)
- Los torneos preestablecidos y guardados podrían ser elegidos, modificados y eliminados por el usuario. (TODO)

- Al crear un nuevo torneo las siguientes características estarían disponibles:
    - Número de categorías: (Pro, Pro + Master, Pro + Master + Avanzado).
    - Crear equipos y seleccionar su respectiva categoría (si se selecciona más de 1 categoría).
    - Elegir si se quiere sólo aleatorizar y jugar una fase de grupos previa a los brackets
        o los brackets serán directamente aleatorios.
    - Elegir el número de grupos, los partidos que se juegan en cada grupo y los goles necesarios para ganar un partido.
    - Elegir si los grupos se juegan 1 a 1 o todos los grupos juntos.
    - Elegir cuántos equipos se clasificarán de cada grupo.
    - Elegir cuántas derrotas puede tener cada equipo en cada categoría (KO simple o KO doble) y los goles necesarios para ganar por partido en cada categoría.
    - Elegir si los partidos se juegan al mejor de 1 o al mejor de 3. (quizás no sea necesario)

- Una vez configurado el torneo la app debería aleatorizar los grupos intentando poner la misma cantidad de equipos de cada categoría en cada grupo para mantenerlos igualados.
- La aplicación debería ordenar los partidos a jugar intentando que los equipos esperen el mismo tiempo entre partidos siempre que sea posible.
- Los resultados de los partidos deben introducirse y guardarse en la app.
- La clasificación de los grupos se mostrará cuando sea necesario con las victorias, derrotas y diferencia de goles de cada equipo.
- TBC



## TODO: Finish with this translation and cleaning:
Y una vez esto este listo en caso de que se clasifiquen todos, generara el cuadro de categoria mas alta con todas las parejas y en caso de haber huecos vacios se asignaran
 de mejor a peor clasificado. Una vez esto este listo se jugara de arriba a abajo el cuadro y se iran introducion resultados o ganadores directamente y la app ira colocando y
 formando los emparejamientos de las siguientes fases del cuadro

Lo primero que se creara sera los dos mas miticos que seran:
 -Torneo con fase de grupos con unica categoria y con seleccion de clasificacion y seleccion de ko directo o doble ko
 -Torneo con fase de grupos con 2 categorias y y con seleccion de clasificacion y seleccion de ko directo o doble ko
