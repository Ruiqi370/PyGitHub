from PyGitHub import g

# for repo in g.get_user().get_repos():
#     print(repo.name)
#     repo.edit(has_wiki=False)
#     # to see all the available attributes and methods
#     print(dir(repo))
#
# g.close()
# import time
# from PyGitHub import g
#
# repositories = g.search_repositories(query='language:python')
# for repo in repositories:
#     print(repo)
#     time.sleep(2)  # delay for 2 seconds
#
#
# repositories = g.search_repositories(query='good-first-issues:>3')
# for repo in repositories:
#    print(repo)
#    time.sleep(2)  # delay for 2 seconds
import time
from PyGitHub import g

cnt=0
max_repos=100

repositories = g.search_repositories(query='language:python')
for repo in repositories:
    if cnt >= max_repos:
       break
    print(repo)
    cnt+=1
    time.sleep(1)  # delay for 2 seconds