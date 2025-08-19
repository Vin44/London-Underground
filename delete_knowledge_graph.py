import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

print("NEO4J_URI:", url)
print("NEO4J_USERNAME:", username)
print("NEO4J_PASSWORD:", password)

driver = GraphDatabase.driver(url, auth=(username, password))

with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")

print("Graph Deleted Successfully!")
driver.close()