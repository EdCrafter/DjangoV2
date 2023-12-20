from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0002_auto_20180405_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chef_portal.CarDealer'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chef_portal.Vehicles'),
        ),
    ]
