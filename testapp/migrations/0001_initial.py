# Generated by Django 2.0.1 on 2018-01-27 05:57

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0002_auto_20180127_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolen_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=255)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField(blank=True, null=True)),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('file_path_field', models.FilePathField(path=None)),
                ('float_field', models.FloatField()),
                ('image_field', models.ImageField(upload_to=None)),
                ('integer_field', models.IntegerField()),
                ('generic_IP_adress_field', models.GenericIPAddressField()),
                ('null_boolean_field', models.NullBooleanField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integet_field', models.PositiveSmallIntegerField()),
                ('slug_field', models.SlugField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
                ('url_field', models.URLField()),
                ('uuid_field', models.UUIDField()),
                ('foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News')),
                ('many_to_many_field', models.ManyToManyField(related_name='_testfields_many_to_many_field_+', to='testapp.TestFields')),
            ],
        ),
    ]
