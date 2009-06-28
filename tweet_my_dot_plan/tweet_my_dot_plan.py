#!/usr/bin/env python
# tweet_my_dot_plan.py
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

import os
import pyinotify
import re
import sys
import twitter

from credentials import twitter_username, twitter_password

username = twitter_username
password = twitter_password

class DotPlanTweeter(pyinotify.ProcessEvent):
  def my_init(self, home_dir = os.environ.get("HOME"),
      twitter_api=twitter.Api(username, password)):
    """
    This is called automatically from ProcessEvent.__init__().
    Any extra arguments are passed to this function.
    """
    self._home_dir = home_dir
    self._twitter_api = twitter_api

  def process_IN_CLOSE_WRITE(self, event):
    dot_plan = open(self._home_dir + os.sep + '.plan', 'r')
    dot_plan_text = dot_plan.read()
    dot_plan_text = re.sub('\n', ' ', dot_plan_text)
    print(dot_plan_text)
    self._twitter_api.PostUpdate(dot_plan_text)

  def process_default(self, event):
    pass


home_dir = os.environ.get("HOME")

wm = pyinotify.WatchManager()
wm.watch_transient_file(home_dir + os.sep + '.plan', pyinotify.ALL_EVENTS,
    DotPlanTweeter)

notifier = pyinotify.Notifier(wm, DotPlanTweeter())
notifier.loop()

