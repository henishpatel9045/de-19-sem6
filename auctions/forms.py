from django import forms
from .models import Listing, Bidding, Comment, Category

from django.utils.translation import gettext_lazy as _


class CustomImageWidget(forms.widgets.FileInput):
    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs["class"] = "custom-image-widget"
        super().__init__(attrs)


class CustomImageField(forms.ImageField):
    widget = CustomImageWidget(attrs={"accept": "image/*"})

    def use_required_attribute(self, initial):
        """
        Returns True if the field is required, False otherwise.

        This method is used to generate the 'required' attribute for the
        field's widget.
        """
        if self.required:
            return True
        # check if initial value is None or empty string
        if initial is not None and initial != "":
            return False
        return self.widget.is_required

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = _("Image")


CATEGORY = Category.objects.all().values_list("name", "name")
CATEGORY1 = {("", "")}

categories = []

for item in CATEGORY:
    categories.append(item)
for item in CATEGORY1:
    categories.append(item)


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        labels = {
            "productnames": "Productname",
            "descriptions": "Description",
            "startingbids": "Starting Bids",
            "images": "Image",
            "category": "Category",
        }
        fields = ["productnames", "descriptions", "startingbids", "images", "category",]
        widgets = {
            "category": forms.Select(
                choices=categories, attrs={"class": "form-control select form-control"}
            ),
            # "productnames": forms.TextInput(attrs={"class": "textinput textInput form-control"}),
            # "startingbids": forms.TextInput(attrs={"class": "numberinput form-control"}),
            # "images": forms.ImageField(required=False),
        }


class BiddingForm(forms.ModelForm):
    class Meta:
        model = Bidding
        labels = {"bidprice": ""}
        fields = ["bidprice"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {"comment": ""}
        fields = ["comment"]
