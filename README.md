# cs-inventario-backend

## Instrucciones para crear entorno de desarrollo

1.  Instalación de requisistos(requiere permisos de root o utilizar sudo)
    *   Paquetes indispensables
    ```
    apt-get install python3.6 python-pip python3-pip python3.6-dev virtualenv pwgen
    ```

2.  Instalación de aplicación y requisitos.
    *   Clonar repositorio en directorio de trabajo local(se asume configuración por defecto de git).
    *   Para el resto de de las instrucciones el directorio de trabajo será el del proyecto
    ```
    cd cs-inventario-backend
    ```
    *   Entorno virtual
    ```
    virtualenv -p /usr/bin/python3.5 .venv
    source .venv/bin/activate
    ```
    *   Instalación de dependencias
    ```
    pip install -r requirements.txt
    ```
    *   Aplicar migraciones
    ```
    ./manage.py migrate
    ```
    *   Cargar datos iniciales
    ```
    ```
    *   Lanzar aplicación
    ```
      ./manage.py runserver
    ```
    *   Abrir la url localhost:8000 en navegador

## git IMPORTANTE
*   Cuando se haga un git pull efectuar git pull --rebase cuando se posible

## Enlaces a documentación
*   [https://docs.python.org/3.6/]()
*   [https://docs.djangoproject.com/en/2.0/]()
*   [http://www.django-rest-framework.org/]()
*   [https://pip.pypa.io/en/stable/user_guide/]()
*   [http://docs.python-guide.org/en/latest/dev/virtualenvs/]()
*   [https://openpyxl.readthedocs.io/en/default/usage.html]()

## PEP 8
*   [https://www.python.org/dev/peps/pep-0008/]()

## Autentificación
*   [http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication]()
*   [https://marcgibbons.github.io/django-rest-swagger/settings/]()
