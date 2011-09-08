======================
 First Implementation
======================

For this first pass at data analysis, articles and exchange rate data will
be downloaded on three currency pairs: USD<->AUD, USD<->GBP, GBP<->AUD.

Feature Extraction
==================

The HTML of the articles will first be preprocessed to exclude all items
not in a <p> tag, and then to remove all HTML markup.

The text will have the named entities identified by the NLTK and then the
proper nouns counted. Only nouns appearing three or more times will
be retained.

The resulting word lists will represent a sparse feature matrix, and
unique words will be assigned dimensions. The currency pairs each also
represent one of three dimensions.

An article is assumed to affect average of the opening and closing
exchange rates of a currency pair the trading day following the
publication of the article, and the fractional increase over the previous
day's opening and closing price is used as the value of the feature matrix
for the SVR.

==============
 Feed Handler
==============

This package handles newsfeeds for a currency pair. It will check the feed
for new articles, and when found, it will pull the new articles and hand
them off to the feature extractor.

Package Dependencies
====================

This requires the `Universal Feed Parser`_, the `feed cache package`_, and
the `requests package`_.

.. _Universal Feed Parser: http://www.feedparser.org/
.. _feed cache package: http://www.doughellmann.com/articles/pythonmagazine/features/feedcache/
.. _requests package: http://pypi.python.org/pypi/requests

=================
 Getting Started
=================

Creating the virtualenv
-----------------------

First, download or install `virtualenv`_. This package can be used to
create isolated Python environments for working on a project without
affecting or being affected by an existing system python. It still
requires that Python be installed, but after that it keeps mostly
to itself.

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

Unpack that, and in the top directory there is a script called
virtualenv.py. We'll need to run that, but from the top of the londonriots
checkout

        python /path/to/virtualenv.py --no-site-packages dev.env

This will create a virtual environment in the directory "dev.env", and we
can use that for all of the development work, including installing
packages and running the components of londonriots itself.


Installing NLTK
---------------

NLTK (Natural Language Toolkit) will be used to extract useful words from the feeds in order to help us find patterns. This is can be installed with:

	./dev.env/bin/pip install http://nltk.googlecode.com/files/nltk-2.0.1rc1.tar.gz

Installing and setup of Postgres
--------------------------------

The easiest way to install Postgres is to use homebrew. You can find more information about it here: http://mxcl.github.com/homebrew/

Once, you have homebrew installed, Postgres installation is as easy as:

	brew install postgres

After the installation is complete, you have to run the following commands:

	initdb --username=postgres /usr/local/var/postgres
	mkdir -p ~/Library/LaunchAgents
	cp /usr/local/Cellar/postgresql/9.0.4/org.postgresql.postgres.plist ~/Library/LaunchAgents/
	launchctl load -w ~/Library/LaunchAgents/org.postgresql.postgres.plist
	createuser --createdb --encrypted --pwprompt --no-superuser --username=postgres --host=localhost devlondonriots
	createdb --host=localhost --username=devlondonriots devlondonriots

If it doesn't already exist, create /etc/sysctl.conf and put the following values in that file:

	kern.sysv.shmmax=64000000
	kern.sysv.shmmin=1
	kern.sysv.shmmni=256
	kern.sysv.shmseg=64
	kern.sysv.shmall=65536

These commands creates a database, a database user, an automatic launcher for postgres and sets the shared memory settings for postgres


Development Installation
------------------------

Next, we'll install the londonriots package in "development" mode, which
downloads and installs all of the external packages, and then adds
londonriots itself to the virtualenv for testing::

	./dev.env/bin/python setup.py develop

Running The Tests
-----------------

	./dev.en/bin/python setup.py test
