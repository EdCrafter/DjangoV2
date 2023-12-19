from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0004_orders_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.Vehicles', unique=True),
        ),
    ]
