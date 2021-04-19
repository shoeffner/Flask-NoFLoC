"""
Flask-NoFLoC is a Flask extension to opt-out of FLoC.
"""
import functools

from flask import make_response


__version__ = '1.0.0'


def add_nofloc_header(view_function):
    """Adds the :code:`Permission-Policy` header to a result from a view function.

    This is supposed to be used as a decorator and should come *after* the
    :meth:`flask:flask.Flask.route` or :meth:`flask:flask.Blueprint.route` decorator:

    .. code :: python

        @app.route('/nofloc')
        @add_nofloc_header
        def nofloc_route():
            return 'response'

    :param view_function: A view function, see :doc:`flask:tutorial/views`.
    :type view_function: :func:`python:callable`
    """
    @functools.wraps(view_function)
    def wrapper(*args, **kwargs):
        response = make_response(view_function(*args, **kwargs))
        return _add_nofloc_header(response)
    return wrapper


def _add_nofloc_header(response):
    """Adds the :code:`Permission-Policy` header to a :class:`flask:Response`.

    This is an internal function and is called by :func:`add_nofloc_header` and
    registered as an :meth:`flask:flask.Flask.after_request` hook in
    :meth:`NoFLoC.init_app` .

    The function adds the :code:`Permission-Policy` header with a value of
    :code:`interest-cohort=()` unless it is already present.

    :param response: A response object.
    :type response: :class:`flask:flask.Response`
    """
    if 'Permission-Policy' not in response.headers:
        response.headers['Permission-Policy'] = 'interest-cohort=()'
    return response


class NoFLoC:
    """The base extension class."""

    def __init__(self, app=None):
        """Initializes the extension.
        If an app is given, :meth:`init_app` is called.

        :param app: A Flask app.
        :type app: :class:`flask:flask.Flask`
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Adds :func:`_add_nofloc_header` as an :meth:`flask:flask.Flask.after_request`
        hook to the app.

        :param app: A Flask app.
        :type app: :class:`flask:flask.Flask`
        """
        app.after_request(_add_nofloc_header)
