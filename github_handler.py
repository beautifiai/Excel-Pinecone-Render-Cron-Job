import os
from github import Github
import base64

class GithubHandler:
    def __init__(self, repository_name):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.repository_name = repository_name

        # Initialize GitHub client
        self.client = Github(self.github_token)
        self.repo = self.client.get_user().get_repo(self.repository_name)

    def get_previous_data(self):
        """
        Fetches the previous version of the Excel file from the GitHub repository,
        decodes it, and returns it as a pandas DataFrame.
        """
        contents = self.repo.get_contents("data.xlsx")
        decoded_contents = base64.b64decode(contents.content)
        data = pd.read_excel(io.BytesIO(decoded_contents), header=None)
        data_dict = data.set_index(0).T.to_dict('list')
        return data_dict

    def update_file(self, data):
        """
        Writes the updated data to the Excel file and pushes it to the GitHub repository.
        """
        # Write data to Excel file
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_excel('data.xlsx', index=False)

        # Read the updated file as bytes
        with open('data.xlsx', 'rb') as file:
            content = file.read()

        # Update the file in the repository
        self.repo.update_file("data.xlsx", "Update data", content, self.repo.get_contents("data.xlsx").sha)
