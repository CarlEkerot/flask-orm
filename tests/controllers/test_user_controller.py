import ujson

from webapp.models.user import User


class TestUserController:

    def test_get_users(self, client, session):
        session.add(User('admin1', 'supersafepassword'))
        session.add(User('admin2', 'supersafepassword'))
        session.commit()

        rv = client.get('/users')
        assert rv.status_code == 200

        res = ujson.loads(rv.data)
        assert len(res) == 2

    def test_get_user(self, client, session):
        u = User('admin', 'supersafepassword')
        session.add(u)
        session.commit()

        user = User.query.first()
        assert user

        rv = client.get('/users/%u' % user.id)
        assert rv.status_code == 200

    def test_get_non_existing_user(self, client):
        rv = client.get('/users/1')
        assert rv.status_code == 404

    def test_create_user(self, client, session):
        rv = client.post('/users', data={
            'username': 'admin',
            'password': 'supersafepassword',
        })
        assert rv.status_code == 200

        user = User.query.first()
        assert user is not None

    def test_create_existing_user(self, client, session):
        u = User('admin', 'supersafepassword')
        session.add(u)
        session.commit()

        rv = client.post('/users', data={
            'username': 'admin',
            'password': 'supersafepassword',
        })
        assert rv.status_code == 200

        res = User.query.first()
        assert res.username == u.username

    def test_update_user(self, client, session):
        u = User('admin', 'supersafepassword')
        session.add(u)
        session.commit()

        expected = 'nimda'

        rv = client.put('/users/%u' % u.id, data={
            'username': expected,
            'password': 'supersafepassword',
        })
        assert rv.status_code == 200

        session.commit()
        assert u.username == expected

    def test_delete_user(self, client, session):
        count1 = User.query.count()
        u = User('admin', 'supersafepassword')
        session.add(u)
        session.commit()

        count2 = User.query.count()
        assert count2 > count1

        rv = client.delete('/users/%u' % u.id)
        assert rv.status_code == 200

        count3 = User.query.count()
        assert count3 < count2
