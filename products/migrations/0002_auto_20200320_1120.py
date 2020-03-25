
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='wood',
            field=models.CharField(max_length=50),
        ),
    ]