from utils.db_mongo import mongo_db
from utils.db_neo4j import neo4j_db

def sync_books():
    books = mongo_db.books.find()
    for book in books:
        query = """
        MERGE (b:Book {id: $id})
        SET b.title = $title, b.author_id = $author_id
        """
        parameters = {
            'id': str(book['_id']),
            'title': book['title'],
            'author_id': book['author_id']
        }
        neo4j_db.query(query, parameters)
