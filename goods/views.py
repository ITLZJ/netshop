from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from goods.models import *
from django.core.paginator import Paginator

class ShowIndex(View):
    def get(self, request, cid=2, num=1):
        cid = int(cid)
        num = int(num)
        # 查询所有类别信息
        categorys = Category.objects.all().order_by('id')

        # 查询当前类别下的商品所有信息
        goodsList = Goods.objects.filter(category_id=cid).order_by('id')

        # 每页显示八条记录
        pager = Paginator(object_list=goodsList,per_page=8)

        # 获取当前页的数据
        page_goodsList = pager.page(num)

        return render(request, 'index.html', {'categorys': categorys, 'goodsList': page_goodsList, 'currentid': cid})


class DetailView(View):
    def get(self, request, goodsid):
        goodsid = int(goodsid)
        # 根据goodsid查询商品的详情信息，获取goods对象
        goods = Goods.objects.get(id=goodsid)
        return render(request,'detail.html',{'goods':goods})



