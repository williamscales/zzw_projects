# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141130_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', models.IntegerField(verbose_name='Order', null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('image', models.ImageField(verbose_name='Image', upload_to='projects')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('page_ptr', models.OneToOneField(to='pages.Page', parent_link=True, auto_created=True, primary_key=True, serialize=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='project',
            name='project_list',
            field=models.ForeignKey(related_name='projects', to='zzw_projects.ProjectList'),
            preserve_default=True,
        ),
    ]
