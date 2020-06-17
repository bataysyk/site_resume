import sched
import time

from django.shortcuts import render, redirect

from .models import PriceList




def report():
    while True:
        s = sched.scheduler(time.time, time.sleep)

        def print_time(a='default'):
            print("From print_time", time.time(), a)

        def print_some_times():
            print(time.time())

        s.enter(1, 1, print_time)
        s.enter(1, 2, print_time, argument=('positional',))
        s.enter(1, 1, print_time, kwargs={'a': 'keyword'})
        s.run()
        print(time.time())
        print_some_times()
        if time.time() == 1:
            break

# Create your views here.
def home(request):
    return render(request, "home.html")





def resume(request):

    return render(request, "resume.html")


def price_list_count(request, pk):
    '''Счетчик клика по ссылке скачать прайс лист.'''
    # try:
    #     price = get_object_or_404(PriceList, is_active=True)
    # except MultipleObjectsReturned:
    #     return HttpResponse('Вы выбрали более одного файла')
    price = PriceList.objects.get(pk=pk)
    price.counter += 1
    price.save()
    return redirect("/home/")  # return redirect(price.file.url)

