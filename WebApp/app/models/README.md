
# DATABASE SCHEMA: RURALL WEB APP ASSIGNMENT

Per l'implementazione del database si decide di utilizzare un database relazionale il cui schema descrive quelli che sono i requisiti richiesti dalla traccia.
 
## Requisiti
1. Storage of employees' information in a local database. 
This information will include at least the following: 
	 - first name 
	 - last name 
	 - username 
	 - email 
	 - gender 
	 - title 
	 - department 
  
2. Storage of at least one report per employee in a local database. 
This information will include at least the following: 
	 - Id 
	 - title 
	 - description 
	 - priority (two possible values: high, low) 

## Minimondo
Dai requisiti di cui sopra, si evince che lo scenario che si vuole modellare coinvolge due entità: **Employee** e **Report**.
Assumendo che tra queste due entità esista una relazione molti-molti ossia, un impiegato può essere associato a più report e un report può essere associato a più impiegati,
l'associazione (**charged**) tra le entità sarà anch'essa mappata in una tabella la cui chiave primaria è fornita dalla coppia delle chiavi primarie nelle tabelle employee e report.
Per quanto riguarda gli attributi delle entità coinvolte si è deciso di usare come chiave primaria per gli impiegati la email, in quanto quest'ultima è di sua natura univoca,
e per i report l'attributo id, che si assume essere un intero autoincrementato.

![Diagramma Entinty Relationship](ER-Diagram.pdf)

L'implementazione di tale schema in python è descritta nel file Models.py e si basa su SQLAlchemy, un ORM (Object Relational Mapper) per Python.
In particolare per questa web app basata su Flask, si è deciso di usare la libreria **Flask-SQLAlchemy** che permette una migliore integrazione SQL in Flask.

## Salvataggio
Il database creato verrà salvato in locale sulla macchina e, più precisamente, nel file **app.db**. 
Quest'ultimo è possibile aprirlo per consultarlo con qualsiasi tool di navigazione di database relazionali; personalmente utilizzo **DB Browser**.
