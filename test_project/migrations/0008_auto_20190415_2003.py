# Generated by Django 2.2 on 2019-04-15 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("test_project", "0007_auto_20190415_2003")]

    operations = [
        migrations.RenameField(
            model_name="deeplynestedparent", old_name="cars", new_name="car"
        )
    ]
