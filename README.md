# Table of Contents
1. [Aufgabenstellung](#Aufgabenstellung)
2. [OrdnerStruktur](#OrdnerStruktur)
2. [Implementierung](#Implementierung)
    1. [Server](#Server)
        1. [Requirements](#Requirements)
        2. [ServerStarten](#ServerStarten)
        3. [Erklärung](#CodeErklärung)
        4. [CMDBefehle](#Befehle)
        5. [Persistierung](#Persistierung)
        6. [Base-64Encoder](#Encoder)
3. [Quellen](#Quellen)
## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## OrdnerStruktur


```bash
├── sew5-simple-user-database-eecevit-tgm/
│   ├── docs
|   #wird nicht weiter verwendet
|
├── restful_userservice.egg-info
|   #wird nicht weiter verwendet
|   
├── src
|   ├── main
|   #in diesem Folder befindet sich der source code
|   |   ├── java
|   |   ├── python
|   |   ├── vue
|   ├── unittest
|   #in diesm Folder befinden sich die Tests
├── tox.ini
|   #für das automatisierte Testen
├── requiremets 
|   #beinhalten die Anfroderungen für das Tox - File
├── .travis.yml
|   #Travis file, damit Travis die Test durchführen kann
├── .gitignore
```

## Implementierung

## Server

### Requirements

* Implementierung
    * [Flask](#Flask)
    * [Python](#Python)
* Testing
    * [Tox](#Tox)
    * [PyTest](#)

#### ServerStarten
Der Server kann mit dem Befehl aus dem Hauptfolder gestartet werden
```bash
python src/main/python/server/server.py
```
Bei einem erfolgreichen Start sollte folgende Ausgabe kommen
```bash
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 276-721-881
```
Wenn es zu einer Fehlermeldung kommt, könnte es sein, dass der Port schon blockiert ist.
Um die IP-Adresse oder den Port ändern zu können muss im Code etwas bearbeitet werden. 
Hierführ muss in das Dokument [server.py](src/main/python/server/server.py) im Verzeichnis ```src/main/python/server/```

Dort muss auf Zeile 223 muss folgender Code hinzugefügt werden```host="...",port="..."```.   
```python
if __name__ == '__main__':                  if __name__ == '__main__':
    app.run(debug=True)                             app.run(debug=True,host="0.0.0.0",port="5005")
```
#### CodeErklärung
Der Coder wurde im File genau beschrieben und kommentiert. [server.py](src/main/python/server/server.py)


### Befehle
Es können nun folgende Befehle über die CMD ausgeführt werden
```bash
curl http://localhost:5000/user
# listet alle User

curl http://localhost:5000/user/<username>
#listet einen bestimmten User

curl http://localhost:5000/user/<username> -X DELETE -v
#löscht einen bestimmten User

curl http://localhost:5000/user/<username> -d "username=newName" -d "email=mail@mail.com" -d "eecevit.jpg" -X PUT -v
#ändert die Werte zu einem bestimmten User

curl http://localhost:5000/user -d "username=newName" -d"email=mail@mail.com" -d"eecevit.jpg" -X POST -v
#erstellt einen neuen User
```
### Persistierung
Damit alles Persistiert werden kann, wurde ein [user.json](src/main/python/server/user.json) File erstell. Hier werden alle User in einem JSON-Format abgespeichert.\
Um CRUD Befehle auf die User im [user.json](src/main/python/server/user.json) ausführen zu können wurde das File [jreader.py](src/main/python/server/jreader.py) erstellt.

### Encoder
Damit uUser auch ein Profilbild haben können, wurde eine Encoder [encoder.py](src/main/python/server/encoder.py) geschrieben, welcher ein Bild in base64 encoded.

Für die Dokumentierung wurde Sphinx verwendet.

## Quellen
[Python](https://docs.python.org/3/)

[Flask](http://flask.pocoo.org/docs/1.0/quickstart/)

[Flask-Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

[Sphinx](http://www.sphinx-doc.org/en/master/)

