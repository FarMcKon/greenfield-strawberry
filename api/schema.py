import typing
import strawberry

#import db_engine

def get_backing_db():
    return BackingDB(dbVersion='1.x',
    schemaVersion='1.x')

def get_books():
 return [
     Book(
         title="The Great Gatsby",
         author="F. Scott Fitzgerald",
         date = 'never'
     ),
     Book(
        title='some books',
        author="some guy",
        date='foo')
 ]

@strawberry.type
class BackingDB:
    dbVersion: str
    schemaVersion: str



@strawberry.type
class Book:
    title: str
    author: str
    date: str


@strawberry.type
class Query:
    #books: typing.List[Book] = strawberry.field(resolver=get_books)
    backing: BackingDB = strawberry.field(resolver=get_backing_db)

schema = strawberry.Schema(query=Query)