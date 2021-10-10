from django import  forms


class EmailSender(forms.Form):
    receiver_email=forms.EmailField()
    SUBJECT=forms.CharField()
    TEXT=forms.CharField()
    date=forms.IntegerField(max_value=31)
    hour=forms.IntegerField(max_value=24)
    minute=forms.IntegerField(max_value=60)

    def __init__(self, *args, **kwargs):
        super(EmailSender, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
