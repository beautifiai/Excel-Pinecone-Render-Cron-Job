import os
import pinecone

class PineconeHandler:
    def __init__(self):
        self.pinecone_key = os.getenv('PINECONE_KEY')

        # Initialize Pinecone
        pinecone.init(api_key=self.pinecone_key)

    def insert_document(self, namespace, embedding):
        """
        Inserts a new document into the Pinecone database.
        """
        # Initialize the index with the namespace if it doesn't exist
        if namespace not in pinecone.list_indexes():
            pinecone.create_index(index_name=namespace, metric="cosine")

        # Switch to the namespace and insert the document
        pinecone.deactivate()
        pinecone.activate(index_name=namespace)
        pinecone.upsert(items={namespace: embedding})

    def remove_document(self, namespace):
        """
        Removes a document from the Pinecone database.
        """
        # Check if the namespace exists
        if namespace in pinecone.list_indexes():
            # Switch to the namespace and delete the document
            pinecone.deactivate()
            pinecone.activate(index_name=namespace)
            pinecone.delete(ids=[namespace])
