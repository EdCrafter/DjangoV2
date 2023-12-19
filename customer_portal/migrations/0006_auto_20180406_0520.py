from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0005_auto_20180406_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.Vehicles'),
        ),
    ]
