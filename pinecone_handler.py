import pinecone

class PineconeHandler:
    def __init__(self, pinecone_key):
        pinecone.init(api_key=pinecone_key)
        self.index_name = "my-vector-index"
        if self.index_name not in pinecone.list_indexes():
            pinecone.create_index(name=self.index_name, metric="cosine", shards=1)
        self.index = pinecone.Index(index_name=self.index_name)

    def insert_document(self, namespace, embedding):
        self.index.upsert(items={namespace: embedding})

    def remove_document(self, namespace):
        self.index.delete(items=[namespace])


