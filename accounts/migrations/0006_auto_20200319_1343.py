from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200319_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]