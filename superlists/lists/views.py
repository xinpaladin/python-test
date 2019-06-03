from django.shortcuts import render, HttpResponse

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
    # if request.method == 'POST':
    #     return render(request,'home.html',{'new_item_text':request.POST['item_text'],})
    
    # return render(request, 'home.html')
