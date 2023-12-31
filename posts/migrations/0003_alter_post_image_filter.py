# Generated by Django 3.2.19 on 2023-08-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('makeup', 'bath'), ('highend', 'budget'), ('lipgloss', 'eyes'), ('perfume', 'nails'), ('brushes', 'lightweight'), ('fullcoverage', 'full-coverage'), ('foundation', 'love'), ('hate', 'lasting'), ('good', '24hour')], default='normal', max_length=32),
        ),
    ]
