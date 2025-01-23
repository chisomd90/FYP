from django.db import migrations, models

def add_plaintiff_column(apps, schema_editor):
    Case = apps.get_model('cases', 'Case')
    field = models.CharField(max_length=255, null=True)
    field.contribute_to_class(Case, 'plaintiff')
    Case.objects.all().update(plaintiff='')  # Set a default or leave it empty

class Migration(migrations.Migration):
    dependencies = [
        ('cases', '0001_initial'),  # Reference the correct last migration
    ]

    operations = [
        migrations.RunPython(add_plaintiff_column),
    ]
