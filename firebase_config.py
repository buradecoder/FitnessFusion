import firebase_admin
from firebase_admin import credentials

# Check if Firebase is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('gym-app-minor-project-e49f3b2dbeca.json')
    firebase_admin.initialize_app(cred)

