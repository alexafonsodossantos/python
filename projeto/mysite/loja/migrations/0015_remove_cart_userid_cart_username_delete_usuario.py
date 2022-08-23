# Generated by Django 4.1 on 2022-08-23 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loja', '0014_rename_user_id_cart_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='userid',
        ),
        migrations.AddField(
            model_name='cart',
            name='username',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
