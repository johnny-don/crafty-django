from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200319_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_one',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_two',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='style',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wood_source',
            field=models.BooleanField(),
        ),
    ]