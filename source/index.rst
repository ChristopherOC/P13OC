.. ReadTheDocsOCLettings documentation master file, created by
   sphinx-quickstart on Fri Feb  2 12:47:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ReadTheDocsOCLettings's documentation!
=================================================

Voici la documentation officielle de OC-Lettings.

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


Pout lancer le serveur de l'application localement :

.. code-block:: shell

   cd Python-OC-Lettings-FR


Installez ensuite les dépendances nécessaires au bon fonctionnement de celui-ci :

.. code-block:: shell

   pip install -r requirements.txt


Lancez ensuite le serveur localement :

.. code-block::  shell

   python manage.py runserver



Vérification du Linting
=======================

Pour vérifier que le code respecte les bonnes pratiques et la nomenclature, utilisez la commande suivante.
Celle-ci effectuera des vérifications telles que l'utilisation des imports ou encore la longueur des lignes.

.. code-block:: shell

   ruff check .



Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
