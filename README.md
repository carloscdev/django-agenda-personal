<p align="center">
  <a href="http://me.carlosc.dev" target="blank"><img src="https://cdn.pixabay.com/photo/2017/06/19/02/06/agenda-2417912_960_720.png" width="300" alt="Agenda Perosnal" /></a>
</p>

## Description

Agenda Personal - Contactos - Tareas
<hr />

## Running the app

* __Clone this respository__

```bash
$ git clone https://github.com/carloscdev/django-agenda-personal/
```

* __Create a virtual enviroment__

```bash
python3 -m venv venv
```

* __Initialize the venv (Windows)__
```bash
.\venv\Scripts\activate
```

* __Install the dependencies__
```bash
pip3 install -r requirements.txt
```

* __Run project__
```bash
docker-compose up -d
```

__or with python locally but you need to have PostgreSQL installed and expose the env variables from docker-compose.yaml:17-22 file__
```bash
python3 mangage.py runserver localhost:3000
```

<hr />

## Stack

* Postgresql
* Django
* TailwindCSS

<hr />

## About Me

- Author - [Carlos Córdova](https://me.carlosc.dev)
- Linkedin - [@carloscdev](https://www.linkedin.com/in/carloscdev/)
