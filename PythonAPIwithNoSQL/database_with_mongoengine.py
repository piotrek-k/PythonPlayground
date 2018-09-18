"""
Example of using MongoEngine
Source from https://realpython.com/introduction-to-mongodb-and-python/
Documentation: http://docs.mongoengine.org/guide/index.html
"""

from mongoengine import *
import datetime

connect('PythonAPIwithNoSQL', host='localhost', port=27017)


class Author(Document):
    name = StringField()


class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = ReferenceField(Author)
    published = DateTimeField(default=datetime.datetime.now)
    visible = BooleanField()

    @queryset_manager
    def live_posts(clazz, queryset):
        return queryset.filter(visible=True)


def new_author(author_name):
    author_1 = Author(
        name=author_name
    )
    author_1.save()


def new_post():
    """
    Adds new post. Will throw exception if provided data doesn't meet provided schema
    """
    author_1 = Author.objects(name="Steve").first()

    post_1 = Post(
        title='Sample Post',
        content='Some engaging content',
        author=author_1,
        visible=True
    )
    post_1.save()  # This will perform an insert
    print(post_1.title)
    # post_1.title = 'A Better Post Title'
    # post_1.save()  # This will perform an atomic edit on "title"
    # print(post_1.title)


def use_method_in_model():
    print(Post.live_posts())


def reference_other_document():
    print("Referencing Author from Post")
    print(Post.objects.first().author.name)


