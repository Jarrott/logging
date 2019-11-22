from .base import Base, db


class Auth(Base):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<Auth %r>" % self.name


class Role(Base):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))

    def __repr__(self):
        return "<Role %r>" % self.name
