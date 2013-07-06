.. m209 documentation master file, created by
   sphinx-quickstart on Thu Jul  4 18:12:07 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to m209's documentation!
================================

:Author: Brian Neal <bgneal@gmail.com>
:Version: |release|
:Date: |today|
:Home Page: https://bitbucket.org/bgneal/m209/
:License: MIT License (see LICENSE.txt)
:Documentation: http://m209.readthedocs.org/
:Support: https://bitbucket.org/bgneal/m209/issues

Introduction
------------

``m209`` is a complete `M-209`_ simulation library and command-line application
written in Python 3. ``m209`` is historically accurate, meaning that it can
exchange messages with an actual M-209 cipher machine.

It is hoped that this library will be useful to M-209 enthusiasts, historians,
and students interested in cryptography.

``m209`` strives to be Pythonic, easy to use, and comes with both unit tests
and documentation. ``m209`` is a library for building applications for
encrypting and decrypting M-209 messages. ``m209`` also ships with a simple
command-line application that can encrypt & decrypt messages for scripting and
experimentation.

Documentation
-------------

Contents:

.. toctree::
   tutorial
   :maxdepth: 2


Requirements
------------

``m209`` is written in Python_, specifically Python 3.3. It has no other
requirements or dependencies.

Installation
------------

``m209`` is available on the `Python Package Index`_ (PyPI). You can install it
using pip_::

   $ pip install m209                  # install
   $ pip install --upgrade m209        # upgrade

You may also download a tarball or .zip file of the latest code by visiting the
Downloads tab on the `m209 Bitbucket page`_. Alternatively if you use
Mercurial_, you can clone the repository with the following command::

   $ hg clone https://bitbucket.org/bgneal/m209

If you did not use pip, you can install with this command::

   $ python setup.py install

Support & Source
----------------

All support takes place at the `m209 Bitbucket page`_. Please enter any
feature requests or bugs into the `issue tracker`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _M-209: http://en.wikipedia.org/wiki/M-209
.. _Python: http://www.python.org
.. _Python Package Index: http://pypi.python.org/pypi/m209/
.. _m209 Bitbucket page: https://bitbucket.org/bgneal/m209
.. _pip: http://www.pip-installer.org
.. _Mercurial: http://mercurial.selenic.com/
.. _issue tracker: https://bitbucket.org/bgneal/m209/issues
