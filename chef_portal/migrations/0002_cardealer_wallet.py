from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardealer',
            name='wallet',
            field=models.IntegerField(default=0),
        ),
    ]
