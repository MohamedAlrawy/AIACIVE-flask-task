from sqlalchemy.orm import validates

from core import models


# clear models metadata object
models.metadata.clear()

class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    name = models.Column(models.String(50))
    email = models.Column(models.String(50), unique=True, index=True)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email
        return email


if __name__ == "__main__":
    models.create_all()
