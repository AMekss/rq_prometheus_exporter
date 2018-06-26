from api import api

class TestServiceRoutes():
    api.testing = True
    test_service = api.test_client()

    def test_get_healthcheck(self):
        resp = self.test_service.get('/healthz')
        assert resp.status_code == 200

    def test_get_metrics(self):
        resp = self.test_service.get('/metrics')
        assert resp.status_code == 200
