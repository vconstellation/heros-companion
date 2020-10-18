from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Category, Thread, Post
from .forms import ThreadCreateForm, PostCreateForm



class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'forum/forum.html'
    paginate_by = 20

class ThreadListView(ListView):
    model = Thread
    context_object_name = 'threads'
    paginate_by = 10
    template_name = 'forum/threads.html'

    def get_context_data(self, **kwargs):
        kwargs['categories'] = self.category
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        queryset = self.category.threads.order_by('-last_updated')
        return queryset


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'forum/posts.html'

    def get_context_data(self, **kwargs):
        self.thread.views += 1
        self.thread.save()
        kwargs['thread'] = self.thread
        return super().get_context_data(**kwargs)


    def get_queryset(self):
        self.thread = get_object_or_404(Thread, category__pk=self.kwargs.get('pk'), pk=self.kwargs.get('thread_pk'))
        queryset = self.thread.posts.order_by('created_at')
        return queryset


class NewThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadCreateForm

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.thread_author = self.request.user
        thread.last_updated = timezone.now()
        thread.category = Category.objects.get(pk=self.kwargs['pk'])
        thread.save()
        return redirect('threads', pk=thread.category.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get(pk=self.kwargs['pk'])
        return context


class ReplyCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'forum/reply_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        cat_pk = Category.objects.get(pk=self.kwargs['pk'])
        cat_pk = cat_pk.pk
        thr_pk = Thread.objects.get(pk=self.kwargs['thread_pk'])
        thr_pk = thr_pk.pk
        post.thread = Thread.objects.get(category__pk=cat_pk, pk=thr_pk)
        post.post_author = self.request.user
        post.created_at = timezone.now()
        form.save()
        return redirect('posts', pk=cat_pk, thread_pk=thr_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['threads'] = Thread.objects.get(pk=self.kwargs['thread_pk'])
        return context

