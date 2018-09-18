"""
Demonstration of operating on MongoDb using official pymongo library
"""

"""
Quotation from: https://realpython.com/introduction-to-mongodb-and-python/

While PyMongo is very easy to use and overall a great library,
it’s probably a bit too low-level for many projects out there.
Put another way, you’ll have to write a lot of your own code to
consistently save, retrieve, and delete objects.

One library that provides a higher abstraction on top of PyMongo is MongoEngine.
MongoEngine is an object document mapper (ODM),
which is roughly equivalent to a SQL-based object relational mapper (ORM).
The abstraction provided by MongoEngine is class-based, so all of the models you create are classes.
"""


from pymongo import MongoClient
client = MongoClient()  # defaults to MongoClient('localhost', 27017) or MongoClient('mongodb://localhost:27017')

db = client['PythonAPIwithNoSQL']
posts = db.posts


def post_something_to_database():
    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))


def post_many_things_to_database():
    post_1 = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    post_2 = {
        'title': 'Virtual Environments',
        'content': 'Use virtual environments, you guys',
        'author': 'Scott'
    }
    post_3 = {
        'title': 'Learning Python',
        'content': 'Learn Python, it is easy',
        'author': 'Bill'
    }
    new_result = posts.insert_many([post_1, post_2, post_3])
    print('Multiple posts: {0}'.format(new_result.inserted_ids))


def find_one_with_bill():
    bills_post = posts.find_one({'author': 'Bill'})
    print(bills_post)


def find_all_by_scott():
    scotts_posts = posts.find({'author': 'Scott'})
    print("Cursor object received: ", scotts_posts)
    for post in scotts_posts:
        print(post)