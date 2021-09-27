Catalog Admin System
=============

Systems allows manage products


# Quick start

* Clone this repository.
* Install docker
* Install docker-compose
* Open a terminal and run next commands:
    
    1. Go to project root directory
    2. Build services
        * **sudo docker-compose -f docker-compose-local.yml build**
    3. Start application
        * **sudo docker-compose -f docker-compose-local.yml up**
        * This process sets up the services for this environmet:
            * Django
            * Postgres
            * Redis
            
    * Note: If you add some new models, before run **docker-compose build** and **docker-compose up**.
    It is necessary to run the migrations with the following command, after **docker-compose build** and before **docker-compose up**.
        * **sudo docker-compose -f docker-compose-local.yml run --rm django python manage.py makemigrations**

      
# Verifying 

1. Open other terminal and run **sudo docker ps**, it should show 3 containers:    
    * django
    * postgres
    * redis

2. Go to **http://localhost:8000/admin/** in your browser, and you should see the admin login

3. Now, you need to make the first user 
    * **sudo docker-compose -f docker-compose-local.yml run --rm django python manage.py createsuperuser**
    * Note: All superuser created with this method is administrator (They are not anonymous users)

4. Congratulation, you can now enter the admin!


# How to use the user API

#### Sign up like a user

**Endpoint: {{host}}/users/v1/signup/**

>**HTTP Verb: POST**

**Header:** 
> Content-Type:application/json
> Accept:application/json

**Body:**

       {
            "email":"jonathan.mdzmtz@gmail.com",
            "username":"jmendoza",
            "phone_number":"5523097299",
            "password":"zxcvbnm12345",
            "password_confirmation":"zxcvbnm12345",
            "first_name":"Jonathan",
            "last_name":"Mendoza",
            "is_admin": true
       }

**Response**
        
        {
            "email": "jonathan.mdzmtz@gmail.com",
            "username": "jmendoza",
            "first_name": "Jonathan",
            "last_name": "Mendoza",
            "phone_number": "5523097299",
            "is_admin": true
        }

#### Login 

**Endpoint: {{host}}/users/v1/login/**

>**HTTP Verb: POST**

**Header:** 
> Content-Type:application/json
> Accept:application/json

**Body**

        {
            "email":"jonathan.mdzmtz@gmail.com",
            "password":"zxcvbnm12345"
       }

**Response**
        
        {
            "user": {
                "email": "jonathan.mdzmtz@gmail.com",
                "username": "jmendoza",
                "first_name": "Jonathan",
                "last_name": "Mendoza",
                "phone_number": "5523097299",
                "is_admin": true
            },
        "access_token": "cdb93a784426fa5f7fffbaacd4709d5999c80a51"
        }

#### User detail 

**Endpoint: {{host}}/users/v1/jmendoza/** (username = jmendoza)

>**HTTP Verb: GET**

**Header:** 
> **Authorization: Token {{access_token}}**
> Accept:application/json

**Response**
        
        {
            "email": "jonathan.mdzmtz@gmail.com",
            "username": "jmendoza",
            "first_name": "Jonathan",
            "last_name": "Mendoza",
            "phone_number": "5523097299",
            "is_admin": true
        }

#### Update user 

**Endpoint: {{host}}/users/v1/jmendoza/** (username = jmendoza)

>**HTTP Verb: PUT**

**Header:** 
> **Authorization: Token {{access_token}}**
> Content-Type:application/json
> Accept:application/json

**Body**

        {
            "email":"jonathan.mdz@gmail.com",
            "username":"dmendoza",
            "phone_number":"5523097291",
            "first_name":"Yonathan",
            "last_name":"Mendez",
            "is_admin": false
        }

**Response**
        
        {
            "email": "jonathan.mdz@gmail.com",
            "username": "dmendoza",
            "first_name": "Yonathan",
            "last_name": "Mendez",
            "phone_number": "5523097291",
            "is_admin": false
        }


## Notes

#### How to make django migrations

You need to run only the django service (from the docker-compose.yml file). Run the make migrations command and end the django service container.

   * **sudo docker-compose -f docker-compose-local.yml run --rm django python manage.py makemigrations**


#### How to do a clean restart of a docker instance

Note: Deleting volumes will wipe out their data. Back up any data that you need before deleting a container.

1. Stop the containers with the following command:
      * if you have the stack executed in a console
          (that is, you executed **sudo docker-compose -f docker-compose-local.yml up**)
          You must stop the processes run **ctrl + c**
    
      * if you have the stack executed in detached mode
          (that is, you executed **sudo docker-compose -f docker-compose-local.yml up -d**)
          You must stop the processes run
          * **sudo docker-compose -f docker-compose-local.yml down**
            
2. Delete all containers using the following command:
    * **sudo docker rm -f $(sudo docker ps -a -q)**
    
3. Delete all volumes using the following command:
    * **sudo docker volume rm $(sudo docker volume ls -q)**

4. Restart the containers using the following command:
    * **sudo docker-compose -f docker-compose-local.yml up**

Sometimes it is necessary to delete the images

5. Delete all images using the following command:
    * **sudo docker rmi $(sudo docker images -q)**
    
6. Build services
    * **sudo docker-compose -f docker-compose-local.yml build**

7. Restart the containers using the following command:
    * **sudo docker-compose -f docker-compose-local.yml up**
