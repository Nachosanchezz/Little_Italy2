from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('healthLabels', models.TextField()),
                ('cuisineType', models.TextField()),
                ('calories', models.FloatField()),
                ('totalNutrients', models.JSONField()),
                ('ingredients', models.TextField()),
            ],
        ),
    ]