import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Put this on environment variable usinf setup tools
cred = credentials.Certificate('neufluence-404e714ebc5d.json')
firebase_admin.initialize_app(cred)


def get_firebase_db():
    # Use a service account
    db = firestore.client()
    return db
