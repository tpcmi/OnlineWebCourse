# Generated by Django 3.2.10 on 2022-10-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_alter_courseorg_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='logo',
            field=models.ImageField(upload_to='CourseOrg/', verbose_name='logo'),
        ),
    ]