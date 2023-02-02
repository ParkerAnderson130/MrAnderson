from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Post
from .filters import PostFilter
from .forms import ContactForm

def home(request):
    posts = Post.objects.all().order_by('-pk')[0:2]
    return render(request, 'index.html', {'post': posts})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)