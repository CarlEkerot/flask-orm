from webapp.models.user import User


class TestLogin:

    def test_user_login(self, client, session):
        admin = User('admin', 'supersafepassword')
        session.add(admin)
        session.commit()

        rv = client.post('/login', data={
            'username': 'admin',
            'password': "supersafepassword",
        })

        assert rv.status_code == 200
        assert 'Logged in' in rv.data
