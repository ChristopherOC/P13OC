.. ReadTheDocsOCLettings documentation master file, created by
   sphinx-quickstart on Fri Feb  2 12:47:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Voici la documentation officielle de OC-Lettings.
=================================================


.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. contents:: Index

Introduction
============
Ceci est une version améliorée de l'application OC-Lettings.
Les améliorations apportées sont :
   - Une amélioration du code et un respect des bonnes pratiques avec l'implémentation d'une architecture modulaire.
   - **Sentry** Implémentation de la journalisation de l'application avec Sentry.
   - **CircleCI** Mise en place d'un pipeline CI/CD.
   - **Heroku** Le déploiement de l'application sur Heroku



Installation :
==============

Prérequis
_________
- Python 3.9 (au minimum)
- Un IDE de votre choix
- Un compte GitHub
- Installer GIT CLI

Créez un environnement virtuel Python :

.. code-block:: shell

   python -m venv env


Activez l'environnement virtuel :
**Windows**

.. code-block:: shell
   
   env/scripts/activate

**Linux et MacOS**

.. code-block:: shell

   source env/bin/activate

Clonez le répertoire GitHub:

.. code-block:: shell

   git clone https://github.com/ChristopherOC/P13OC.git


Lancement du serveur:
_____________________

Pout lancer le serveur de l'application localement :

.. code-block:: shell

   cd Python-OC-Lettings-FR


Installez ensuite les dépendances nécessaires au bon fonctionnement de celui-ci :

.. code-block:: shell

   pip install -r requirements.txt


Lancez ensuite le serveur localement :

.. code-block::  shell

   python manage.py runserver


Si vous souhaitez accéder au Panneau Administrateur, accédez à l'url suivante:

.. code-block:: shell
   
   http://localhost:8000/admin

Les identifiants pour se connecter sont les suivants:

Identifiant : Admin

Mot de passe : Abc1234!

Vérification du Linting
=======================

Pour vérifier que le code respecte les bonnes pratiques et la nomenclature, utilisez la commande suivante.
Celle-ci effectuera des vérifications telles que l'utilisation des imports ou encore la longueur des lignes.

.. code-block:: shell

   ruff check .


Lancement des tests
===================

Pour lancer les tests et voir la couverture de ceux-ci sur l'ensemble du code nous utiliserons Pytest et Coverage.

Pour les tests, utilisez la commande suivante:
______________________________________________

.. code-block:: shell

   pytest -v


Pour voir la couverture des tests, utilisez la commande suivante:
_________________________________________________________________

.. code-block:: shell

   coverage run -m pytest


Puis pour générer le raport montrant le pourcentage de la couverture:

.. code-block:: shell

   coverage report


Pour accéder à la journalisation:
_________________________________

Connezctez-vous à votre compte Sentry, récupérez votre clef DSN puis dans le fichier ``settings.py`` saisissez-la dans la fonction suivante:

.. code-block:: shell

   sentry_sdk.init(sdn="Votre_clef")
   

Maintenant vous devriez avoir accès à la journalisation de votre application et d'y voir toute les erreurs levées.

Déploiement et intégration continue
===================================

Prérequis:
__________

Pour que tout puisse fonctionner, il est nécessaire d'avoir :

- Un compte GitHub
- Un compte Docker
- Un compte CircleCI
- Un compte Heroku

Le déploiement automatique s'effectue lorsque l'utilisateur "push" l'application vers GitHub.
Lorsque le "push" s'effectue sur la branche "Master", le linting et les tests sont lancés automatiquements.
Si l'un des deux ne réussit pas, alors le déploiement ne fonctionnera pas.
Si ceux-ci sont passés sans encombre alors le déploiement s'effectue.

Configuration:
______________

Il est nécessaire d'utiliser les variables d'environnement afin de garantir la sécurité et la confidentialité de l'application.
Pour cela, rendez-vous sur CircleCI puis dans "Project Settings" et "Environment Variables" afin de créer les varibales suivantes avec vos informations:

DOCKER_USERNAME : Votre username Docker

DOCKER_PASSWORD : Votre mot de passe Docker

HEROKU_APP_NAME : Le nom de votre application sur Heroku

HEROKU_KEY : Votre clé d'API Heroku

Lien de l'application en ligne :

.. code-block:: shell

   https://lettingsheroku-ff8587e22918.herokuapp.com/


A chaque "push" sur GitHub, le pipeline effectuera donc les tests et le linting.
Pour les ajuster, rendez-vous dans le fichier ``config.yml``.





Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
