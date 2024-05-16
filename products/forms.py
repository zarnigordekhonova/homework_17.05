from django.forms import ModelForm

from products.models import Reviews


class AddReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'star_given']

class ReviewUpdateForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'