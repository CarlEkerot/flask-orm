from webapp.models.user import User


class TestMainController:

    def test_home(self, client):
        rv = client.get('/')
        assert rv.status_code == 200

    def test_login(self, client, session):
        admin = User('admin', 'supersafepassword')
        session.add(admin)
        session.commit()

        rv = client.post('/login', data={
            'username': 'admin',
            'password': 'supersafepassword',
        })

        assert rv.status_code == 200

    def test_login_fail(self, client):
        rv = client.post('/login', data={
            'username': 'admin',
            'password': 'badpassword',
        })

        assert rv.status_code == 401

    def test_logout(self, client, session):
        admin = User('admin', 'supersafepassword')
        session.add(admin)
        session.commit()

        rv = client.post('/login', data={
            'username': 'admin',
            'password': 'supersafepassword',
        })

        rv = client.get('/logout')
        assert rv.status_code == 200

    def test_restricted(self, client):
        rv = client.get('/restricted')
        assert rv.status_code == 401
