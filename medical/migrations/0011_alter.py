from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0010_drop_views'),
    ]
    operations = [
       migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(db_column='ItemCode', max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='code',
            field=models.CharField(db_column='ServCode', max_length=50),
        ),

                  ]