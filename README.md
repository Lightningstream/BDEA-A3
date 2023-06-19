# Installation
```
docker compose up
```

Warten, bis der Cluster vollständig gestartet ist (Alle Knoten müssen 'Started' sein).

```
docker exec -it core1 chmod -R 777 import
```

Auf dem Jupyter-Notebook befinden sich alle Queries und Imports.

`localhost:8888` aufrufen und das Neo4j Import and Queries.ipynb öffnen

Für Visualisierungen können auch die Web GUIs verwendet werden.

`localhost:7474`
-> neo4j Web GUI core1

`localhost:7475`
-> neo4j Web GUI core2

`localhost:7476`
-> neo4j Web GUI core3

