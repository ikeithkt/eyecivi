from flask import render_template

from app import create_app

app = create_app()


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
