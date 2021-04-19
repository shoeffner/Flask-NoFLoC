from flask import Flask
from flask_nofloc import NoFLoC, add_nofloc_header


def test_direct_instantiation():
    app = Flask('DirectApp')
    NoFLoC(app)

    @app.route('/')
    def index():
        return ''

    with app.test_client() as client:
        response = client.get('/')

    assert 'Permission-Policy' in response.headers, 'Permission-Policy is not in headers'
    assert response.headers['Permission-Policy'] == 'interest-cohort=()', 'Permission-Policy is not interest-cohort=()'


def test_init_app_instantiation():
    app = Flask('InitApp')

    @app.route('/')
    def index():
        return ''

    nofloc = NoFLoC()
    nofloc.init_app(app)

    with app.test_client() as client:
        response = client.get('/')

    assert 'Permission-Policy' in response.headers, 'Permission-Policy is not in headers'
    assert response.headers['Permission-Policy'] == 'interest-cohort=()', 'Permission-Policy is not interest-cohort=()'


def test_two_apps():
    app1 = Flask('App1')

    @app1.route('/')
    def index1():
        return '1'

    app2 = Flask('App2')

    @app2.route('/')
    def index2():
        return '2'

    nofloc = NoFLoC()
    nofloc.init_app(app1)
    nofloc.init_app(app2)

    with app1.test_client() as client:
        response = client.get('/')

    assert 'Permission-Policy' in response.headers, 'Permission-Policy is not in headers for app1'
    assert response.headers['Permission-Policy'] == 'interest-cohort=()', 'Permission-Policy is not interest-cohort=() for app1'

    with app2.test_client() as client:
        response = client.get('/')

    assert 'Permission-Policy' in response.headers, 'Permission-Policy is not in headers for app2'
    assert response.headers['Permission-Policy'] == 'interest-cohort=()', 'Permission-Policy is not interest-cohort=() for app2'


def test_individual_route():
    app = Flask('TestApp')

    @app.route('/floc')
    def floc():
        return 'floc'

    @app.route('/nofloc')
    @add_nofloc_header
    def nofloc():
        return 'nofloc'

    with app.test_client() as client:
        response = client.get('/floc')

        assert 'Permission-Policy' not in response.headers, 'Permission-Policy is in headers but should not be'

        response = client.get('/nofloc')

        assert 'Permission-Policy' in response.headers, 'Permission-Policy is not in headers'
        assert response.headers['Permission-Policy'] == 'interest-cohort=()', 'Permission-Policy is not interest-cohort=()'
