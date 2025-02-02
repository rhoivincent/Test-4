from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomePageView, AboutPageView, ContactPageView,
    ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView,
    ResourceListView, ResourceDetailView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    FeedbackListView, FeedbackDetailView, FeedbackCreateView, FeedbackUpdateView, FeedbackDeleteView
)

urlpatterns = [
    # Home, About, Contact
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # Content URLs
    path('content/', ContentListView.as_view(), name='content_list'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
    path('content/new/', ContentCreateView.as_view(), name='content_create'),
    path('content/<int:pk>/edit/', ContentUpdateView.as_view(), name='content_update'),
    path('content/<int:pk>/delete/', ContentDeleteView.as_view(), name='content_delete'),

    # Resource URLs
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('resources/new/', ResourceCreateView.as_view(), name='resource_create'),
    path('resources/<int:pk>/edit/', ResourceUpdateView.as_view(), name='resource_update'),
    path('resources/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource_delete'),

    # Event URLs
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/new/', EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    # Feedback URLs
    path('feedback/', FeedbackListView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedback/new/', FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedback/<int:pk>/edit/', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
