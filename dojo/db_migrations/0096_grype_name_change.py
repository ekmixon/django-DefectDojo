from django.db import migrations


class Migration(migrations.Migration):
    def rename_grype_parser_name(self, schema_editor):
        test_type_model = self.get_model('dojo', 'Test_Type')

        if grype_testtype := test_type_model.objects.filter(
            name='anchore_grype'
        ).first():
            grype_testtype.name = 'Anchore Grype'
            grype_testtype.save()

    def reverse_rename_grype_parser_name(self, schema_editor):
        test_type_model = self.get_model('dojo', 'Test_Type')

        if grype_testtype := test_type_model.objects.filter(
            name='Anchore Grype'
        ).first():
            grype_testtype.name = 'anchore_grype'
            grype_testtype.save()

    dependencies = [
        ('dojo', '0095_remove_old_product_contact_fields'),
    ]

    operations = [migrations.RunPython(rename_grype_parser_name, reverse_rename_grype_parser_name)]
