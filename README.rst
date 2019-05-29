========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/atomstoys/badge/?style=flat
    :target: https://readthedocs.org/projects/atomstoys
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/craabreu/atomstoys.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/craabreu/atomstoys

.. |codecov| image:: https://codecov.io/github/craabreu/atomstoys/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/craabreu/atomstoys

.. |version| image:: https://img.shields.io/pypi/v/atomstoys.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/atomstoys

.. |commits-since| image:: https://img.shields.io/github/commits-since/craabreu/atomstoys/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/craabreu/atomstoys/compare/v0.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/atomstoys.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/atomstoys

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/atomstoys.svg
    :alt: Supported versions
    :target: https://pypi.org/project/atomstoys

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/atomstoys.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/atomstoys


.. end-badges

A library for toy model simulations

* Free software: MIT license

Installation
============

::

    pip install atomstoys

Documentation
=============


https://atomstoys.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
