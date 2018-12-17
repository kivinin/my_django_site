from django.http import HttpResponse
def post_list(request):
 html = "<html><body><H1>Первое представление на джанго выполнилось</H1></body></html>"
 return HttpResponse(html)
