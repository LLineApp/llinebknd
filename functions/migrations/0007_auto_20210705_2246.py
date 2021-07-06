from django.db import migrations, connections


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0006_auto_20210410_1706'),
    ]

    db_schema = 'public.' if connections['default'].vendor == 'postgresql' else ''
    
    operations = [
        migrations.RunSQL(
            "INSERT INTO " + db_schema +
            "functions_profileadvisors (profile_id, advisor_id) " +
            "SELECT distinct id, financial_advisor_id " +
            "FROM " + db_schema + "functions_profile " +
            "WHERE financial_advisor_id IS NOT NULL"
        )]
