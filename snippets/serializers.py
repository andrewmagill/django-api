from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'owner', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    # 'snippets' has a reverse relationship to the user model, so
    # it will not be included by default, we need to explicitly add the field
    snippets = serializers.PrimaryKeyRelatedField(many=True,
                                                  queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
