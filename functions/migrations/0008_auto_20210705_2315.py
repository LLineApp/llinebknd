from django.db import migrations, connections


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0007_profileadvisors_main_advisor'),
    ]

    db_schema = 'public.' if connections['default'].vendor == 'postgresql' else ''
    
    operations = [
        migrations.RunSQL(
            "UPDATE " + db_schema + "functions_profileadvisors SET main_advisor = TRUE"
        )]
