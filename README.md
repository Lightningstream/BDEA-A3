```
docker compose build
```
```
docker compose up
```
```
docker exec -it graph_db sh bin/neo4j-admin database import full --nodes=import/users.csv --relationships=import/follows.csv --overwrite-destination neo4j 
docker exec -it graph_db sh bin/neo4j-admin database import full --nodes=import/users.csv --relationships=import/follows.csv --overwrite-destination neo4j 
```
localhost:8888
-> ipynb