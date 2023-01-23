from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import InputRequired
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
api = Api(app)

class AlbumForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    cover = FileField('Cover')

@app.route('/')
def index():
    form = AlbumForm()
    return render_template('index.html', form=form)

@app.route('/albums', methods=['POST'])
def add_album():
    form = AlbumForm()
    if form.validate_on_submit():
        title = form.title.data
        cover = form.cover.data

        filename = secure_filename(cover.filename)
        cover.save(os.path.join('static/img', filename))

        return redirect(url_for('index'))

class Album(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(Album, '/album/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
