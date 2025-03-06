from rest_framework import serializers
from .models import Person, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ["id", "book_name", "returned"]
        fields = '__all__'

class PersonSer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    book = BookSerializer(read_only=True)
    
    class Meta:
        model = Person
        fields = '__all__'
        # exclude = ["book"]
        # depth = 1
        
    def get_country(self, obj):
        return "INDIA"