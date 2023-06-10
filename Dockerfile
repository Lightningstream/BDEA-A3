FROM neo4j
USER root
RUN apt-get update -y
RUN apt install python3 -y

COPY twitter_combined.txt ./twitter_combined.txt
COPY tweets.csv ./tweets.csv
COPY import.py ./import.py
RUN python3 import.py

COPY users.csv import/users.csv
COPY relations.csv import/relations.csv
 

