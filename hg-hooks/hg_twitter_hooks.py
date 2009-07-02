import twitter

twitter_username = 'cirquetidev'
twitter_password = '********'

def incoming(ui, repo, node, **kwargs):
    twitter_api = twitter.Api(
        username=twitter_username,
        password=twitter_password,
        )

    changeset = repo.changectx(node)
    
    description = changeset.description()
    description_summary = description.splitlines()[0]

    changed_files = len(changeset.files())

    update_text = "{0} [{1} changed]".format(
        description_summary,
        changed_files,
        )

    twitter_api.PostUpdate(update_text)
    return False
