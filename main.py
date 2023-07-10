import os
from excel_handler import ExcelHandler
from pinecone_handler import PineconeHandler
from github_handler import GithubHandler
from embedding_handler import EmbeddingHandler

def main():
    # Obtain necessary keys and URLs from environment variables
    excel_url = os.getenv('EXCEL_URL')
    pinecone_key = os.getenv('PINECONE_KEY')
    openai_key = os.getenv('OPENAI_KEY')
    github_token = os.getenv('GITHUB_TOKEN')

    # Initialize handlers
    excel_handler = ExcelHandler(excel_url)
    pinecone_handler = PineconeHandler(pinecone_key)
    github_handler = GithubHandler(github_token, "beautifiai", "Excel-Scraper")
    embedding_handler = EmbeddingHandler(openai_key)

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
