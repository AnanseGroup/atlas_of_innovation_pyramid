import unittest
import transaction

from pyramid import testing

def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)


class APITests(unittest.TestCase):
    def init_database(self, settings_file):
        from atlas_of_innovation.models.meta import Base
        session_factory = self.config.registry['dbsession_factory']
        engine = session_factory.kw['bind']
        Base.prepare(engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        from atlas_of_innovation.models import reset_db
        reset_db.main(argv=["reset_db", settings_file, "atlas_of_innovation/tests/test_spaces.csv"])

    def setUp(self):
        from pyramid.paster import get_appsettings
        settings_file = "pytest.ini"
        settings = get_appsettings(settings_file, name='main')
        from atlas_of_innovation.models import get_tm_session
        self.config = testing.setUp(settings=settings)

        # For some reason, the following include does not add the dbsession
        # variable in the request the way it does when using more full-
        # featured versions of the app. As a work- around, use the
        # dummy_request method and manage the transactions on your own instead
        # of depending on the request to do it. See the docstraing for
        # get_tm_session for more information.
        self.config.include('atlas_of_innovation.models')

        session_factory = self.config.registry['dbsession_factory']
        self.session = get_tm_session(session_factory, transaction.manager)
        self.init_database(settings_file)

    def tearDown(self):
        testing.tearDown()

        transaction.abort()

        from atlas_of_innovation.models.meta import Base
        session_factory = self.config.registry['dbsession_factory']
        engine = session_factory.kw['bind']
        Base.metadata.drop_all(engine)


    def test_map_requirements(self):
        from atlas_of_innovation.views.API_views import all_innovation_spaces
        request = dummy_request(self.session)
        info = all_innovation_spaces(request)
        self.assertIn('latitude', info[0])
        self.assertIn('longitude', info[0])
        self.assertIn('name', info[0])
        self.assertIn('city', info[0])
        self.assertIn('country', info[0])
        self.assertIn('types', info[0])
        self.assertIn('description', info[0])
        self.assertIn('wiki', info[0])