from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0006_auto_20180406_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
