from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200319_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_one',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_two',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='experience',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password2',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='style',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]