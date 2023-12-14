from django.shortcuts import render
from django.views.generic import View
from .models import Rating
from django.http import JsonResponse

class DoctorRating(View):
    def post(self, request):
        element_id = request.POST.get('el_id')
        val = request.POST.get('val')
        if self.request.user.is_authenticated:
            if not Rating.objects.filter(user=self.request.user, doctor_id=element_id):
                Rating.objects.create(doctor_id=element_id, score=val, user=self.request.user)
            else:
                rate = Rating.objects.get(user=self.request.user, doctor_id=element_id)
                rate.score = val
                rate.save()
            return JsonResponse({'success': 'true', 'score': val}, safe=False)

    def get(self, request):
        return JsonResponse({'success': 'False'})
