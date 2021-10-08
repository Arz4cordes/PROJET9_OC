# PROJET9_OC
Projet Django: blog avec des demandes d'avis sur des livres
               et des réponses aux demandes,
               avec un système d'inscriptions d'utilisateurs
               et de gestion d'abonnements à des utilisateurs

1) Pour utiliser les programmes, installer un environnement virtuel Python,
    par exemple avec la commande python -m venv projet7 sous windows
2) Le fichier requirements.txt contient les bibliothèques à installer.
    pour utiliser les programmes.
3) Une fois Django installé, vous pouvez faire les migrations avec les    
    commandes suivantes depuis le dossier source LITReview:
    python manage.py makemigrations
    python manage.py migrate
    Cela mettra en place les tables de la base de donnée SQLLite
4) L'application comprend une interface d'administration, accessible        
    via l'URL http://127.0.0.1:8000/admin dans un navigateur web.
    Cette interface permet d'ajouter, de visualiser, de modifier et de supprimer des utilisateurs, des tickets et des critiques.
    Un administrateur (superuser) a déjà été crée, pour tests,
    avec les identifiants suivants:
    Nom: Armel
    Mot de passe: OCP9.dj2021
5) L'application se lance à partir de la page de connexion suivante:
    http://127.0.0.1:8000/login
    Cette page permet d'inscrire un nouvel utilisateur de l'application,
    ou bien de connecter un utilisateur déjà inscrit.
    Toutes les autres pages de l'application ne sont pas accessibles tant qu'un utilisateur authentifié n'est pas connecté.
