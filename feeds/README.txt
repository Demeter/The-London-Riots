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

