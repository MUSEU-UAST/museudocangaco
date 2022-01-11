from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView

from .models.book import Book
from .models.course import Course
from .models.event import Event
from .models.post import Post


def get_sidebar_content(context):
    context["post_list"] = Post.get_recent()[0:4]
    context["book_list"] = Book.objects.all()[0:3]
    return context


class PostListView(ListView):
    template_name = "portal/post/list.html"
    model = Post
    context_object_name = "post_list"
    paginate_by = 8

    def get_queryset(self):
        return Post.get_news()


class PostView(DetailView):
    template_name = "portal/post/view.html"
    model = Post
    context_object_name = "post"

    def get_queryset(self):
        return Post.get_news()

    def get_context_data(self, **kwargs):
        return get_sidebar_content(super(PostView, self).get_context_data())


class PageView(DetailView):
    template_name = "portal/post/view.html"
    model = Post

    def get_queryset(self):
        queryset = Post.objects.filter(category__iexact="P")
        return queryset

    def get_context_data(self, **kwargs):
        return get_sidebar_content(super(PageView, self).get_context_data())


class EventListView(ListView):
    template_name = "portal/event/list.html"
    model = Event
    context_object_name = "event_list"
    paginate_by = 16


class EventView(DetailView):
    template_name = "portal/event/view.html"
    model = Event
    context_object_name = "event"


class ContactView(TemplateView):
    template_name = "portal/contact.html"


class BookListView(ListView):
    template_name = "portal/book/list.html"
    model = Book
    context_object_name = "book_list"
    paginate_by = 16


class BookView(DetailView):
    template_name = "portal/book/view.html"
    model = Book
    context_object_name = "book"


class CourseListView(ListView):
    template_name = "portal/course/list.html"
    model = Course
    context_object_name = "course_list"
    paginate_by = 8


class CourseView(DetailView):
    template_name = "portal/course/view.html"
    model = Course
    context_object_name = "course"


class SearchView(TemplateView):
    template_name = "portal/search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET.get("search", "")
        default_filter = Q(title__icontains=search, description__icontains=search)
        context["post_list"] = Post.get_news().filter(title__icontains=search, subtitle__icontains=search)[0:8]
        context["book_list"] = Book.objects.filter(default_filter)[0:8]
        context["course_list"] = Course.objects.filter(default_filter)[0:8]
        context["event_list"] = Event.objects.filter(default_filter)[0:8]
        return context


class HomeView(TemplateView):
    template_name = "portal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["post_list"] = Post.get_recent()
        context["event_list"] = Event.objects.all()
        context["course_list"] = Course.objects.all()
        context["book_list"] = Book.objects.all()
        return context
