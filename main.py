import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
from src.shortest_path import find_shortest_path
from src.time.time_range import get_value_by_time

load_dotenv()

url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(url, auth=(username, password))


def main():
    start = input("What is the Starting Station: ").upper()
    end = input("What in the Ending Station: ").upper()
    # print("what is the Time Property:")
    # print("1. Unimpeded Time")
    # print("2. AM Peak Time")
    # print("3. Inter Peak Time")

    choose = get_value_by_time()
    if choose == 1:
        time_property = "am_peak_time"
    elif choose == 2:
        time_property = "inter_peak_time"
    elif choose == 3:
        time_property = "unimp_time"

    print(start, end)

    with driver.session() as session:
        result = session.read_transaction(find_shortest_path, start, end, time_property)

        if result:
            stations, total_time, unimp_time = result["stations"], result["totalTime"], result["unimpTime"]
            print(f"\nFastest route from {start} to {end} ({time_property}):")
            print(" -> ".join(stations))

            print(F"Total Travel Time(unimp_time): {unimp_time} seconds")
            print(f"Total Travel Time({time_property}): {total_time} seconds")
        else:
            print("No path found between the given stations.")


if __name__ == "__main__":
    main()
    driver.close()