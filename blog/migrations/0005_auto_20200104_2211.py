# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=20, default='general', choices=[('general', 'General'), ('relationship', 'Sex and Relationship'), ('technology', 'Technology'), ('academics', 'Academics'), ('politics', 'Politics')]),
        ),
    ]
