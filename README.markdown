What is this?
=============

This is a collection of scripts I've written to do cool and unusual (well,
I think so, anyway) things with Twitter.


tweet_my_dot_plan.py
--------------------

A Python script to tweet the contents of your `.plan` file whenever you
update it. It uses the credentials found in the file `credentials.py` (of
which a sample is provided), currently expected to be in the same
directory, for the Twitter account.

Its requirements are the git version of `pyinotify`, found
[here](http://trac.dbzteam.org/pyinotify/wiki), and `python-twitter`,
available [here](http://code.google.com/p/python-twitter).

To use it, simply run it (preferably in the background, since it doesn't
daemonize itself yet):
`python tweet_my_dot_plan.py &`


git-hooks
---------

Several Python scripts for updating Twitter with git commits. There is
a `post-commit` script, which posts each commit to Twitter as it
happens, and a `post-receive` script, which posts commits to Twitter
after receiving them (via a `push`, for example).

Their requirements are [GitPython](http://gitorious.org/git-python)
and [python-twitter](http://code.google.com/p/python-twitter).

Sample hooks are provided which demonstrate how to use the scripts;
they and the Python files should be placed in the `.git/hooks`
directory of your repository.
