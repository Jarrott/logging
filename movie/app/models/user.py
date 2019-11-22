from .base import Base, db


class User(Base):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text, comment='简介')
    face = db.Column(db.String(255), unique=True, comment='头像')
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship('UserLog', backref='user')
    comments = db.relationship('Comment', backref='user')
    moviecols = db.relationship('Moviecol', backref='user')

    def __repr__(self):
        return "<User> %r" % self.name


class UserLog(Base):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(50))

    def __repr__(self):
        return '<UserLog %r>' % self.id


