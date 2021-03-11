import os
import django
from rest_framework import serializers

# settings.configure(DEBUG=True)
# settings.configure(default_settings=myapp_defaults, DEBUG=True)

# reference https://stackoverflow.com/questions/24793351/django-appregistrynotready
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
# end reference

from django.conf import settings

# Reference: what follows is an example from
# https://www.django-rest-framework.org/api-guide/serializers/#declaring-serializers
# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
# https://www.django-rest-framework.org/api-guide/fields/#date-and-time-fields
# https://www.django-rest-framework.org/api-guide/fields/#datetimefield
# end reference


class Comment:
    def __init__(self, email, content, created):  # created=None):
        self.email = email
        self.content = content
        # self.created = created or datetime.now()
        self.created = created


# playing with the Date/Time format and serialization. This is the crux of what I'm trying to deal with
a_datetime_string = '2021-12-12T12:00:14.858000'
# a_datetime_string = '2021-12-12T12:00:14'
# a_datetime_string = '2021-12-12XXX12:00:14.858000'


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    # created = serializers.DateTimeField(
    #     format=output_format,
    #     input_formats=input_formats,
    #     default_timezone=None)

    # created = serializers.DateField(
    #     format="%Y-%m-%d",
    #     input_formats=['%Y-%m-%d',])

    def create(self, validated_data):
        return Comment(**validated_data)  # if subclass of Serializer
        # return Comment.objects.create(**validated_data)  # if subclass of ModelSerializer

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        # instance.save()  # if subclass of ModelSerializer
        return instance


print("here")
print("settings.MY_DATETIME_FORMAT={}".format(settings.MY_DATETIME_FORMAT))

# Reference:  https://www.django-rest-framework.org/api-guide/serializers/#declaring-serializers

comment = Comment(email='leila@example.com', content='foo bar', created=a_datetime_string)
# construct serializer given object
serializer = CommentSerializer(comment)
# when constructed from an object, you can get a reference to the original object by using .instance
print('--constructed from object: type(serializer.instance)={}'.format(type(serializer.instance)))
print('--constructed from object: repr(serializer.instance)={}'.format(repr(serializer.instance)))
# when constructed from an object, you can immediately convert to serialized form using .data
print('--constructed from object: type(serializer.data)={}'.format(type(serializer.data)))
print('--constructed from object: repr(serializer.data)={}'.format(repr(serializer.data)))
# At this point we've translated the model instance into Python native datatypes. To finalise the serialization process we render the data into json.
from rest_framework.renderers import JSONRenderer
json_data = JSONRenderer().render(serializer.data)
print('--constructed from object: type(json_data)={}'.format(type(json_data)))
print('--constructed from object: repr(json_data)={}'.format(repr(json_data)))

# construct serializer given (native) data
# First we parse a stream into Python native datatypes...
import io
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json_data)
seed_data = JSONParser().parse(stream)
print('--constructed from data: type(seed_data)={}'.format(type(seed_data)))
print('--constructed from data: repr(seed_data)={}'.format(repr(seed_data)))

serializer = CommentSerializer(data=seed_data)
# when constructed from native data... you can get the original native data by using .initial_data
print('--constructed from data: type(serializer.initial_data)={}'.format(type(serializer.initial_data)))
print('--constructed from data: repr(serializer.initial_data)={}'.format(repr(serializer.initial_data)))
# calling is_valid() will establish .data property within the serializer
# additional information is in .errors property if this fails
if serializer.is_valid():
    print("--constructed from data: is_valid()=True,  serializer.errors={}".format(serializer.errors))
else:
    print("--constructed from data: is_valid()=False, serializer.errors={}".format(serializer.errors))
# verified_data = serializer.data
# # look at the verified data
# print('--constructed from data: type(serializer.data)={}'.format(type(serializer.data)))
# print('--constructed from data: repr(serializer.data)={}'.format(repr(serializer.data)))

# If we want to be able to return complete object instances based on the validated data we need to implement one or both of the .create() and .update() methods.
# If your object instances correspond to Django models you'll also want to ensure that these methods save the object to the database.
# Now when deserializing data, we can call .save() to return an object instance, based on the validated data.
comment = serializer.save()

# Calling .save() will either create a new instance, or update an existing instance, depending on if an existing instance was passed when instantiating the serializer class:
# .save() will create a new instance.
serializer = CommentSerializer(data=seed_data)
serializer.is_valid()
comment2 = serializer.save()
print('--create new instance:     (comment2 == comment) is expect=False, observed={}'.format(comment2==comment))

# .save() will update the existing `comment` instance.
serializer = CommentSerializer(comment, data=seed_data)
serializer.is_valid()
comment3 = serializer.save()  # should be the same as "comment"
print('--update current instance: (comment3 == comment) is expect=True, observed={}'.format(comment3==comment))



print('------------ moving along ------------')

from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
print("type(d)={}".format(type(d)))
print("d={}".format(d))
# Methods related to formatting string output

d.isoformat()
d.strftime("%d/%m/%y")
d.strftime("%A %d. %B %Y")
d.ctime()
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")

# Methods for to extracting 'components' under different calendars
t = d.timetuple()
for i in t:     
    print(i)
