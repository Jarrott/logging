from .base import Base, db


class Movie(Base):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255))
    star = db.Column(db.SmallInteger)
    playnum = db.Column(db.BigInteger, comment='播放数')
    commentnum = db.Column(db.BigInteger, comment='评论数')
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(100), comment='地区')
    release_time = db.Column(db.Date, comment='上映时间')
    length = db.Column(db.String(100))
    comments = db.relationship('Comment', backref='movie')
    moviecols = db.relationship('Moviecol', backref='movie')

    def __repr__(self):
        return "<Movie %r>" % self.title


# 上映预告
class Preview(Base):
    __tablename__ = 'preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    logo = db.Column(db.String(255))

    def __repr__(self):
        return "<Preview %r>" % self.title


# 电影收藏
class Moviecol(Base):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Moviecol %r>" % self.id