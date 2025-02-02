from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Content, Resource, Event, Feedback
from .forms import FeedbackUpdateForm





class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'



# ======== CONTENT VIEWS ========

class ContentListView(ListView):
    model = Content
    template_name = 'content/content_list.html'
    context_object_name = 'contents'
    ordering = ['-created_at']


class ContentDetailView(DetailView):
    model = Content
    template_name = 'content/content_detail.html'
    context_object_name = 'content'

class ContentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Content
    fields = ['title', 'description', 'type']
    template_name = 'content/content_create.html'

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can add content


class ContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Content
    fields = ['title', 'description', 'type']
    template_name = 'content/content_update.html'

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can update content


class ContentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Content
    template_name = 'content/content_delete.html'
    success_url = reverse_lazy('content_list')

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can delete content


# ======== RESOURCE VIEWS ========

class ResourceListView(ListView):
    model = Resource
    template_name = 'resource/resource_list.html'
    context_object_name = 'resources'


class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'resource/resource_detail.html'
    context_object_name = 'resource'


class ResourceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Resource
    fields = ['name', 'description', 'resource_url', 'video']
    template_name = 'resource/resource_create.html'

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can add resources


class ResourceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resource
    fields = ['name', 'description', 'resource_url', 'video']
    template_name = 'resource/resource_update.html'

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can update resources


class ResourceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resource
    template_name = 'resource/resource_delete.html'
    success_url = reverse_lazy('resource_list')

    def test_func(self):
        return self.request.user.is_staff  # Only admin/staff can delete resources


# ======== EVENT VIEWS ========

class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'date']
    template_name = 'event/event_create.html'

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Automatically assign logged-in user as organizer
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'location', 'date']
    template_name = 'event/event_update.html'

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer or self.request.user.is_staff  # Organizer or admin can edit


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer or self.request.user.is_staff  # Organizer or admin can delete


# ======== FEEDBACK VIEWS ========

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback/feedback_list.html'
    context_object_name = 'feedbacks'
    ordering = ['-created_at']


class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback/feedback_detail.html'
    context_object_name = 'feedback'


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['resource', 'rating', 'comments']
    template_name = 'feedback/feedback_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign feedback to logged-in user
        return super().form_valid(form)


class FeedbackUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Feedback
    form_class = FeedbackUpdateForm  # Use the custom form
    template_name = 'feedback/feedback_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback'] = self.object
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'resource': self.object.resource}  # Pre-fill resource field as readonly
        return kwargs

    def form_valid(self, form):
        # Optionally, ensure that the resource is not modified
        # This is important if you don't want the user to change the resource
        form.instance.resource = self.object.resource  # Keep the original resource value
        return super().form_valid(form)

    def test_func(self):
        feedback = self.get_object()
        return self.request.user == feedback.user  # Only the owner can update their feedback


class FeedbackDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Feedback
    template_name = 'feedback/feedback_delete.html'
    success_url = reverse_lazy('feedback_list')

    def test_func(self):
        feedback = self.get_object()
        return self.request.user == feedback.user  # Only the owner can delete their feedback
