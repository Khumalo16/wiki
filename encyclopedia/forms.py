from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title",required = True,
            help_text="<p class='text-secondary'>Please refer <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>",
            widget= forms.TextInput
            (attrs={'placeholder':'Enter Title','class':'col-sm-30','style':'bottom:1rem'}))

    content = forms.CharField(label="Type in the big space provided below and press submit bottomn", required=False, 
              widget= forms.Textarea 
              (attrs={
                      "class": "text areaa",
                      "rows": 2, 
                      "cols": 2}),
              help_text="<p class='text-secondary'>Please refer <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>")

class EditPageForm(forms.Form):
    pagename = forms.CharField(label="Title",disabled = False,required = False,
    widget= forms.HiddenInput
    (attrs={'class':'col-sm-12','style':'bottom:1rem'}))
   
    body = forms.CharField(label="Markdown content",help_text="<p class='text-secondary'>Please refer <a class='text-info' href = https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax> GitHub’s Markdown guide</a> </p>",
    widget= forms.Textarea
    (attrs={"rows":20, "cols":80,'class':'col-sm-11','style':'top:2rem'}))
