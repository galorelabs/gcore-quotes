from django.http import JsonResponse
import zenquotespy



def quotes(request):
  quote = zenquotespy.random() 
  return JsonResponse({"message": quote })
