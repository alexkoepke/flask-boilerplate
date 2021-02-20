from app import create_app, db, cli

# from app.models import models, go, here


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    # return {'db': db, 'models': models, 'go': go, 'here': here}
    return {'db': db}
