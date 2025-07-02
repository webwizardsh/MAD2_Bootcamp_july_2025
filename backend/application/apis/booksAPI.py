import json
from flask import request, jsonify
from flask_restful import Resource, reqparse, abort, fields, marshal_with

from application.data.model import db,Books

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "author": fields.String
}

book_post_args = reqparse.RequestParser()
book_post_args.add_argument('name', type = str, required = True, help = "book name is required")
book_post_args.add_argument('author', type=str, required = True, help = "book author is required")

book_put_args = reqparse.RequestParser()
book_put_args.add_argument('name', type = str)
book_put_args.add_argument('author', type=str)


class AllBookAPI(Resource):
    @marshal_with(resource_fields)
    def get(resource):
        books = Books.query.all()
        if not books:
            abort (404, message = "No Books found")
        return books,200
    
    @marshal_with(resource_fields)
    def post(resource):
        args = book_post_args.parse_args()
        book = Books.query.filter_by(name = args["name"]).first()
        if book:
            abort(409, message="book already exists")
        input = Books(name = args["name"], author = args["author"])
        db.session.add(input)
        db.session.commit()
        return input, 201
    
class BookAPI(Resource):
    @marshal_with(resource_fields)
    def get(self, book_id):
        book = Books.query.filter_by(id = book_id).first()
        if not book:
            abort(404, message = "Could not found book with this book_id")
        return book, 200
    
    @marshal_with(resource_fields)   
    def put(self,book_id):
        args = book_put_args.parse_args()
        book = Books.query.filter_by(id = book_id).first()
        if not book:
            abort(404, message = "Could not found book with this book_id")
        if args["name"]:
            book_name_exists = Books.query.filter_by(name = args["name"]).first()
            if book_name_exists:
                abort(409, message="book name already exists")
            book.name = args["name"]
        if args["author"]:
            book.author = args["author"]
            
        db.session.commit()
        return book , 200
    
    def delete(self, book_id):
        book = Books.query.filter_by(id = book_id).first()
        if not book:
            abort(404, message = "Could not found book with this book_id")
        db.session.delete(book)
        db.session.commit()
        return jsonify({"status":"Book Deleted", "deleted book": book.name})