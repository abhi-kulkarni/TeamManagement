# TeamManagement

Steps for running the project on local system (Linux):

1) Clone the repository using the command in your terminal :
- git clone https://github.com/abhi-kulkarni/TeamManagement.git

2) Create a virtual environment for python3 using the command:
- python3 -m venv <virtual_env_folder_name> 

Activate your virtual environment using the below command:
- source <path_to_virtual_env_folder>/bin/activate

3) Install all the requirements for the project using the below command:
- pip install -r requirements.txt

4) Create a new database using MYSQL.

5) Go inside the team_management_app folder and create a .env file in the same directory as "manage.py" and replace the below with your data. 

    SECRET_KEY=<YOUR_SECRET_KEY> <br />
    DEBUG=True <br />
    TEMPLATE_DEBUG=True <br />
    DB_ENGINE=django.db.backends.mysql <br />
    DB_NAME=<YOUR_DB_NAME> <br />
    DB_USER=<YOUR_DB_USER> <br />
    DB_PASSWORD=<YOUR_DB_PASSWORD> <br />
    DB_HOST=127.0.0.1 <br />
    DB_PORT=3306 <br />
    BASE_URL=http://127.0.0.1:8000 <br />
    ENV=dev <br />

6) Go inside the directory containing manage.py and run the following command :
- python manage.py makemigrations
- python manage.py migrate

7) Once all the above steps are done, you can run the below command:
- python manage.py runserver

8) The project will be up and running on your localhost 
- http://127.0.0.1:8000