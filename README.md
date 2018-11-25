cr  ud

-----------------------------------
obj = Class.objects.get(pk=this_object_id)
form = JournalForm(initial={'tank': 123})
form = SomeModelForm(request.POST or None, initial={"option": "10"})
<a href="{% url 'checkout' %}" class="btn btn-success" role="button">
        <span class="glyphicon glyphicon-ok-sign" aria-hidden="true">Checkout</span>
    </a>
    
-------------------------
Use the queryset object update method:

MyModel.objects.filter(pk=some_value).update(field1='some value')
----------------------------
def my_view(request):

    if request.method == 'POST':
        print request.POST.get('my_field')

        form = MyForm(request.POST)

        print form['my_field'].value()
        print form.data['my_field']

        if form.is_valid():

            print form.cleaned_data['my_field']
            print form.instance.my_field

            form.save()
            print form.instance.id  # now this one can access id/pk

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

