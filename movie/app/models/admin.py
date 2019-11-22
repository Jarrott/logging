from .base import Base, db


class Admin(Base):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), comment='所属角色')
    adminlogs = db.relationship('AdminLog', backref='admin')
    oplogs = db.relationship('OpLog', backref='admin')

    def __repr__(self):
        return '<Admin %r>' % self.name


class AdminLog(Base):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(50))

    def __repr__(self):
        return '<AdminLog %r>' % self.id


class OpLog(Base):
    __tablename__ = 'oplog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(50))
    reason = db.Column(db.String(600), comment='操作原因')

    def __repr__(self):
        return '<OpLog %r>' % self.id