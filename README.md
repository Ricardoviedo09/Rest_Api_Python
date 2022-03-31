# Rest_Api_Python

• Resumen

Es una api, diseñada para que los colaboradores de un restaurante puedan gestionar los clientes que llegan el dia de la jornada de almuerzo organizada
por el dueño del lugar, puede almacenar los clientes, asi como editarlos, eliminarlos o simplemente leer esa información proveniente de una base de datos.

Pueden realizar consultas, tales como buscar por nombre o correo, o por el id asignado al momento de crear al cliente, pueden organizar los nombres de la A a la Z
o viceversa, organizar por edad de mayor a menor y les devuelve los clientes en paginas de 10 clientes c/u.

• Paquetes/librerias

- Flask: micro framework que utilizamos para la creacion de nuestro servicio web.
- Flask-sqlalchemy: ORM que facilita con la conexión y administración de la base de datos manejando las consultas como objetos dentro del programa.
- Sqlalchemy: utilizado para usar su función desc().
- Re: regulagor de expresiones regulares que utilizamos para validar si el texto facilitado era un email.
- Flask_marshmallow: permite crear schemas del modelo de la base de datos, para la obtención de los datos dependiendo si sabemos que el retorno nos devolverá uno o mas objetos.
- Marshmallow: facilita la creación del schema con su método fields
- Pymysql: driver de mysql para la conexión con la base de datos a través de flask-sqlalchemy
- marshmallow-sqlalchemy: complemento

• Montar entorno

- Clonar archivos del repositorio
- Crear la base de datos, en este caso de nombre "pruebapractica"
- Crear un entorno de desarrollo, puede ser con virtualenv
- Activar el entorno
- Instalar todos los paquetes mencionados arriba
- Ejecutar python app.py

• Estructura de proyecto

Objetivos

- Poder crear, leer, modificar y eliminar los registros
- Buscar por correo y nombre al realizar una búsqueda de un registro
- Filtrar por edad mayor a menor.
- Filtrar por nombre de la A a la Z.
- Paginar los registros a 10 registros por página, organizado desde el más reciente al más viejo.

Finalidad

- Lograr que el restaurante pueda tener al final de cada dia un conteo de todas las personas que visitaron su jornada de almuerzo, tenerlas almacenadas
y poder administrarlas, para posibles vias de contacto y demas.

• URL de acciones

- Listar todas los registros
http://127.0.0.1:5000/lunchs


- Obtener todos los registros paginados
http://127.0.0.1:5000/lunchs/page=
Nota: en page= colocar la pagina a mostrar => (page=1, page=2)

- Obtener todos los registros en orden ASC, DESC o EDAD
http://127.0.0.1:5000/lunchs/order=
Nota: en order= colocar lo que desee obtener => (order=asc, order=desc, order=age)

- Obtener registros filtrando por ID, Nombre o Email
http://127.0.0.1:5000/lunchs/
Nota: despues del lunchs/ colocar lo que desee obtener, ya sea un id, nombre o email. => (lunchs/2, lunchs/ricardo, luchs/example@example.com)
Nota2: Usando el metodo POST, PUT y DELETE con solo ID, se pueden crear, actualizar o borrar los registros
- 
