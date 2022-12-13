from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'shop'

urlpatterns = [

    # path('comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
    # path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single'),
    # path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    # path('', cache_page(15 * 60)(HomeView.as_view()), name='home'),
    # path('', HomeView.as_view(), name='home'),
    path('test/', tester, name='test_url'),
    path('gender/', gender_change, name='gender_url'),
    path('', top_viev, name='home')
]