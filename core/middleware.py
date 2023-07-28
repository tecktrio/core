from django.http import JsonResponse


class Authentication(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        access_token = request.GET.get('key')
        response            = self.get_response(request)
        if access_token == 'widecitymakesitsimple':
            return response
        else:
            return JsonResponse({'status':'failed','error':'invalid api key'})