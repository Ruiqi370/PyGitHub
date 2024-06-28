from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("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")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()