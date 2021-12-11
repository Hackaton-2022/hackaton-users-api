# Microservicio de autenticación y manejo de usuarios

Microservicio de manejo de usuarios y autenticación, contiene toda la logica para el manejo de usuarios y autenticación mediante el uso de una API Rest junto con JWT.


## 💻 Requisitos

* Python 3.9
* PostgreSQL
* Docker

## 🛠️ Guia de configuracion

El proyecto se encuentra corriendo bajo un host de docker, es posible utilizar el proyecto de manera local utilizando python o utilizando docker


### Creacion de variables de entorno
En la raiz del proyecto se debe crear un archivo con el nombre **.env**, este archivo con la siguiente informacion

```
DEBUG=<Boolean: False o True>
SECRET_KEY=<secret key, puede ser cualquier string>
DB_NAME=<nombre db>
DB_USER=<usuario de la db>
DB_PASSWORD=<contraseña de la db>
DB_HOST=<host de la db>
DB_PORT=<puerto de la db>
```

Si se desea trabajar en un entorno de desarrollo, se debe actualizar la variable DEBUG a True. 
**En el entorno de desarrollo la informacion de la base de datos no tiene relevancia ya que se utiliza una base de datos sqlite**


La informacion suministrada no debe tener comillas o espacios

### Configuración tradicional

La guia de configuracion esta creada bajo comandos de Windows. Todos los comandos se deben realizar en la raiz del proyecto (carpeta del proyecto) a la altura del archivo manage.py.

#### 1️⃣ Crear entorno virtual
```console
python -m venv venv
```

#### 2️⃣ Ejecutar entorno virtual
```console
.\venv\Scripts\activate
```

#### 3️⃣ Instalar dependencas del proyecto
```console
pip install -r requirements.txt
```

#### 4️⃣ Realizar migraciones
```console
python manage.py makemigrations
```
```console
python manage.py migrate
```

#### 5️⃣ Crear superusuario
```console
python manage.py createsuperuser
```

#### 6️⃣ Inicio del servidor
```console
python manage.py runserver
```

Para un entorno de produccion se debe utilizar adicionalmente el siguiente comando antes de iniciar el servidor

#### 7️⃣ Generacion de archivos estaticos (solo produccion)
```console
python manage.py collectstatic
```

### Configuracion via Docker

La guia de configuracion esta creada bajo comandos de Windows. Todos los comandos se deben realizar en la raiz del proyecto (carpeta del proyecto) a la altura del archivo manage.py.

#### 1️⃣ Inicio del servidor Docker
```console
docker-compose up
```

#### 3️⃣ Crear superusuario
De ser necesario es posible crear un superusuario con el comando
```console
docker-compose exec users python3 manage.py createsuperuser
```

Para cerrar el servidor una vez inicializado se debe usar el comando:

#### ⏹️ Cerrar servidor Docker
```console
docker-compose down -v
```

## ⚙️ API

Un usuario solo podra obtener, modificar y eliminar su propia información, solo los usuarios con permisos de administrador pueden acceder y modificar la información de otros usuarios.

