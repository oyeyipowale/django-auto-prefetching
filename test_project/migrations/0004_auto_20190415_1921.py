# Generated by Django 2.2 on 2019-04-15 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("test_project", "0003_auto_20190415_1832")]

    operations = [
        migrations.CreateModel(
            name="ManyToManyModelTwo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("two_text", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="childb",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children_b",
                to="test_project.TopLevel",
            ),
        ),
        migrations.CreateModel(
            name="ManyToManyModelOne",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("one_text", models.TextField()),
                (
                    "model_two_set",
                    models.ManyToManyField(
                        related_name="model_one_set",
                        to="test_project.ManyToManyModelTwo",
                    ),
                ),
            ],
        ),
    ]
