# Generated by Django 3.2.9 on 2021-11-23 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0002_auto_20211110_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='backend.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_default', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(choices=[('usd', 'USD'), ('eur', 'EUR'), ('da', 'DA')], max_length=255)),
                ('change', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('featured', 'Featured'), ('new', 'New'), ('hot', 'Hot')], max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('shipping_address', models.CharField(max_length=255)),
                ('shipping_date', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('total_tax', models.FloatField(default=0)),
                ('shipping', models.FloatField(default=0)),
                ('total_price', models.FloatField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('comming', 'Comming'), ('completed', 'Completed')], max_length=255)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='backend.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('featured', 'Featured'), ('new', 'New'), ('hot', 'Hot')], max_length=255)),
                ('price', models.FloatField(blank=True, null=True)),
                ('shipping_price', models.FloatField(default=0)),
                ('tax', models.FloatField(default=0)),
                ('description', models.TextField()),
                ('discount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_main', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='backend.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='backend.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(to='backend.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='foodoffer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='foodoffer',
            name='option',
        ),
        migrations.RemoveField(
            model_name='foodoffer',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='adress',
        ),
        migrations.AddField(
            model_name='category',
            name='brief',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
        migrations.DeleteModel(
            name='FoodOffer',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='backend.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.currency'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
