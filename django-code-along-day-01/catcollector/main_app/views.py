import os
import boto3
import uuid

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Cat, Toy, Photo
from .forms import FeedingForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# this will work for function
from django.contrib.auth.decorators import login_required

# this works for class based views
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# http://localhost:8000
def home(request):
    return render(request, "home.html")


# http://localhost:8000/about-us/
def about_us(request):
    return render(request, 'about.html')


# http://localhost:8000/cats/
@login_required
def cat_index(request):
    # select * from table_name
    # cats = Cat.objects.all()  # this will return a list of cats
    # SELECT name, age ... FROM cats WHERE user_id = id
    cats = Cat.objects.filter(user=request.user)
    return render(request, 'cats/index.html', {'cats': cats})


# http://localhost/cats/1/
@login_required
def cats_detail(request, cat_id):
    # select name, description from table_name where
    # id = cat_id
    cat = Cat.objects.get(id=cat_id)
    # 10 in [10, 20, 30, 40]
    # cat.toys.all().values() means give me all the fields
    # cat.toys.all().values_list('id') give me list of ids
    # cat.toys.all().values_list('id') = [1, 2, 3, 4]
    # Toy.objects.exclude = [1, 2, 3, 10, 11, 12, 14]
    # id__in means  [1, 2, 3, 10, 11, 12, 14] in [1, 2, 3, 4]
    t = cat.toys.all().values_list('id')
    # print(f"top {t}")
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=t)
    # print(f"here ===> {toys_cat_doesnt_have}")
    feeding_form = FeedingForm()
    return render(
        request,
        'cats/detail.html',
        {'cat': cat, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have}
    )


# http://localhost:8000/cats/2/add_feeding/
@login_required
def add_feeding(request, cat_id):
    # print(request.POST['date'])
    # print(request.POST['meal'])
    # print(request.POST['csrfmiddlewaretoken'])
    form = FeedingForm(request.POST)
    if form.is_valid():
        # commit=False because we need to assign a cat id
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        print(new_feeding)
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    # fields = '__all__'
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        # self.request.user means current logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # self.object.id = 9
        # http://127.0.0.1:8000/cats/9
        # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    # fields = '__all__'
    fields = ['description', 'age']

    def get_success_url(self, **kwargs):
        # self.object.id = 9
        # http://127.0.0.1:8000/cats/9
        # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        return reverse('detail', args=(self.object.id,))


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = '/cats/'


# http://localhost:8000/toys/
class ToyList(LoginRequiredMixin, ListView):
    model = Toy


# http://localhost:8000/toys/1/
class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy


# http://localhost:8000/toys/create/
class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'


# http://localhost:8000/toys/1/update/
class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']


# http://localhost:8000/toys/1/delete/
class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'


@login_required
def assoc_toy(request, cat_id, toy_id):
    # SELECT name FROM cats WHERE id=cat_id
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    # redirect need two params
    # 1. the URL name
    # 2. if there is an id, you need to pass it
    # path('cats/<int:cat_id>/', views.cats_detail, name='detail')
    # http://localhost:8000/cats/1/
    return redirect('detail', cat_id=cat_id)


# Add this import to access the env vars

...


@login_required
def add_photo(request, cat_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
              photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # Saving the image
            Photo.objects.create(url=url, cat_id=cat_id)
        except:
            print('An error occured while uploading to s3')
    return redirect("detail", cat_id=cat_id)


def some_function(request):
    secret_key = os.environ['SECRET_KEY']


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save the user to the db
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # this is our HTML form for the template
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)
