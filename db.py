from neo4j import GraphDatabase, basic_auth

def dbResult(query):

    try:
        driver = GraphDatabase.driver(
        "neo4j://localhost:11003",
        auth=basic_auth("user", "123"))


        with driver.session(database="neo4j") as session:
            results = session.read_transaction(
                lambda tx: tx.run(query).data())
        driver.close()

        return results
    except:
        print("Truy vấn lỗi")

def dbResultParam(query, param):

    try:
        driver = GraphDatabase.driver(
        "neo4j://localhost:11003",
        auth=basic_auth("user", "123"))


        with driver.session(database="neo4j") as session:
            results = session.read_transaction(
                lambda tx: tx.run(query, param=param).data())
        driver.close()

        return results
    except:
        print("Truy vấn lỗi")

