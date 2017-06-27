from django.db import models
class CategoriesFirst(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название раздела")
    slug = models.CharField(max_length = 50, verbose_name = "Ссылка")
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Раздел"

class CategoriesSecond(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название категории")
    slug = models.CharField(max_length = 50, verbose_name = "Ссылка")
    section = models.ForeignKey(CategoriesFirst)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Категория"

class Brand(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название категории")
    slug = models.CharField(max_length = 50, verbose_name = "Ссылка")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Брэнды"

class Product(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Название товара")
    description = models.TextField(verbose_name = "Описание")
    brand = models.ForeignKey(Brand)
    size = models.CharField(max_length = 50, verbose_name = "Размер")
    compound = models.CharField(max_length = 100, verbose_name = "Состав")
    price = models.DecimalField(decimal_places = 2, max_digits = 6, verbose_name = "Цена")
    count = models.IntegerField(default = 0, verbose_name = "Количество")
    land = models.CharField(max_length = 50, verbose_name = "Страна производитель")
    image = models.ImageField(upload_to = 'img', verbose_name = "Изображение товара")
    category = models.ForeignKey(CategoriesSecond)
    views = models.IntegerField(default = 0, verbose_name = "Просмотры", blank = True)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Продукты"

class Order(models.Model):
    last_name = models.CharField(max_length = 256, verbose_name="Фамилия")
    first_name = models.CharField(max_length = 256, verbose_name="Имя")
    two_name = models.CharField(max_length = 256, verbose_name="Отчество")
    phone = models.CharField(max_length = 256, verbose_name="Фамилия")
    stat = models.CharField(max_length = 256, verbose_name="Город")
    street = models.CharField(max_length = 256, verbose_name="Улица")
    house = models.CharField(max_length = 256, verbose_name="Дом")
    index = models.CharField(max_length = 256, verbose_name="Индекс")
    att = models.TextField(verbose_name="Примечания")
    product = models.TextField(verbose_name="Товары")

    def __str__ (self):
        return self.last_name + " " + self.first_name + " " + self.two_name
    class Meta:
        verbose_name_plural = "Заказы"
