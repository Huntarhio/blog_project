# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=20, default='general', choices=[('general', 'General'), ('sex and relationhip', 'Sex and Relationship'), ('technology', 'Technology'), ('academics', 'Academics'), ('politics', 'Politics')]),
        ),
    ]
