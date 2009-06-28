#!/usr/bin/env python
# script to update cirquetidev on twitter with git commits

import git
import twitter

from credentials import *
api = twitter.Api(
    username=twitter_username,
    password=twitter_password
    )

repo_location = ".."

repo = git.Repo(repo_location)
head = repo.heads[0]
last_commit = head.commit

post = last_commit.summary + " ["
post += str(last_commit.stats.total['lines']) + " lines"
post += ' (+' + str(last_commit.stats.total['insertions'])
post += '/-' + str(last_commit.stats.total['deletions']) + ") in "
post += str(last_commit.stats.total['files']) + " file"
if last_commit.stats.total['files'] > 1: post += "s"
post += "]"

api.PostUpdate(post)

