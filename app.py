from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

albums = []

class Album(Resource):
    def get(self, id):
        for album in albums:
            if album['id'] == id:
                return album
        return {"error": "album not found"}, 404
    
    def put(self, id):
        for album in albums:
            if album['id'] == id:
                album['title'] = request.form['title']
                album['artist'] = request.form['artist']
                return {"message": "album updated successfully"}
        return {"error": "album not found"}, 404
    
    def delete(self, id):
        for album in albums:
            if album['id'] == id:
                albums.remove(album)
                return {"message": "album deleted successfully"}
        return {"error": "album not found"}, 404

class AlbumList(Resource):
    def get(self):
        return albums
    
    def post(self):
        album = {
            'id': len(albums) + 1,
            'title': request.form['title'],
            'artist': request.form['artist']
        }
        albums.append(album)
        return {"message": "album added successfully", "album": album}, 201

api.add_resource(Album, '/album/<int:id>')
api.add_resource(AlbumList, '/albums')

if __name__ == '__main__':
    app.run(debug=True)

