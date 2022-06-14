from topibox import create_app, db
from topibox.models import *

app = create_app()



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}