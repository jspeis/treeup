from treeup import db

class Base(db.Model):
    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Donation(Base):
    name = db.Column(db.String(128), nullable=True, default="Anonymous")
    email = db.Column(db.String(128),  nullable=True)
    amount = db.Column(db.Float, nullable=False) # in cents
    message = db.Column(db.String, nullable=True)

    def __str__(self):
        return '<User {} Msg: {}>'.format(self.name, self.message)
