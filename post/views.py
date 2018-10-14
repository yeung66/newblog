from django.shortcuts import render
from post.models import Article
from django.db.models import Count

# Create your views here.
def index(request):
    all_articles = Article.objects.all()
    return render(request,'index.html',{'articles':all_articles,'recommand':get_recommand(),'types':get_type()})

def article(requset,blog_id):
    a = Article.objects.filter(id=blog_id).first()
    a.see_count+=1
    a.save()
    next = Article.objects.filter(id__gt=blog_id).first()
    previous = Article.objects.filter(id__lt=blog_id).last()
    return render(requset,'info.html',{'article':a,'previous':previous,'next':next,'recommand':get_recommand(),'types':get_type()})

def get_recommand():
    return Article.objects.all().order_by('see_count')[:10]

def get_type():
    return Article.objects.values('type').annotate(Count('id'))