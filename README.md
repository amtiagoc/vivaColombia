## Santiago Cano Duque - Prueba Tecnica Backend 

### Dockerize the project

1. I added a Dockerfile with a content like the one below:
-------------------------------------
```
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```
2. I create a requierements.txt, instead of installing what i need one by one
```
asgiref==3.5.0
Django==4.0.4
sqlparse==0.4.2
requests==2.27.1
```
3. Right after that, I add docker-compose.yml -> To define the services and environment of the django project that we needd, one of them is redis.

4. Now I'm going to create the django project, and configure to run the server by docker using "docker-compose up"

### How the endpoint works?

1. There is the endpoint of the top stories, that display all the most recent stories and show its id. I modified that endpoint in views.py

2. After collecting all the data, there is a loop to iterate in the Json. but, there is a condition that depend of a range that the user defines so on base of that it will show the stories.

3. Finally i use a list, to add each attribute of each story.

4. Finally i return a JsonResponse to visualize a json in the url.




