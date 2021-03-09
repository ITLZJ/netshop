from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=10)

    def __str__(self):
        return u'Category:%s' % self.cname


class GoodsDetailName(models.Model):
    """
    商品详细名字数据库表
    """
    gdname = models.CharField(max_length=30)

    def __str__(self):
        return u'GoodsDetailName:%s' % self.gdname


class Goods(models.Model):
    """
    商品名字数据库表
    """
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(verbose_name=u'原价',max_digits=5,decimal_places=2)
    price = models.DecimalField(verbose_name=u'现价',max_digits=5,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return u'Goods:%s' % self.gname

    # 获取商品大图
    def getGimg(self):
        return self.inventory_set.first().color.colorurl


    def getColorList(self):
        """
        获取商品所有的颜色，并且返回该商品的所有对象
        :return:
        """
        colorList = []
        for inventory in self.inventory_set.all():
            color = inventory.color
            if color not in colorList:
                colorList.append(color)
        return colorList

    def getSizeList(self):
        """
        获取所有尺寸
        :return:
        """
        sizeList = []
        for inventory in self.inventory_set.all():
            size = inventory.size
            if size not in sizeList:
                sizeList.append(size)
        return sizeList

    def getDetailList(self):
        # 创建有序字典用于存放详情信息 *k:详情名称 v:图片列表
        import collections
        datas = collections.OrderedDict()
        for goodsDetail in self.goodsdetail_set.all():
            gdname = goodsDetail.name()
            if gdname not in datas.keys():
                datas.update({gdname: [goodsDetail.gdurl]})
            else:
                datas[gdname].append(goodsDetail.gdurl)
        return datas




class GoodsDetail(models.Model):
    """
    商品详细信息
    """
    gdurl = models.ImageField(upload_to='')  # 当为空的时候该上传路径会直接传到系统配置的media路径当中
    gdname = models.ForeignKey(GoodsDetailName,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    def name(self):
        """
        获取详情名称
        :return:
        """
        return self.gdname.gdname

class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __str__(self):
        return u'Size:%s'%self.sname


class Color(models.Model):
    """
    商品颜色
    """
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __str__(self):
        return u'Color:%s'%self.colorname


class Inventory(models.Model):
    """
    仓库剩余量信息
    """
    count = models.PositiveIntegerField()  # 正整数
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)


