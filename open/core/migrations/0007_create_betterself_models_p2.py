# Generated by Django 2.2.13 on 2020-07-06 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import open.utilities.date_and_time
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0006_betterself_basic_models_v2"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                ("name", models.CharField(max_length=300)),
                ("is_significant_activity", models.BooleanField(default=False)),
                ("is_negative_activity", models.BooleanField(default=False)),
                ("is_all_day_activity", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["name"], "unique_together": {("name", "user")},},
        ),
        migrations.AddField(
            model_name="ingredient", name="notes", field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="ingredientcomposition",
            name="notes",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="usersupplementstack",
            name="notes",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="usersupplementstackcomposition",
            name="notes",
            field=models.TextField(default=""),
        ),
        migrations.CreateModel(
            name="SleepLog",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("api", "Api"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                            ("mobile", "Mobile"),
                            ("web", "Web"),
                            ("user_excel", "User_Excel"),
                            ("text_message", "Text_Message"),
                        ],
                        max_length=50,
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Sleep Log",
                "verbose_name_plural": "Sleep Logs",
                "ordering": ["user", "-end_time"],
            },
        ),
        migrations.CreateModel(
            name="WellBeingLog",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                (
                    "time",
                    models.DateTimeField(
                        default=open.utilities.date_and_time.get_utc_now
                    ),
                ),
                ("mental_value", models.PositiveSmallIntegerField()),
                ("physical_value", models.PositiveSmallIntegerField()),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("api", "Api"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                            ("mobile", "Mobile"),
                            ("web", "Web"),
                            ("user_excel", "User_Excel"),
                            ("text_message", "Text_Message"),
                        ],
                        default="web",
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Well Being Log",
                "verbose_name_plural": "Well Being Logs",
                "ordering": ["user", "-time"],
                "unique_together": {("user", "time")},
            },
        ),
        migrations.CreateModel(
            name="SupplementLog",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("api", "Api"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                            ("mobile", "Mobile"),
                            ("web", "Web"),
                            ("user_excel", "User_Excel"),
                            ("text_message", "Text_Message"),
                        ],
                        default="web",
                        max_length=50,
                    ),
                ),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                ("time", models.DateTimeField()),
                (
                    "supplement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Supplement",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Supplement Log",
                "verbose_name_plural": "Supplement Logs",
                "ordering": ["user", "-time"],
                "unique_together": {("user", "time", "supplement")},
            },
        ),
        migrations.CreateModel(
            name="DailyProductivityLog",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("api", "Api"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                            ("mobile", "Mobile"),
                            ("web", "Web"),
                            ("user_excel", "User_Excel"),
                            ("text_message", "Text_Message"),
                        ],
                        max_length=50,
                    ),
                ),
                ("date", models.DateField()),
                (
                    "very_productive_time_minutes",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "productive_time_minutes",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "neutral_time_minutes",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "distracting_time_minutes",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "very_distracting_time_minutes",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Daily Productivity Log",
                "verbose_name_plural": "Daily Productivity Logs",
                "ordering": ["-date"],
                "unique_together": {("date", "user")},
            },
        ),
        migrations.CreateModel(
            name="ActivityLog",
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
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("notes", models.TextField(default="")),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("api", "Api"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                            ("mobile", "Mobile"),
                            ("web", "Web"),
                            ("user_excel", "User_Excel"),
                            ("text_message", "Text_Message"),
                        ],
                        default="web",
                        max_length=50,
                    ),
                ),
                ("duration_minutes", models.IntegerField(default=0)),
                ("time", models.DateTimeField()),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.Activity"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["user", "-time"],
                "unique_together": {("time", "user", "activity")},
            },
        ),
    ]
