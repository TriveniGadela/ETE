import mongoengine

def init_db(app):
    mongoengine.connect(host=app.config['MONGODB_URI'])
