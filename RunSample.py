from PyGitHub import g

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     repo.edit(has_wiki=False)
#     # to see all the available attributes and methods
#     print(dir(repo))
#
# g.close()

repositories = g.search_repositories(query='language:python')
for repo in repositories:
    print(repo)

repositories = g.search_repositories(query='good-first-issues:>3')
for repo in repositories:
   print(repo)