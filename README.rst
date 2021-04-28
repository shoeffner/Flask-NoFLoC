============
Flask-NoFLoC
============

Flask-NoFLoC_ is a `Flask extension`_ which disables FLoC_ by adding the header

.. code::

    Permissions-Policy: interest-cohort=()

to each HTTP response of your app. Documentation_

.. _Flask-NoFLoC: https://Flask-NoFLoC.readthedocs.io/en/latest/
.. _Documentation: https://Flask-NoFLoC.readthedocs.io/en/latest/
.. _Flask extension: https://flask.palletsprojects.com/en/1.1.x/extensiondev/
.. _Flask: https://flask.palletsprojects.com
.. _FLoC: https://web.dev/floc/


Examples
--------

To set it up, follow the usual Flask extension setup, either directly:

.. code:: python

    from flask import Flask
    from flask_nofloc import NoFLoC

    app = Flask(__name__)
    NoFLoC(app)

or using the ``init_app``-paradigm:

.. code:: python

    # extensions.py
    from flask_noflock import NoFLoC

    nofloc = NoFLoC()


    # app.py
    from flask import Flask
    from extensions import nofloc

    def create_app(settings):
        app = Flask('myapp')

        nofloc.init_app(app)

        return app

If you only want to exclude specific route, you can use a decorator:

.. code:: python

    from flask_nofloc import add_nofloc_header

    @app.route('/nofloc')
    @add_nofloc_header
    def no_floc():
        return 'no FLoC'


Installation
------------

Install via pip and your favorite installation method:

.. code:: bash

    pip install Flask-NoFLoC


Background
----------

For some background on FLoC, here is a list of related links:

- Technical background: https://web.dev/floc/
- Specification: https://github.com/WICG/floc / https://wicg.github.io/floc/
- An implementation of SimHash: https://github.com/hybridtheory/floc-simhash
- Critique on FLoC: https://www.eff.org/deeplinks/2021/03/googles-floc-terrible-idea
- How to opt out: https://paramdeo.com/blog/opting-your-website-out-of-googles-floc-network
- Browser coverage: https://www.theverge.com/2021/4/16/22387492/google-floc-ad-tech-privacy-browsers-brave-vivaldi-edge-mozilla-chrome-safari


Alternatives
------------

Came here for Django? Check out django-nofloc_.

.. _django-nofloc: https://pypi.org/project/django-nofloc/
