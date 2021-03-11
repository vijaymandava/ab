from datetime import datetime
from rest_framework import serializers

# $Env:DJANGO_SETTINGS_MODULE=lims_server/lims_server/settings_standalone.py
# >>> from  infrastructure.z_practice_4_lims_server.project.lims_server.app_sm_rx.zona_comment import Comment
# >>> from  infrastructure.z_practice_4_lims_server.project.lims_server.app_sm_rx.zona_comment import CommentSerializer
# comment = Comment(email='leila@example.com', content='foo bar')
# serializer = CommentSerializer(comment)
# serializer.data


# zona - exapmle
class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)

    the_datetime_format = '%d/%m/%Y %l:%M:%S'  # as observed: "1/4/2021 11:24:12 PM"}'

    # created = serializers.DateTimeField(
        # # format=the_datetime_format,
        # # input_formats=[
        # #     the_datetime_format
        # # ],
        # default_timezone=None)

    created = serializers.DateTimeField(
        format=the_datetime_format,
        input_formats=[
            the_datetime_format
        ],
        default_timezone=None)
