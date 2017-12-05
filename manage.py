from flask_script import Manager
from songbase import app, db, Artist, Song

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    coldplay = Artist(name='Junbo Son', about='Junbo is a Business Analytics teacher.')
    maroon5 = Artist(name='Diane Wright', about='Diane Wright is a MISY160 teacher.')
    song1 = Song(name='BUAD345', year=2017, lyrics="Analytics and Visualization", artist=coldplay)
    song2 = Song(name='MISY160', year=2016, lyrics="Intro to Business Information Systems", artist=maroon5)
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
