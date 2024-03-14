# La Caffettiera: Web Empresarial

La Caffettiera es una plataforma web empresarial desarrollada para una cafetería ficticia del mismo nombre. Esta aplicación web está construida con Python y el framework Django, combinando partes estáticas y dinámicas para ofrecer una experiencia completa a los usuarios.

## Características

- **Partes estáticas:** La interfaz está construida utilizando HTML, CSS y la librería Bootstrap, ofreciendo una presentación atractiva de la información sobre la cafetería, incluyendo su historia, menú y ubicación.

- **Partes dinámicas:**
  - **Blog:** Los usuarios pueden crear y gestionar entradas de blog, permitiendo a la cafetería compartir noticias, recetas y eventos.
  - **Gestión de contactos:** Facilita la comunicación con la empresa, ofreciendo enlaces directos para consultas y reservas.
  - **Formulario de mensajes:** Permite a los clientes enviar mensajes directamente al equipo de la cafetería, mejorando la comunicación y el servicio al cliente.
  - **Sección de entradas recientes:** Muestra las últimas actualizaciones y ofertas de la cafetería, manteniendo a los visitantes informados sobre las novedades más relevantes.

## Instalación y Uso

1. Clona este repositorio en tu máquina local.
2. Instala los requisitos del proyecto ejecutando `pip install -r requirements.txt`.
3. Realiza las migraciones de la base de datos con `python manage.py migrate`.
4. Crea un superusuario con `python manage.py createsuperuser` para acceder al panel de administración.
5. Inicia el servidor local con `python manage.py runserver`.
6. Accede a la aplicación desde tu navegador web visitando `http://localhost:8000`.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y commitealos (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Autores

Este proyecto fue desarrollado por [Álvaro García](https://github.com/GVAlvaro96).

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
