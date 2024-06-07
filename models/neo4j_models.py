from neo4j import GraphDatabase
from config import Config

class Neo4jConnection:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            Config.NEO4J_URI, 
            auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None, **kwargs):
        with self.driver.session() as session:
            result = session.run(query, parameters, **kwargs)
            return [record for record in result]
