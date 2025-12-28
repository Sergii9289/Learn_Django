from django.urls import path
from . import views  # Імпортуємо наші представлення

app_name = 'books'

urlpatterns = [
    # path('', views.book_list, name='book_list'),  # Відображення списку книг
    # path('<int:pk>/', views.book_detail, name='book_detail'),  # Деталі книги
    # path('add/', views.book_add, name='book_add'),  # Додавання книги
    # path('genre/<str:genre>/year/<int:year>/', views.book_filter, name='book_filter'),
]