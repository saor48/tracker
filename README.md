cr  ud


------------------------------------------
def myFunction(request):
    myObj = MyObjectType()
    myObj.customParameter = parameterX
    ...
    myObj.save()
    
----------------------------
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    article = Article()
    article.title = 'This is the title'
    article.contents = 'This is the content'
    article.save()
    
    template = loader.get_template('articles/index.html')
    context = {
        'new_article_id': article.pk,
    }
    return HttpResponse(template.render(context, request))
    
--------------------------------------------


There is plenty of good guides online. 

https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Django has a sendmail library that you can use once you get your app started

https://docs.djangoproject.com/en/1.9/topics/email/

--------------------------..............................
class LocationForm(forms.ModelForm):

    auto_email_list = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Location
        exclude = ['id']
---------------------
    query = Issue(
        name = "new issue",
        description = "created in views",
        comment = "",
        category = "bug",
        date_issued = Date.today, 
        date_accepted = None,
        date_started = None,
        date_completed = None,
        price = None,
        )
    
    if request.method == "POST":
        query.save()
        return redirect(reverse('issues'))

