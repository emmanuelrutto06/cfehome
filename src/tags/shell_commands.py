(InteractiveConsole)
from tags.models import Tag
Tag.objects.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
 Tag.objects.last()
<Tag: Black>
 black = Tag.objects.last()
 black.title
'Black'
 black.slug
'black'
black.active
True
 black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0
x0000000003F1BC50>
 black.products.all()
<ProductQuerySet [<Product: T.shirt>, <Product: hat>, <Product: T.shirt>]>
 black.products.all().first()
<Product: T.shirt>
 exit()
(cfehome) PS C:\Users\rutto\dev\cfehome\src> python manage.py shell
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
 from products.models import Product
 qs = Product.objects.all()
 qs
<ProductQuerySet [<Product: T.shirt>, <Product: hat>, <Product: supercomputer>, <Product: T.shirt>, <Product: Lorem ipsu
m>]>
 tshirt = qs.first()
 tshirt
<Product: T.shirt>
 tshirt.title
'T.shirt'
 tshirt.description
'This t.shirt is awesome buy it :)'
 tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0
x0000000004086F98>
tshirt.tag_set.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Black>]>
 tshirt.tag_set.filter(title__iexact='Black')
<QuerySet [<Tag: Black>]>
tshirt.tag_set.filter(title__icontains='black')
