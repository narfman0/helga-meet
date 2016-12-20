helga-meet
==============

.. image:: https://badge.fury.io/py/meet.png
    :target: https://badge.fury.io/py/meet

.. image:: https://travis-ci.org/narfman0/meet.png?branch=master
    :target: https://travis-ci.org/narfman0/meet

System for asynchronous meetings e.g. standup

Installation
------------

Install via pip::

    pip install helga-meet

And add to settings!

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

Usage
-----

    !meet help

License
-------

Copyright (c) 2016 Jon Robison

See LICENSE for details
