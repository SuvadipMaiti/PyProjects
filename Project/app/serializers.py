from rest_framework import serializers
from .models import Books,Character,Author

# Serializers define the API representation.
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','surname']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Books
        fields = ['title','description','price','published','is_published','cover','characters','authors']


