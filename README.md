# projectTsunami

- TODO : Translation to English and Cleaning the Text to be more easily readable

La app en un principio no tendra conexion a servidor para poder compartir torneos y sera una app local para el organizador del torneo

La pantalla de inicio seria una pantalla con los torneos ya creados y un boton para crear un nuevo torneo. Si hay torneos creados estos tendran un boton para modificarlos o borrarlos

Al crear un nuevo torneo se debe dejar, primero seleccionar cuantas categorias hay, luego se añaden las parejas en las cuales se pondra un solo nombre, ya sea de equipo o
 nombre-nombre. A cada pareja le habra que poner en la categoria que participa. En caso de haber solo una categoria esto no seria necesario. Una vez que sabemos las categorias
 y las parejas se nos pedira seleccionar como sera el torneo. Por ejemplo si se sorteara y se hara la tabla directamente o si se hara una fase de grupo previa. La fase de
 grupos dejara seleccionar cuantos grupos se haran, dependiendo de cuantos grupos se hagan pondra cuantas partidas se juegan y dejara seleccionar a cuantos goles van las
 partidas de grupos. Una vez configurada la fase de grupos preguntara cuanta gente se clasificara y como se quiere configurar cada categoria, preguntando si sera ko directo
 o doble ko y a cuantos goles seran las partidas.

Se deberia poder selecionar si se van a jugar todos los grupos a la vez o si jugara un grupo detras de otro

Una vez el torneo este configurado la app debera generar los grupos de forma aleatoria pero haciendo que en todos los grupos haya las mismas personas de cada categoria o sean
 lo mas nivelados posible. Una vez esto este listo se empezara a jugar la fase de grupos, para esto la app debera buscar la forma optima de ordenar los partidos para que las
 parejas dejen mas o menos la misma distancia entre partido y partido y asi una no juegue varios partidos seguidos. Una segun se vayan jugando partidos se debera introducir
 en la app los resuldados de los mismos. Se podria poner alguna forma de mostrar los resultados temporales mientras no se acabe la fase de grupos, pero lo principal seria
que al acabar la fase de grupos los ordene por puestos.

Y una vez esto este listo en caso de que se clasifiquen todos, generara el cuadro de categoria mas alta con todas las parejas y en caso de haber huecos vacios se asignaran
 de mejor a peor clasificado. Una vez esto este listo se jugara de arriba a abajo el cuadro y se iran introducion resultados o ganadores directamente y la app ira colocando y
 formando los emparejamientos de las siguientes fases del cuadro

Lo primero que se creara sera los dos mas miticos que seran:
 -Torneo con fase de grupos con unica categoria y con seleccion de clasificacion y seleccion de ko directo o doble ko
 -Torneo con fase de grupos con 2 categorias y y con seleccion de clasificacion y seleccion de ko directo o doble ko
