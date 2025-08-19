def find_shortest_path(tx, start, end, time_property):
    """
    Finds the shortest path between two stations based on the given time property.
    """
    query = f"""
    MATCH (start:Station {{name: $start}}), (end:Station {{name: $end}})
    MATCH path = shortestPath((start)-[:CONNECTED*]-(end))
    WITH path,
         REDUCE(total=0, r IN relationships(path) | total + COALESCE(r.{time_property}, 999999)) AS totalTime,
         REDUCE(unimp=0, r IN relationships(path) | unimp + COALESCE(r.unimp_time, 999999)) AS unimpTime
    RETURN [n IN nodes(path) | n.name] AS stations, totalTime, unimpTime
    """
    result = tx.run(query, start=start, end=end)
    return result.single()