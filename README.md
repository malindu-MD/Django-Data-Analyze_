# OctopusBi-Assessment

 cloning the backend project(https://github.com/malindu-MD/OctopusBi-Assessment.git)add datasets to data folder.

Steps to create Docker image and run Django Application
==============================================
    Clone the repository - https://github.com/malindu-MD/OctopusBi-Assessment.git
    Go to OctopusBi-Assessment directory
    add the CSV files to data folder ,if you want to  import the all (more) data(Run command python manage.py importData)
    run the this command for create docker image ----->  docker build -t mydjangoapp .
    run the this command for create docker container ------>  docker run -p 8000:8000
    Open a web browser and go to http://localhost:8000 to access your Django application running inside the Docker container.
    Open a web browser and go to http://localhost:8000/admin to access Admin side (username-admin,password-admin).





local Run step
==============================================

    Clone the repository - https://github.com/malindu-MD/OctopusBi-Assessment.git
    Install Python with Pip
    Run pip install -r requirements.txt
    Go to OctopusBi-Assessment directory
    add the CSV files to data folder ,if you want to  import the all data(Run command python manage.py importData)
    Run python manage.py runserver
    http://127.0.0.1:8000/
