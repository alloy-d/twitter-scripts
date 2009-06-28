#!/usr/bin/env python
# script to update cirquetidev on twitter with git commits

import sys

import git
import twitter

from credentials import *
api = twitter.Api(
    username=twitter_username,
    password=twitter_password
    )

repo_location = ".."

repo = git.Repo(repo_location)

oldrev = sys.argv[1]
newrev = sys.argv[2]

new_commits = repo.commits_between(oldrev, newrev)

for commit in new_commits:
    post = commit.summary + " ["
    post += str(commit.stats.total['lines']) + " lines"
    post += ' (+' + str(commit.stats.total['insertions'])
    post += '/-' + str(commit.stats.total['deletions']) + ") in "
    post += str(commit.stats.total['files']) + " file"
    if commit.stats.total['files'] > 1: post += "s"
    post += "]"

    api.PostUpdate(post)

