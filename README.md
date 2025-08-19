# London Underground

This system allows people to Input two London Underground Stations as the starting point and the end point. Then the system calculates the shortest path between those stations and the total travel time. 

I used data from the [Station to Station Journey Times - WhatDoTheyKnow](https://www.whatdotheyknow.com/request/station_to_station_journey_times). (The xls file is available in the repo.)

Used Neo4J' official docker image to create a Graph DataBase and placed train stations as nodes and travel times as edges. You can refer the Neo4J's documentations and docker Image [here](https://hub.docker.com/_/neo4j).

## How to run the Programme

First, clone the repo into a new working directory.

Then create a folder called 'data'. This step is important. 
This is where your graph database gonna be saved locally.

Then download and build the docker image for the Neo4J. When building make sure to create a password for the Neo4J.

```
docker run --restart always --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=neo4j/<your-password-here> --volume="C:\Users\VininduW\Desktop\LEARNS\knowlage_graphs_for_rag:/data" neo4j:latest
```

You only need to build this image once. If you wanna re-run the programme simply run the docker start command.

```bash
docker start <container_id>
```

Then create a `.env` file and make sure to add the following variables.

`NEO4J_URI=bolt://localhost:7687` Keep this as it is.
\
`NEO4J_USER=neo4j`\
`NEO4J_PASSWORD=<your-password>`

All set, Simply run the `create_knowledge_graph.py`. After creating you can visualize the graph db in the [http://localhost:7474/](http://localhost:7474/). 
(Make sure that the docker image is throughout this whole proccess.)

Then run the `main.py` and when you enter the starting and ending stations make sure type it in all caps. 


