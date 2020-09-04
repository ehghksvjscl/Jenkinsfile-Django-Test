from django.views     import View
from django.http      import JsonResponse

class SampleView(View):
    def get(self,request):
        return JsonResponse({"message":"Hello word"},status=200)