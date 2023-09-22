## LITReview - Application Web pour les lecteurs

### Auteur : Nicolas Sylvestre

### Contact : sylvestrenicolas@sfr.fr

## Introduction
Cette application web a pour objectif de réunir des lecteurs qui souhaitent partager et demander leurs opinions sur des livres ou des articles.   

## Contenu du site web.
LITReview est une application web conçue pour rassembler les amateurs de lecture, leur permettant de partager  
et de solliciter des avis sur des livres et des articles. Elle offre une plateforme conviviale pour les lecteurs  
qui souhaitent s'engager dans des discussions littéraires, demander des critiques et partager leurs propres opinions.


## L'application LITReview offre les fonctionnalités suivantes.
- Page de connexion et d'inscription
- Réinitialisation de mot de passe en cas de difficultés
- Abonnement et désabonnement aux autres lecteurs en fonction des préférences
- Demande de critique pour obtenir l'avis des lecteurs
- Création de critiques permettant aux lecteurs de partager leurs avis sur un livre ou un article
- Réponse aux demandes de critiques
- Modification et suppression de critiques ou de tickets

## Installation de Python.
**Information importante ! Pour un bon fonctionnement de l'application, il est recommandé de télécharger et d'installer  
la version la plus récente de Python.**
- Comment installez Python sous Windows ou Mac / Linux, cliquez sur le lien suivant >> [Comment installer Python](https://fr.wikihow.com/installer-Python)
- Télécharger la dernière version de Python (Windows, Mac / Linux) en cliquant sur le lien suivant >> [Télécharger Python](https://www.python.org/downloads/) 

## Téléchargement de l'application.
 - Cliquez sur le lien suivant pour procéder au téléchargement de l'application >> [Application Web LITReview](https://github.com/Nico13118/Projet9_V2/archive/refs/heads/master.zip)

# Pour un paramétrage Windows, suivre les indications ci-dessous.  
## Accédez aux téléchargements.
- Ouvrez l'Explorateur de fichiers en appuyant sur la touche **<< "Windows" + "E" >>** ou en cliquant sur l'icône de dossier  
dans la barre des tâches.
- Dans l'Explorateur de fichiers, vous verrez une option appelée **<< "Téléchargements" >>** dans le volet gauche,  
sous **<< "Ce PC" >>** ou **<< "Ordinateur" >>**. Cliquez sur **<< "Téléchargements" >>** pour ouvrir ce dossier.

## Décompressez l'application.
- Faites un clic droit sur le fichier **<< "Projet9_V2-master.zip" >>**. 
- Sélectionnez l'option **<< "Extraire tout..." >>**.
- Dans la fenêtre **<< "Assistant Extraction de fichiers" >>**, cliquez sur le bouton **<< "Parcourir ..." >>**, puis sélectionnez  
le bureau comme destination.
- Cliquez ensuite sur le bouton **<< "Extraire" >>** pour démarrer le processus de décompression.
- Une fois la décompression terminée, vous trouverez sur votre bureau un répertoire nommé **<< "Projet9_V2-master" >>**.

## Ouverture de PowerShell.
- Option 1 : Saisissez dans la barre de recherche **<< "Windows Powershell" >>** sélectionnez-le et appuyez sur **<< "Entrée" >>**.
- Option 2 : Ouvrir la fenêtre **<< "Exécuter" >>** - Touche raccourci clavier **<< Win + R >>** puis saisir **<< "powershell" >>** et appuyer sur **<< "Entrée" >>**.

## Création d'un environnement virtuel.
**Information importante ! Une fois l'environnement virtuel crée, il n'est plus necéssaire de le recréer à chaque utilisation.**
- Saisissez les lignes de commandes suivantes :

```sh
cd Desktop\Projet9_V2-master   
   ```
```sh
python -m venv env   
   ```

## Activation de l'environnement virtuel.
**Information importante ! Pour un bon fonctionnement de l'application, il est impératif de procéder  
à la réactivation de votre environnement virtuel après chaque fermeture / ouverture de PowerShell.**

- Saisissez la ligne de commande suivante :

```sh
env\Scripts\Activate.ps1
   ```

## Installation du gestionnaire de packages (pip).
- Saisissez la ligne de commande suivante :

```sh
python -m pip install --upgrade pip
   ```

## Installation des packages Python (requirements.txt).
**Information importante ! Après avoir effectué cette installation, il n'est plus nécessaire de la répéter.** 
- Saisissez la ligne de commande suivante :

```sh
pip install -r requirements.txt
   ```

## Exécution du serveur d'application.
- Saisissez les lignes de commandes suivantes :

```sh
cd LITReview
   ```

```sh
python manage.py runserver
   ```

## Accédez à l'application Web.
- Pour accéder à l'application web, procédez à l'ouverture de votre navigateur puis copier / coller  
le lien suivant : http://127.0.0.1:8000/login/

## Recommandations.
- Pour garantir la stabilité, la sécurité et les performances de votre enrironement Python et de votre application, nous  
recommandons de mettre à jour régulièrement le gestionnaire de packages (pip). 
- Pour pouvoir mettre à jour le gestionnaire de packages (pip), vous devez arrêter dans un premier temps le serveur  
d'application.

## Arret du serveur d'application. 
- Pour arrêter le serveur d'application, appuyez sur les touches de votre clavier :  

```sh
Ctrl + C
   ```

## Mise à jour du gestionnaire de packages (pip).
- Pour mettre à jour le gestionnaire de packages (pip), positionnez l'invite de commande dans le répertoire  
**<< "Projet9_V2-master" >>** en saisissant la ligne de commande ci-dessous.  

```sh
cd ..
   ```
- Puis saisir :
```sh
python -m pip install --upgrade pip 
   ```


## Redémarrer le serveur d'application.
- Pour redémarrer le serveur d'application, positionnez l'invite de commande dans le répertoire **<< "LITReview" >>**  
en saisissant la ligne de commande ci-dessous.  

```sh
cd LITReview
   ```
- Puis :
```sh
python manage.py runserver
   ```

- Pour que votre application puisse fonctionner, vous devez maintenir PowerShell ouvert. 
- En cas de fermeture accidentelle ou intentionnelle de votre invite de commande, procédez à sa réouverture,  
réactivez l'environnement virtuel, puis relancez le serveur d'application en utilisant les lignes de commandes ci-dessous.

```sh
cd Desktop\Projet9_V2-master
   ```

```sh
env\Scripts\Activate.ps1
   ```

```sh
cd litreview
   ```
```sh
python manage.py runserver
   ```


# Pour un paramétrage Mac / Linux, suivre les indications ci-dessous.  
## Accédez aux téléchargements.
- Cliquez sur l'icône du Finder dans le Dock (la barre d'outils en bas de l'écran).
- Dans la fenêtre du Finder qui s'ouvre, vous verrez **<< "Téléchargements" >>** dans la liste des dossiers de gauche,  
cliquez sur **<< "Téléchargements" >>** pour ouvrir ce dossier.

## Décompressez l'application.
- Cliquez deux fois sur le fichier **<< "Projet9_V2-master.zip" >>**, le répertoire décompressé apparaît sans l'extension **<< zip >>**.  
- Déplacez ensuite le répertoire **<< "Projet9_V2-master" >>** sur votre bureau.

## Ouverture du Terminal.
- Appuyez sur les touches **<< "Cmd (⌘) + Espace" >>** pour ouvrir **<< Spotlight >>**, puis commencez à taper **<< "Terminal" >>**.  
Lorsque **<< "Terminal" >>** apparaît dans les résultats des recherches, sélectionnez-le et appuyez sur **<< "Entrée" >>**.

## Création d'un environnement virtuel.
**Information importante ! Une fois l'environnement virtuel crée, il n'est plus necéssaire de le recréer à chaque utilisation.**
- Saisissez les lignes de commandes suivantes :

```sh
cd ~/Desktop/Projet9_V2-master   
   ```
```sh
python3 -m venv env   
   ```
   
## Activation de l'environnement virtuel.
**Information importante ! Pour un bon fonctionnement de l'application, il est impératif de procéder  
à la réactivation de votre environnement virtuel après chaque fermeture / ouverture du Terminal.**
- Saisissez la ligne de commande suivante :

```sh
env/bin/activate
   ```
## Installation du gestionnaire de packages (pip).
- Saisissez la ligne de commande suivante :

```sh
python3 -m pip install --upgrade pip
   ```

## Installation des packages Python (requirements.txt).
**Information importante ! Après avoir effectué cette installation, il n'est plus nécessaire de la répéter.** 
- Saisissez la ligne de commande suivante :
```sh
pip install -r requirements.txt
   ```

## Exécution du serveur d'application.
- Saisissez les lignes de commandes suivantes :

```sh
cd LITReview
   ```

```sh
python3 manage.py runserver
   ```

## Accédez à l'application Web.
- Pour accéder à l'application web, procédez à l'ouverture de votre navigateur puis copier / coller  
le lien suivant : http://127.0.0.1:8000/login/

## Recommandations.
- Pour garantir la stabilité, la sécurité et les performances de votre enrironement Python et de votre application, nous  
recommandons de mettre à jour régulièrement le gestionnaire de packages (pip). 
- Pour pouvoir mettre à jour le gestionnaire de packages (pip), vous devez arrêter dans un premier temps le serveur  
d'application.

## Arret du serveur d'application. 
- Pour arrêter le serveur d'application, appuyez sur les touches de votre clavier :

```sh
Cmd (⌘) + C
   ```

### Mise à jour du gestionnaire de packages (pip).
- Pour mettre à jour le gestionnaire de packages (pip), positionnez l'invite de commande dans le répertoire  
**<< "Projet9_V2-master" >>** en saisissant la ligne de commande ci-dessous.  

```sh
cd ..
   ```
- Puis :

```sh
python3 manage.py runserver
   ```

### Redémarrer le serveur d'application.
- Pour redémarrer le serveur d'application, positionnez l'invite de commande dans le répertoire **<< "LITReview" >>**  
en saisissant la ligne de commande ci-dessous.

```sh
cd LITReview
   ```
- Puis :
```sh
python3 manage.py runserver
   ```

- Pour que votre application puisse fonctionner, vous devez maintenir le Terminal ouvert. 
- En cas de fermeture accidentelle ou intentionnelle de votre invite de commande, procédez à sa réouverture,  
réactivez l'environnement virtuel, puis relancez le serveur d'application en utilisant les lignes de commandes ci-dessous.

```sh
cd ~/Desktop/Projet9_V2-master/
   ```

```sh
env/bin/activate
   ```
```sh
cd LITReview
   ```
```sh
python3 manage.py runserver
   ```

