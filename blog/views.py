from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Photos, Comments
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from blog.forms import RegisterUserForm, LoginUserForm, CommentForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.db.models import Q



def home(request):
    id = 1
    post_home = Posts.objects.get(pk=id)
    photos = Photos.objects.filter(post_id=id)
    context = {'home': post_home, 'photos': photos}
    return render(request, 'blog/home.html', context=context)

class Story(ListView):
    model = Posts
    template_name = 'blog/story.html'
    context_object_name = 'posts'

def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    photos = Photos.objects.filter(post__slug=post_slug, is_published=True)
    comment = Comments.objects.filter(post__slug=post_slug, is_published=True)
    if  request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.post = post
            form.save()
            return redirect('blog:post', post_slug)
    else:    
        form = CommentForm()
    context = {'post': post, 'photos': photos, 'comments': comment, 'form': form}
    return render(request, 'blog/post.html', context=context)


def photo_gallery(request):
    photos = Photos.objects.all()
    context = {'photos': photos}
    return render(request, 'blog/photo_gallery.html', context=context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blog:home') 

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(sefl):
        return reverse_lazy('blog:home')

def logout_user(request):
    logout(request)
    return redirect('blog:login')


def search(request):
    search_query = request.GET.get('search', '')
    posts = None
    if search_query != '':
        posts = Posts.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    return render(request, 'blog/search.html', context={'posts': posts})
