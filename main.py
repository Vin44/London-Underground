import os
from neo4j import GraphDatabase
from dotenv import load_dotenv


load_dotenv()

url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(url, auth=(username, password))

def find_shortest_path(tx, start, end, time_property="unimp_time"):
    """
    Finds the shortest path between two stations based on the given time property.
    """
    query = f"""
    MATCH (start:Station {{name: $start}}), (end:Station {{name: $end}})
    MATCH path = shortestPath((start)-[:CONNECTED*]-(end))
    WITH path,
         REDUCE(total=0, r IN relationships(path) | total + COALESCE(r.{time_property}, 999999)) AS totalTime
    RETURN [n IN nodes(path) | n.name] AS stations, totalTime
    """
    result = tx.run(query, start=start, end=end)
    return result.single()

def main():
    start = input("What is the Starting Station: ")
    end = input("What in the Ending Station: ")
    time_property = "unimp_time"

    with driver.session() as session:
        result = session.read_transaction(find_shortest_path, start, end, time_property)

        if result:
            stations, total_time = result["stations"], result["totalTime"]
            print(f"\nFastest route from {start} to {end} ({time_property}):")
            print(" -> ".join(stations))
            print(f"Total Travel Time: {total_time} seconds")
        else:
            print("No path found between the given stations.")


if __name__ == "__main__":
    main()
    driver.close()