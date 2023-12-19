from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0003_auto_20180405_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
