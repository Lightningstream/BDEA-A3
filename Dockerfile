FROM neo4j

COPY users.csv import/users.csv
COPY relations.csv import/relations.csv

