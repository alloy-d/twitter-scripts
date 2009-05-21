What is this?
=============

This is a collection of scripts I've written to do cool and unusual (well,
I think so, anyway) things with Twitter.


tweet_my_dot_plan.py
--------------------

A Python script to tweet the contents of your `.plan` file whenever you
update it. It uses the credentials found in the file `credentials.py` (of
which a sample is provided) for the Twitter account.

It uses the git version of `pyinotify`, found
[here](http://trac.dbzteam.org/pyinotify/wiki), and `python-twitter`,
available [here](http://code.google.com/p/python-twitter).

To use it, simply run it (preferably in the background, since it doesn't
daemonize itself yet):
`python tweet_my_dot_plan.py &`

