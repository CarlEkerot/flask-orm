class TestMainController:

    def test_home(self, client):
        rv = client.get('/')
        assert rv.status_code == 200

    def test_login(self, client):
        rv = client.post('/login')
        assert rv.status_code == 200

    def test_logout(self, client):
        rv = client.get('/logout')
        assert rv.status_code == 200

    def test_restricted(self, client):
        rv = client.get('/restricted')
        assert rv.status_code == 401
