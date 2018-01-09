import unittest

from pyramid import testing


class RoutingTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_appsettings
        settings = get_appsettings('pytest.ini', name='main')
        from atlas_of_innovation import main
        app = main(global_config = None, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    # static page tests
    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'<h1 id="map-page-title">Crowdsourced Atlas of Community Innovation Spaces</h1>' in res.body)

    def test_map(self):
        res = self.testapp.get('/map', status=200)
        self.assertIn(b'<h1 id="map-page-title">Crowdsourced Atlas of Community Innovation Spaces</h1>', res.body)

    def test_about(self):
        res = self.testapp.get('/about', status=200)
        self.assertIn(b'This platform was financially supported by', res.body)

    def test_goals(self):
        res = self.testapp.get('/about/goals', status=200)
        self.assertIn(b"We're making a map and public wiki for anyone to add new spaces and correct information about existing spaces.", res.body)

    def test_docs(self):
        res = self.testapp.get('/docs', status=200)
        self.assertIn(b'Datafields and definitions', res.body)

    def test_dev_docs(self):
        res = self.testapp.get('/docs/developer', status=200)
        self.assertIn(b'Creative Commons Attribution-ShareAlike 4.0 International Public License', res.body)

    def test_wiki(self):
        res = self.testapp.get('/wiki', status=200)
        self.assertIn(b'Countries', res.body)

