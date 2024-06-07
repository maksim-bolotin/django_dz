from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from blogpost.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_dealer = form.save()
            new_dealer.slag = slugify(new_dealer.title)
            new_dealer.save()
        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):
        if form.is_valid():
            new_dealer = form.save()
            new_dealer.slag = slugify(new_dealer.title)
            new_dealer.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogpost:detail', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost:list')
