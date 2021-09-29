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


# Email

**For local environment**
>+ Build and run the services with **docker-compose-local.yml** file
>+ It's define environment variables at .env.local path
>+ And send emails with Django Backend Email


**For production environment**
>+ Build and run the services with **docker-compose-production.yml** file
>+ It's define environment variables at .env.production path
>+ And send emails with AWS SES


# Examples

**For local environment**
>+ Build and run the services with **docker-compose-local.yml** file
>+ It's define environment variables at .env.local path
>+ And send emails with Django Backend Email
>+ If you want run AWS SES at local environtment, add aws variables in ./envs/.local/.aws/* path 
and change ENV=local to ENV=prod in ./envs/.local/.django

**For production environment**
>+ Build and run the services with **docker-compose-production.yml** file
>+ It's define environment variables at .env.production path
>+ And send emails with AWS SES


# Examples
___
## USERS

#### Login 

Use the super user, previously created in the verify section

**Endpoint: {{host}}/users/v1/login/**

>**HTTP Verb: POST**

**Header:** 
> * Content-Type:application/json
> * Accept:application/json

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

#### Sign up like a user

**Endpoint: {{host}}/users/v1/signup/**

>**HTTP Verb: POST**

**Header:**
> * **Authorization: Token {{access_token}}** 
> * Content-Type:application/json
> * Accept:application/json

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

#### User detail 

**Endpoint: {{host}}/users/v1/jmendoza/** (jmendoza is username and lookup field)

>**HTTP Verb: GET**

**Header:** 
> * **Authorization: Token {{access_token}}**
> * Accept:application/json

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

**Endpoint: {{host}}/users/v1/jmendoza/** (jmendoza is username and lookup field)

>**HTTP Verb: PUT**

**Header:** 
> * **Authorization: Token {{access_token}}**
> * Content-Type:application/json
> * Accept:application/json

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

#### Delete user 

**Endpoint: {{host}}/users/v1/jmendoza/** (jmendoza is username and lookup field)

>**HTTP Verb: DELETE**

**Header:** 
> * **Authorization: Token {{access_token}}**


## PRODUCTS

#### Create a product 

**Endpoint: {{host}}/products/v1/**

>**HTTP Verb: POST**

**Header:** 

> * **Authorization: Token {{access_token}}**
> * Content-Type:application/json
> * Accept:application/json

**Body**

        {
            "name":"Playera",
            "sku":"P0001",
            "price": 100.01,
            "brand": "Patito",
            "is_public": true
        }

**Response**
        
        {
            "name": "Playera",
            "sku": "P0001",
            "price": "100.01",
            "brand": "Patito",
            "is_public": true
        }

#### List a products 

**Endpoint: {{host}}/products/v1/**

>**HTTP Verb: GET**

**Header:** 

> * **Authorization: Token {{access_token}}**
> * Accept:application/json

**Response**
        
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "Playera",
                "sku": "P0001",
                "price": "100.01",
                "brand": "Patito",
                "is_public": true
            },
            {
                "name": "Pantalon",
                "sku": "P0002",
                "price": "100.01",
                "brand": "Patito",
                "is_public": true
            }
        ]
    }

#### Product detail 

**Endpoint: {{host}}/products/v1/P0001/** (P0001 is sku and lookup field)

>**HTTP Verb: GET**

**Header:** 
> * Accept:application/json

**Response**
        
    {
        "name": "Playera",
        "sku": "P0001",
        "price": "100.01",
        "brand": "Patito",
        "is_public": true
    }

#### Delete a product 

**Endpoint: {{host}}/products/v1/P0002/**  (P0002 is sku and lookup field)

>**HTTP Verb: DELETE**

**Header:** 
> * **Authorization: Token {{access_token}}**

## How to entry to data base

1. Open a terminal and run the containers 
    * **sudo docker-compose -f docker-compose-local.yml up**

2. Open another terminal and get container id of postgres service
    * **sudo docker ps**

3. Go to environment variables path (.envs/.local/.postgres) and get **POSTGRES_USER** and **POSTGRES_DB**

4. Run next command
    * **sudo docker exec -it CONTAINER_ID psql -U POSTGRES_USER -a POSTGRES_DB**
    
    * For example
        * **sudo docker exec -it f22dae79a480 psql -U sBLRWyyPsInwHftmHAWmYJURGWBGFpLs -a catalog**

5.- Some interesting commands
> * Show tables
>   * **\dt**
> * Show table definition
>   * **\d TABLE_NAME**
> * To go out
>   * **\q**



## Notes

#### How to make django migrations

You need to run only the django service (from the docker-compose.yml file). Run the make migrations command and end the 
django service container.

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
