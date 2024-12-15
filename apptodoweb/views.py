from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import TodoForm
from .models import Model_ToDoWeb
from django.contrib import messages

class MainView(TemplateView):
    template_name = "apptodoweb/index.html"

def index(request):

    item_list = Model_ToDoWeb.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    print(page)
    return render(request, 'apptodoweb/index.html', page)



### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Model_ToDoWeb.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('index')