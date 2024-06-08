from neo4j import GraphDatabase

class Neo4jDB:
    def __init__(self):
        self.driver = GraphDatabase.driver('bolt://3.84.16.168:7687', auth=("neo4j", "tempers-additive-retention"))

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

neo4j_db = Neo4jDB()