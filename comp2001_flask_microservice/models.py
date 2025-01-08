# models.py

from datetime import datetime
import pytz
from config import db, ma

# Trail Table
class Trail(db.Model):
    __tablename__ = "Trail"
    __table_args__ = {"schema": "CW2"}
    TrailID = db.Column(db.Integer, primary_key=True)
    TrailName = db.Column(db.String(255), nullable=False)
    TrailSummary = db.Column(db.String(1024))
    TrailDescription = db.Column(db.Text)
    Difficulty = db.Column(db.String(50))
    Location = db.Column(db.String(255))
    Length = db.Column(db.Float)
    ElevationGain = db.Column(db.Float)
    RouteType = db.Column(db.String(50))
    OwnerID = db.Column(db.Integer, db.ForeignKey("CW2.User.UserID"))
    Pt1_lat = db.Column(db.Float)
    Pt1_long = db.Column(db.Float)
    Pt1_desc = db.Column(db.String(255))
    Pt2_lat = db.Column(db.Float)
    Pt2_long = db.Column(db.Float)
    Pt2_desc = db.Column(db.String(255))
    Pt3_lat = db.Column(db.Float)
    Pt3_long = db.Column(db.Float)
    Pt3_desc = db.Column(db.String(255))
    Pt4_lat = db.Column(db.Float)
    Pt4_long = db.Column(db.Float)
    Pt4_desc = db.Column(db.String(255))
    Pt5_lat = db.Column(db.Float)
    Pt5_long = db.Column(db.Float)
    Pt5_desc = db.Column(db.String(255))

# Feature Table
class Feature(db.Model):
    __tablename__ = "Feature"
    __table_args__ = {"schema": "CW2"}
    TrailFeatureID = db.Column(db.Integer, primary_key=True)
    TrailFeature = db.Column(db.String(255), nullable=False)

# TrailFeature Table (Composite Key)
class TrailFeature(db.Model):
    __tablename__ = "TrailFeature"
    __table_args__ = {"schema": "CW2"}
    TrailID = db.Column(db.Integer, db.ForeignKey("CW2.Trail.TrailID"), primary_key=True)
    TrailFeatureID = db.Column(db.Integer, db.ForeignKey("CW2.Feature.TrailFeatureID"), primary_key=True)

# User Table
class User(db.Model):
    __tablename__ = "User"
    __table_args__ = {"schema": "CW2"}
    UserID = db.Column(db.Integer, primary_key=True)
    EmailAddress = db.Column(db.String(255), unique=True, nullable=False)
    Role = db.Column(db.String(50), nullable=False)

# Schemas
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True

class TrailFeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailFeature
        load_instance = True

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)

trail_feature_schema = TrailFeatureSchema()
trail_features_schema = TrailFeatureSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)