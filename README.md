# PYTHON FLASK WITH NGINX & UWSGI: RURALL WEB APP ASSIGNMENT

## CONTENUTO

1. WebApp Folder
2. webapp_config
3. webapp.service

## USAGE

1. WebApp Folder - Contiene tutti i sorgenti della web app che va inizializzata tramite virtual environment e le librerie presenti nel file `requirements.txt`.
2. webapp_config - Contiene la configurazione nginx per per esporre la web app sul server di riferimento.
3. webapp.service - Unit file linux usato da systemd per far sì che la web app riparta in caso di crash e al boot del server.

## PREREQUISITI

1. Clonare questo repository.
2. Una distro Linux Debian based, con i privilegi di superuser `sudo`. Io ho usato un'istanza del catalogo AMI in AWS (che ahimè, ho dovuto spegnere $$$).
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
### INSTALLAZIONE

1. Installare l'app come servizio linux e abilitare il servizio:

	```
    cp webapp.service /etc/systemd/system/
	sudo systemctl start webapp.service
	sudo systemctl enable webapp.service
    ```
Se lanciata correttamente, il modulo uwsgi crea un file .socket al path indicato nel file uwsgi.ini (socket =/tmp/rurall-assign.sock)

### DEPLOY
A questo punto è possibile usare nginx come reverse proxy per ridirigere le request arrivate su una certa porta al file socket creato al punto precedente.

1. Registrare file di configurazione per il binding di nginx su una specifica interfaccia di rete e porta
	
	```
    cp webapp_config /etc/nginx/sites-available
	ln -s /etc/nginx/sites-available/webapp_config /etc/nginx/sites-enable/webapp_config
	sudo nginx -s reload
    ```

Per controllare che nginx sia in ascolto sull'interfaccia:porta attesa usare il comando netstat.

La procedura di installazione e deploy è quasi uno standard, tuttavia potrebbero esserci delle modifiche da apportare ai file .service o allo stesso uwsgi.ini che potrebbero essere diverse da macchina a macchina.

### DEPLOY ON LOCALHOST
Per mettere in esecuzione e far sì che anche tutti i file statici (css, js, etc.) siano correttamenti caricati nel browser, consiglio l'esecuzione in localhost.
1. Spostarsi all'interno della directory WebApp/app e dare comando:
 - Windows
	```
    env\Scripts\activate
	flask run
	```
 - Linux
 	```
    source env/Scripts/activate
	flask run
	```
	
La web app verrà messa in esecuzione sul localhost alla porta 5000, default di Flask.