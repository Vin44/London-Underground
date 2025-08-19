from src.data_ret import get_cleaned_data
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

filename = "Inter_Station_Train_Times.xls"

stations, unimpeded_times, am_time, inter_peaked_time = get_cleaned_data(filename)
print(f"Station Pairs: {len(stations)}")
print(f"Unimpeded Time Edges: {len(unimpeded_times)}")
print(f"AM Time Edges: {len(am_time)}")
print(f"Inter Peaked Time Edges: {len(inter_peaked_time)}")

if len(stations)*3 == len(unimpeded_times)+len(am_time)+len(inter_peaked_time): 

    load_dotenv()

    url = os.getenv("NEO4J_URI")
    username = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")

    driver = GraphDatabase.driver(url, auth=(username, password))

    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    def create_station_graph(tx, pairs, unimpended_times, am_time, inter_peaked_time):
        for (start, end), unimp_time, am_peak_time, inter_peak_time in zip(pairs, unimpended_times, am_time, inter_peaked_time):
            tx.run("""
                MERGE (s1:Station {name: $start})   
                MERGE (s2:Station {name: $end})
                MERGE (s1)-[r:CONNECTED]->(s2)
                SET r.unimp_time = $unimp_time,
                r.am_peak_time = $am_peak_time,
                r.inter_peak_time = $inter_peak_time
            """, start=start, end=end, unimp_time=unimp_time, am_peak_time = am_peak_time, inter_peak_time=inter_peak_time )

    with driver.session() as session:
        session.execute_write(create_station_graph, stations, unimpeded_times, am_time, inter_peaked_time)

    print("Graph Created Successfully!")
    driver.close()

else:
    print("There is a issue when extarcting data.")