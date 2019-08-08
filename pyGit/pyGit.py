from github import Github


g = Github(base_url="https://theahmedjamal/api/v3", login_or_token="5586b32b70a86003c0399f48fdf9cec5ddead1f")

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))
