from django.shortcuts import render
from app.forms import AddForm, HeyYouForm
from django.http import HttpResponse


def root(request):
    print(request.POST)
    return render(request, "root.html")


def add(request):
    form = AddForm(request.GET)
    if form.is_valid():
        x = form.cleaned_data["x"]
        y = form.cleaned_data["y"]
        answer = x + y
        return render(
            request, "add.html", {"form": form, "x": x, "y": y, "answer": answer}
        )
    else:
        return render(request, "add.html", {"form"})


def hey_you(request):
    name = HeyYouForm(request.GET)
    if request.method == 'POST':
        form = HeyYouForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['name']
    else:
        form = HeyYouForm()

    return render(request, 'hey_you.html', {'form': form, 'name': name})