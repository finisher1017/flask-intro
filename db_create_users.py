from project import db
from project.models import User

# insert data
#db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("jonathan", "jonathan@seubs.com", "jonathan"))

# commit the changes
db.session.commit()