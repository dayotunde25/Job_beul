<<<<<<< HEAD
# In Python shell or add to your code:
from __init__ import create_app, db
from flask import current_app
from app.models import User

app = create_app()
with app.app_context():
    admin = User(username='admin', email='admin@example.com', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
=======
# In Python shell or add to your code:
from __init__ import create_app, db
from flask import current_app
from app.models import User

app = create_app()
with app.app_context():
    admin = User(username='admin', email='admin@example.com', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
>>>>>>> 24806e06812e7a8caf53d6dd5ce6b2ee56a9d86f
