#!/usr/bin/env python
# script to update Twitter with git commits
#
# Copyright (C) 2009 Adam Lloyd <lloyda2 (at) rpi (dot) edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

