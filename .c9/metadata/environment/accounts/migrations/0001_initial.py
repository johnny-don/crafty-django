{"filter":false,"title":"0001_initial.py","tooltip":"/accounts/migrations/0001_initial.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":29,"column":5},"action":"insert","lines":["from django.db import migrations, models","","","class Migration(migrations.Migration):","","    initial = True","","    dependencies = [","    ]","","    operations = [","        migrations.CreateModel(","            name='UserRegistration',","            fields=[","                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),","                ('first_name', models.CharField(max_length=12)),","                ('last_name', models.CharField(max_length=12)),","                ('username', models.CharField(max_length=150)),","                ('address_one', models.CharField(max_length=100)),","                ('address_two', models.CharField(blank=True, max_length=100)),","                ('city', models.CharField(max_length=50)),","                ('email', models.EmailField(max_length=254)),","                ('password1', models.CharField(max_length=15)),","                ('password2', models.CharField(max_length=15)),","                ('experience', models.CharField(max_length=300)),","                ('style', models.CharField(max_length=200)),","                ('wood_source', models.BooleanField(default=True)),","            ],","        ),","    ]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":29,"column":5},"end":{"row":29,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585146804335,"hash":"1a493bfb462099453f993f01b81178063b50ab0f"}