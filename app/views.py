from django.shortcuts import render
from app.forms import HeyYouForm, AgeInForm, OrderTotalForm, FontTimesForm
from django.http import HttpResponse
from django.http import HttpRequest


def hey_you(request):
    form = HeyYouForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "hey_you.html", {"form": form, "name": name})
    else:
        form = HeyYouForm()
        return render(request, "hey_you.html", {"form": form})


def age_in(request):
    form = AgeInForm(request.GET)
    if form.is_valid():
        year = form.cleaned_data["year"]
        BYear = form.cleaned_data["BYear"]
        age = int(year) - int(BYear)
        return render(
            request,
            "age_in.html",
            {"form": form, "age": age, "year": year, "BYear": BYear},
        )
    else:
        form = AgeInForm()
        return render(request, "age_in.html", {"form": form})


def order_total(request):
    form = OrderTotalForm(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
        return render(
            request,
            "order_total.html",
            {
                "form": form,
                "total": total,
                "burgers": burgers,
                "fries": fries,
                "drinks": drinks,
            },
        )
    else:
        form = OrderTotalForm()
        return render(request, "order_total.html", {"form": form})


def font_times(request):
    result = None
    if request.method == "GET":
        form = FontTimesForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data["text"]
            number = form.cleaned_data["number"]
            front = text[:3]
            result = front * number
    else:
        form = FontTimesForm()

    return render(request, "font_times.html", {"form": form, "result": result})
