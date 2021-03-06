import time
from flask import Response

from doajtest.helpers import DoajTestCase
from portality import models
from portality.core import app
from portality.app import load_account_for_login_manager
from portality.decorators import api_key_required, api_key_optional

class TestClient(DoajTestCase):
    @classmethod
    def setUpClass(cls):
        @app.route('/hello')
        @api_key_required
        def hello_world():
            return Response("hello, world!")

        @app.route('/helloopt')
        @api_key_optional
        def hello_world_opt():
            return Response("hello, world!")

        app.testing = True
        app.login_manager.user_loader(load_account_for_login_manager)

    def setUp(self):
        super(TestClient, self).setUp()

    def tearDown(self):
        super(TestClient, self).tearDown()

    def test_01_api_role(self):
        """test the new roles added for the API"""
        a1 = models.Account.make_account(username="a1_user", name="a1_name", email="a1@example.com", roles=["user", "api"], associated_journal_ids=[])
        a1.save()
        time.sleep(1)

        # Check an API key was generated on account creation
        a1_key = a1.api_key
        assert a1_key is not None

        # Check we can retrieve the account by its key
        a1_retrieved = models.Account.pull_by_api_key(a1_key)
        assert a1 == a1_retrieved

        # Check that removing the API role means you don't get a key
        a1.remove_role('api')
        assert a1.api_key is None

    def test_02_api_required_decorator(self):
        """test the api_key_required decorator"""
        a1 = models.Account.make_account(username="a1_user", name="a1_name", email="a1@example.com", roles=["user", "api"], associated_journal_ids=[])
        a1_key = a1.api_key
        a1.save()               # a1 has api access

        a2 = models.Account.make_account(username="a2_user", name="a2_name", email="a2@example.com", roles=["user", "api"], associated_journal_ids=[])
        a2_key = a2.api_key     # user gets the key before access is removed
        a2.remove_role('api')
        a2.save()               # a2 does not have api access.

        time.sleep(1)

        with app.test_client() as t_client:
            # Check the authorised user can access our function, but the unauthorised one can't.
            response_authorised = t_client.get('/hello?api_key=' + a1_key)
            assert response_authorised.data == "hello, world!"
            assert response_authorised.status_code == 200

            response_denied = t_client.get('/hello?api_key=' + a2_key)
            assert response_denied.status_code == 401

    def test_03_api_optional_decorator(self):
        """test the api_key_optional decorator"""
        a1 = models.Account.make_account(username="a1_user", name="a1_name", email="a1@example.com", roles=["user", "api"], associated_journal_ids=[])
        a1_key = a1.api_key
        a1.save()               # a1 has api access

        a2 = models.Account.make_account(username="a2_user", name="a2_name", email="a2@example.com", roles=["user", "api"], associated_journal_ids=[])
        a2_key = a2.api_key     # user gets the key before access is removed
        a2.remove_role('api')
        a2.save()               # a2 does not have api access.

        # There is no a3 - the last test case is just a public call with no API key

        time.sleep(1)

        with app.test_client() as t_client:
            # Check the authorised user can access our function, but the unauthorised one can't.
            response_authorised = t_client.get('/helloopt?api_key=' + a1_key)
            assert response_authorised.data == "hello, world!"
            assert response_authorised.status_code == 200

            response_denied = t_client.get('/helloopt?api_key=' + a2_key)
            assert response_denied.status_code == 401

            # also check it's ok to not have a key at all
            response_authorised2 = t_client.get('/helloopt')
            assert response_authorised2.data == "hello, world!"
            assert response_authorised2.status_code == 200

            # but if you do specify a key it needs to exist
            response_denied2 = t_client.get('/helloopt?api_key=nonexistent_key')
            assert response_denied2.status_code == 401
