from core import serializer


class UserSerializer(serializer.Schema):
    class Meta:
        fields = ('id', 'name', 'email')
