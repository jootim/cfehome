from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, FormView, DeleteView, UpdateView

from .forms import SecondForm
from .models import Reviews



class ReviewListView(ListView):
    template_name = 'review_list.html'
    model = Reviews
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data =base_query.filter(rating__gt=3)
        return data.order_by('rating')


class ReviewDetailView(DetailView):
    template_name = 'review_detail.html'
    model = Reviews
    context_object_name = 'review'


class ReviewCreateView(FormView):
    template_name = 'review_form.html'
    form_class = SecondForm
    success_url = "/reviews"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class ReviewDeleteView(DeleteView):
    template_name = 'review_delete.html'
    model = Reviews
    context_object_name = 'review'
    success_url = "/reviews"

class ReviewUpdateView(UpdateView):
    template_name = 'review_update.html'
    model = Reviews
    context_object_name = 'review'
    success_url = "/reviews"
    # class ReviewDetailView(TemplateView):
    #     template_name = 'review_detail.html'
    #
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         review_id = kwargs['id']
    #         review = Reviews.objects.get(pk=review_id)
    #         context['review'] = review
    #         return context

