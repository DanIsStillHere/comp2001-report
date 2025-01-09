# people.py

from flask import request
from flask import abort, make_response
from config import db
from models import (
    Trail,
    Feature,
    TrailFeature,
    User,
    trail_schema,
    trails_schema,
    feature_schema,
    features_schema,
    trail_feature_schema,
    trail_features_schema,
    user_schema,
    users_schema,
)

# Trails
def read_all_trails():
    trails = Trail.query.all()
    return trails_schema.dump(trails)

def create_trail():
    trail = request.get_json()
    owner_id = trail.get("OwnerID")
    # Check if the owner exists
    owner = User.query.get(owner_id)
    if not owner:
        abort(404, f"User with ID {owner_id} not found. Cannot create trail.")
    
    # Create the new trail
    new_trail = trail_schema.load(trail, session=db.session)
    db.session.add(new_trail)
    db.session.commit()
    return trail_schema.dump(new_trail), 201

def read_one_trail(trail_id):
    trail = Trail.query.get(trail_id)
    if trail:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with ID {trail_id} not found")

def update_trail(trail_id):
    trail_data = request.get_json()
    existing_trail = Trail.query.get(trail_id)

    if existing_trail:
        update_data = trail_schema.load(trail_data, session=db.session, partial=True)
        for key, value in trail_data.items():
            setattr(existing_trail, key, value)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f"Trail with ID {trail_id} not found")

def delete_trail(trail_id):
    existing_trail = Trail.query.get(trail_id)
    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"Trail ID {trail_id} successfully deleted", 200)
    else:
        abort(404, f"Trail with ID {trail_id} not found")

# Features
def read_all_features():
    features = Feature.query.all()
    return features_schema.dump(features)

def create_feature():
    feature = request.get_json()
    new_feature = feature_schema.load(feature, session=db.session)
    db.session.add(new_feature)
    db.session.commit()
    return feature_schema.dump(new_feature), 201

# TrailFeature (Linking Features to Trails)
def create_trail_feature():
    trail_feature = request.get_json()
    trail_id = trail_feature.get("TrailID")
    feature_id = trail_feature.get("TrailFeatureID")

    # Validate if the trail and feature exist
    trail = Trail.query.get(trail_id)
    feature = Feature.query.get(feature_id)

    if not trail:
        abort(404, f"Trail with ID {trail_id} not found. Cannot link feature.")
    if not feature:
        abort(404, f"Feature with ID {feature_id} not found. Cannot link to trail.")

    # Create the trail-feature relationship
    new_trail_feature = trail_feature_schema.load(trail_feature, session=db.session)
    db.session.add(new_trail_feature)
    db.session.commit()
    return trail_feature_schema.dump(new_trail_feature), 201

# Users
def read_all_users():
    users = User.query.all()
    return users_schema.dump(users)

def create_user():
    user = request.get_json()
    email = user.get("EmailAddress")
    existing_user = User.query.filter_by(EmailAddress=email).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"User with email {email} already exists")

def read_one_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user_schema.dump(user)
    else:
        abort(404, f"User with ID {user_id} not found")

def delete_user(user_id):
    existing_user = User.query.get(user_id)
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"User ID {user_id} successfully deleted", 200)
    else:
        abort(404, f"User with ID {user_id} not found")