# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('blog', '0007_auto_20160310_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(verbose_name='External link')),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SocialLinkItem',
            fields=[
                ('sociallink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.SocialLink')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='blog.SocialMediaLinks')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('blog.sociallink', models.Model),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='default_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='hover_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
    ]
