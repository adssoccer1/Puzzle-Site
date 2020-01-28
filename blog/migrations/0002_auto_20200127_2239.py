# Generated by Django 2.2.9 on 2020-01-27 22:39

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

   

    operations = [
        migrations.AddField(
            model_name='post',
            name='_text_rendered',
            field=models.TextField(default='this is the default value', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='text_markup_type',
            field=models.CharField(blank=True, choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown')], default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
    ]
