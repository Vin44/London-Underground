import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(url, auth=(username, password))

def create_graph(tx):
    tx.run("""
        CREATE (a:Person {name: 'Alice', age: 30})
        CREATE (b:Person {name: 'Bob', age: 25})
        CREATE (c:Person {name: 'Charlie', age: 35})
        CREATE (a)-[:FRIEND]->(b)
        CREATE (b)-[:FRIEND]->(c)
    """)

def query_friends(tx, name):
    result = tx.run("""
        MATCH (p:Person {name: $name})-[:FRIEND]->(friend)
        RETURN friend.name AS friend
    """, name=name)
    return [record["friend"] for record in result]

with driver.session() as session:
    # Create data
    session.execute_write(create_graph)

    # Query Alice’s friends
    friends = session.execute_read(query_friends, "Alice")
    print("Alice's friends:", friends)

driver.close()