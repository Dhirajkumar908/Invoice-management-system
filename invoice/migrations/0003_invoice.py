# Generated by Django 4.2.7 on 2023-11-20 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('sub_total', models.IntegerField()),
                ('Client_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.product')),
            ],
        ),
    ]
