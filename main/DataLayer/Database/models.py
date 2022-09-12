from main import db


class StaticInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_section = db.Column(db.String, nullable=False)
    s_section = db.Column(db.String, nullable=False)
