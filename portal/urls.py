from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PostListView, PostView, HomeView, EventListView, EventView, BookListView, BookView, CourseListView, \
    CourseView, SearchView, PageView, ContactView

app_name = "portal"

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name="home-view"),

    # Portal
    path('portal/<slug:slug>', PageView.as_view(), name="page-view"),

    # Postagem
    path('noticias/', PostListView.as_view(), name="post-list-view"),
    path('noticia/<str:publication_date>/<slug:slug>', PostView.as_view(), name="post-view"),

    # Evento
    path('eventos/', EventListView.as_view(), name="event-list-view"),
    path('evento/<slug:slug>', EventView.as_view(), name="event-view"),

    # Livro
    path('livros/', BookListView.as_view(), name="book-list-view"),
    path('livro/<slug:slug>', BookView.as_view(), name="book-view"),

    # Curso
    path('cursos/', CourseListView.as_view(), name="course-list-view"),
    path('curso/<slug:slug>', CourseView.as_view(), name="course-view"),

    # Busca
    path('busca/', SearchView.as_view(), name="search-view"),

    # Contato
    path('contato/', ContactView.as_view(), name="contact-view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
