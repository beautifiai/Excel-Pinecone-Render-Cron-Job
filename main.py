import os
from excel_handler import ExcelHandler
from pinecone_handler import PineconeHandler
from github_handler import GithubHandler
from embedding_handler import EmbeddingHandler

def main():
    # Initialize handlers
    excel_handler = ExcelHandler("excel_handler.py")
    pinecone_handler = PineconeHandler("pinecone_handler.py")
    github_handler = GithubHandler("github_handler.py")
    embedding_handler = EmbeddingHandler("embedding_handler.py")

    # Get current and previous Excel data
    current_data = excel_handler.get_excel_data()
    previous_data = github_handler.get_previous_data()

    # Determine rows to add and remove
    to_add, to_remove = excel_handler.compare_data(current_data, previous_data)

    # Update Pinecone database
    for row in to_add:
        namespace, embedding_data = row[0], row[1:]
        embedding = embedding_handler.create_embedding(embedding_data)
        pinecone_handler.insert_document(namespace, embedding)
    for namespace in to_remove:
        pinecone_handler.remove_document(namespace)

    # Update Excel file in repository
    github_handler.update_file(current_data)

if __name__ == "__main__":
    main()
