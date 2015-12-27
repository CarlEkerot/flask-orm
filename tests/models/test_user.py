from webapp.models.user import User


class TestUserModel:

    def test_user_save(self, session):
        admin = User('admin', 'supersafepassword')
        session.add(admin)
        session.commit()

        user = User.query.filter_by(username="admin").first()
        assert user is not None

    def test_user_password(self):
        """ Test password hashing and checking """
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert admin.check_password('supersafepassword')
