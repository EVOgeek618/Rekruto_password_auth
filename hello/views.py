from django.http import HttpResponse
import random
def hello(request):
    return HttpResponse(random.sample(range(10), 4))