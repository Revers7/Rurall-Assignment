# PYTHON FLASK WITH NGINX & UWSGI: RURALL WEB APP ASSIGNMENT

## CONTENTS

1. WebApp Folder
2. webapp_config
3. webapp.service

## USAGE

1. WebApp Folder - Contiene tutti i sorgenti della web app che va inizializzata tramite virtual environment e le librerie presenti nel file `requirements.txt`.
2. webapp_config - Contiene la configurazione nginx per per esporre la web app sul server di riferimento.
3. webapp.service - Unit file linux usato da systemd per far sì che la web app riparta in caso di crash e al boot del server.

## PREREQUISITES

1. Clonare questo repository.
2. Una distro Linux Debian based, con i privilegi di superuser `sudo`. Io ho usato un'istanza xxxxxx del catalogo AMI in AWS.
3. Installare i seguenti pacchetti:

    ```
    sudo apt-get update
    sudo apt-get install python3 python3-pip
    sudo apt-get install systemd nginx
    sudo pip3 install virtualenv
    ```

4. Inizializzare virtual environment del progetto:

    ```
    cd PATH_TO/WebApp
    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ```
