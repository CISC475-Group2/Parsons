from rest_framework import serializers
from app.models import Problem
from racketparser import parser

# print(parser.read_parse_string_to_list(parser.parse("(- 2 (3 2))")))

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'question', 'points')
