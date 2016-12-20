helga-meet
==============

.. image:: https://badge.fury.io/py/helga-meet.png
    :target: https://badge.fury.io/py/helga-meet

.. image:: https://travis-ci.org/narfman0/helga-meet.png?branch=master
    :target: https://travis-ci.org/narfman0/helga-meet

System for asynchronous meetings e.g. standup

Installation
------------

Install via pip::

    pip install helga-meet

And add to settings!

Usage
-----

Schedule a daily standup at 3pm Mon-Fri, saying in room #general: "PSA @all"::

    !meet schedule standup "#general" "PSA @all" "hour 15 day_of_week 0-4"

Adds a status entry for the day for the user. Nick and time saved along with status::

    !meet status standup made widget1, started on widget2. will finish widget2, and no blockers

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

Release
-------

To publish your plugin to pypi, sdist and wheels are (registered,) created and uploaded with::

    make release

TODO
----

* Make queryable log with date or date range. Post to dpaste possibly.
* Ensure loading from cold start works, too!

License
-------

Copyright (c) 2016 Jon Robison

See LICENSE for details
