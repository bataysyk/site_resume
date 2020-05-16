from django.shortcuts import render, redirect
from .models import PriceList

# Create your views here.
def home(request):
    return render(request, "home.html")

def price_list_count(request, pk):
    '''Счетчик клика по ссылке скачать прайс лист.'''
    # try:
    #     price = get_object_or_404(PriceList, is_active=True)
    # except MultipleObjectsReturned:
    #     return HttpResponse('Вы выбрали более одного файла')
    price = PriceList.objects.get(pk=pk)
    price.counter += 1
    price.save()
    return redirect("/home/")                                          #return redirect(price.file.url)