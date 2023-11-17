from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.http import HttpRequest

def index(request):
    return render(request, "index.html")

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


def no_teen_sum(request):
    result = None
    if request.method == "GET":
        form = NoTeenSumForm(request.GET)
        if form.is_valid():
            numbers = [
                form.cleaned_data["a"],
                form.cleaned_data["b"],
                form.cleaned_data["c"],
            ]
            result = sum(n if n < 13 or n > 19 or n in [15, 16] else 0 for n in numbers)
    else:
        form = NoTeenSumForm()

    return render(request, "no_teen_sum.html", {"form": form, "result": result})


def xyz_there(request):
    def check_xyz(word):
        return "xyz" in word and not ".xyz" in word

    result = None
    if request.method == "GET":
        form = XyzThereForm(request.GET)
        if form.is_valid():
            word = form.cleaned_data["word"]
            result = check_xyz(word)
    else:
        form = XyzThereForm()

    return render(request, "xyz_there.html", {"form": form, "result": result})


def centered_average(request):
    def calculate_centered_average(nums):
        nums = sorted(nums)
        return sum(nums[1:-1]) // len(nums[1:-1])

    result = None
    if request.method == "GET":
        form = CenteredAverageForm(request.GET)
        if form.is_valid():
            numbers = form.cleaned_data["numbers"]
            numbers = list(map(int, numbers.split(',')))
            result = calculate_centered_average(numbers)
    else:
        form = CenteredAverageForm()

    return render(request, "centered_average.html", {"form": form, "result": result})