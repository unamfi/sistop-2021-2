
Problema del alumno y el asesor

Decidimos usar python3 y lo codificamos en sublimetext.

Para ejecutarlo basta con abrir la terminal, colocarse en la carpeta donde se encuentra el archivo y escribir "python3 alumnoYasesor.py"

El primer patrón de sincronización que usamos fue el Multiplex, ya que se delimita el acceso a 6 alumnos a la vez (ya que hay solo 6 sillas). Después utilizamos un mutex para cuidar el arreglo de alumnos con dudas. Utilizamos una señalización "despertar_asesor" para notificar al asesor que hay un alumno con dudas y despertarlo, y por último usamos otra señalización llamada "responder" que es enviada por el asesor cuando está disponible para responder una duda. 

Nuestro problema no tenía refinamientos.

Durante el proceso no tuvimos dudas pero en un momento habíamos implementado un torniquete para que pasaran de alumno en alumno, sin embargo creemos que mutex_alumnos ya nos ayuda con eso.