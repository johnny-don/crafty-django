from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200319_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]