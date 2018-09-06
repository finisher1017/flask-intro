from project import db
from project.models import User

# insert data
#db.session.add(User("michael", "michael@realpython.com", "i'll-never-tell"))
db.session.add(User("jonnyboy", "jb@seubs.com", "jonnyboy"))

# commit the changes
db.session.commit()