from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task



# Create your views here.
class task_list(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "Tasks"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        search_input = self.request.GET.get('search','')
        if search_input !='':
            queryset = queryset.filter(
                title__startswith=search_input
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search', '')
        context['search_input'] = search_input
        #context['count'] = context['tasks'].filter(complete=False).count()
        return context



class task_detail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "Task"
    queryset = Task.objects.all()


class task_create(LoginRequiredMixin, CreateView):
    model = Task
    fields = {'complete', 'title', 'description'}
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user field to the currently logged-in user
        return super(task_create, self).form_valid(form)


class task_update(LoginRequiredMixin, UpdateView):
    model = Task
    fields= {'title', 'description', 'complete'}
    success_url = reverse_lazy('tasks')


class delete_view(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

