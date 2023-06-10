```
docker compose build
```
```
docker compose up
```
```
docker exec -it graph_db sh bin/neo4j-admin database import full --nodes=import/users.csv --relationships=import/relations.csv --overwrite-destination neo4j 
```
localhost:8888
-> ipynb