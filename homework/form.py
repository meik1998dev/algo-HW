from django import forms

class TextFileForm(forms.Form):
    text_file = forms.FileField(label=' task file', help_text='Upload a text file')

    def clean_text_file(self):
        file = self.cleaned_data['text_file']
        if not file.name.endswith('.txt'):
            raise forms.ValidationError('File must be a text file')
        return file

