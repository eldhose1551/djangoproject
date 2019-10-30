from django import forms
from .models import Blogs


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            'title',
            'content',
            'image',
            # 'author',
            # 'created_on',
            # 'updated_on',
        ]


# class CommentForm(forms.ModelForm):
#     class Meta:
#         models = Blogs
#         fields = [
#             'name',
#             'email',
#             'website',
#             'message',
#             'date',
#         ]
