from project import db
#from project.models import BlogPost

#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Good", "I\'m cool."))
db.session.add(BlogPost("Good", "I\'m aight."))

#commit the changes
db.session.commit()