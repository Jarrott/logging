from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)


