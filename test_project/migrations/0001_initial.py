# Generated by Django 2.2 on 2019-04-15 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChildA",
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
                ("childA_text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="TopLevel",
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
                ("top_level_text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ChildB",
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
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_project.TopLevel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChildABro",
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
                (
                    "sibling",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_project.ChildA",
                    ),
                ),
            ],
        ),
    ]
