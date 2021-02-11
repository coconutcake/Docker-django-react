<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="http://mign.pl/adds/logo.png" alt="Project logo"></a>
</p>

<h3 align="center">DjangoDocker</h3>

<div align="center">

[![Staus](https://img.shields.io/travis/coconutcake/DjangoDocker)](https://travis-ci.org/github/coconutcake/DjangoDocker)
[![Size](https://img.shields.io/github/repo-size/coconutcake/DjangoDocker?style=flat-square)]()
[![Dependencies](https://img.shields.io/requires/github/coconutcake/DjangoDocker)](https://requires.io/github/coconutcake/DjangoDocker/requirements/?branch=main)


</div>

---

<p align="center"> Save a time preparing app. Use ready to use template!
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)



## 🧐 About <a name = "about"></a>

This complete package includes all You need to start making django app on docker containers saving Your time for preparations. With one command, You can start the whole stack using Docker Composer which includes:
- Python 3.8 slim machine container with Django version 3.1.2 (prepared for handling with postgresql)
- Postgresql container version 12
- Adminer container for handling postgresql
- Nginx for handling upstream Django with reverse proxy and ssl server

## 🏁 Getting Started <a name = "getting_started"></a>

The first thing You wanted to check before You can move further is Docker. In case You havent downloaded yet, please choose Your appriopriate platform and download docker [here](https://www.docker.com/get-started). Make sure, You also have the latest git version installed as well.

### Installing

After docker engine installation, clone the current repository:
```
git clone https://github.com/coconutcake/DjangoDocker.git
```

## 🚀 Deployment <a name = "deployment"></a>

Simply run from main directory:

```
docker-compose up --build
```
in order to build all required Dockerfiles and launch the stack. 
Thats all! 
Your services are running now and You can check their availability:

- Django -> [http://127.0.0.1:8833](http://127.0.0.1:8833) - Accept self-signed ssl certificate here to redirect to HTTPS
- Adminer -> [http://127.0.0.1:8080](http://127.0.0.1:8080)