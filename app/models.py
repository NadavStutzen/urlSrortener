from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Url(db.Model):
    """
    Create a Urls table
    """

    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    longUrl = db.Column(db.String(300), unique = True, nullable=False)
    shortUrl = db.Column(db.String(40), unique = True, nullable=True)
    
def __init__(self,url): 
    self.longUrl = url
    self.shortUrl = ''
    
