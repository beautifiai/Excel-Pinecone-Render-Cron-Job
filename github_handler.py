from github import Github
import base64

class GithubHandler:
    def __init__(self, repo_name, token):
        self.github = Github(token)
        self.repo = self.github.get_user().get_repo(repo_name)
        self.file_path = "data.xlsx"

    def get_previous_data(self):
        file_content = self.repo.get_contents(self.file_path)
        file_data = base64.b64decode(file_content.content)
        return pd.read_excel(io.BytesIO(file_data))

    def update_file(self, current_data):
        current_data.to_excel(self.file_path, index=False)
        with open(self.file_path, 'rb') as file:
            content = file.read()
        self.repo.update_file(self.file_path, "Update data", content, self.file_path)

