import models


if __name__ == '__main__':
    models.initialize()
    models.User.create_user(
        username="Bob",
        email="example@example.com",
        password="password",
        admin=True
    )
