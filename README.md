# editor-writer-demo
Editor Writer demo

Small demo on django and dockers


just install docker and docker-compose you can read from https://docs.docker.com/install/ be sure to follow your OS structions

once cloned this repository jump into it and do

$ docker-compose run web python3 manage.py migrate

to initialize the db

$ docker-compose run web python3 manage.py createsuperuser

to create first user

then run

$ docker-composer up

and direct broser to localhost:8000/admin (please check the OS instalation instructions to the correct name)

login as a super user and create some users (some writers and some readers)

and some articles, 

then direct the broser to localhost:8000

adn login with a writer user and then with a editor user and proceed to move up articles.


