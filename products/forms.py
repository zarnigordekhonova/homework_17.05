from django.forms import ModelForm
from products.models import Reviews



class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'