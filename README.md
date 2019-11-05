# Proyecto de arquitectura del software

1. Recomendable crear un entorno virtual `virtualenv`

2. Instalar los paquetes necesarios con `pip install > requirements.txt`

3. `path/to/project/hotelHangares` y ejecutar `python manage.py migrate`

4. Es importante ingresar información de los tipos de usuarios antes de crear alguno, para ellos ejecutaremos el comando `python manage.py loaddata TipoUsuario`

5. Luego crear un super usuario `python manage.py createsuperuser`

6. Correr servidor `python manage.py runserver`

7. Ingresar ` http://localhost:8000/api/v1.0/ ` o ` http://localhost:8000/`

   > Enderson Vizcaino 
   >
   > Christian Rodríguez