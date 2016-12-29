# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0007_auto_20161218_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='area',
            field=models.SmallIntegerField(choices=[(1, b'Abule Ijesha'), (2, b'Abule egba'), (3, b'Alagbado'), (4, b'Akowonjo'), (5, b'Baruwa'), (6, b'Dopemu'), (7, b'Egbe'), (8, b'Egbeda'), (9, b'Ejigbo'), (10, b'Ijegun'), (11, b'Ikotun'), (12, b'Egan'), (13, b'Iyana Ipaja'), (14, b'Ipaja'), (15, b'Jakande'), (16, b'Ojo'), (17, b'Ojota'), (18, b'Idimu'), (19, b'Adeniyi jones'), (20, b'Agbara'), (21, b'Agege'), (22, b'Agidingbi'), (23, b'Agric'), (24, b'Aguda'), (25, b'Airport road'), (26, b'Ajah'), (27, b'Ajao estate'), (28, b'Ajeromi-Ajegunle'), (29, b'Ajeromi-Ifelodun'), (30, b'Akessan Estate'), (31, b'Akoka'), (32, b'Akute-Ajuwon'), (33, b'Alausa'), (34, b'Alimosho'), (35, b'Allen'), (36, b'Amuwo-odofin'), (37, b'Anthony'), (38, b'Apapa'), (39, b'Apapa-Ajegunle'), (40, b'Awolowo'), (41, b'Awolowo way'), (42, b'Badagry'), (43, b'Banana-Island'), (44, b'Bariga'), (45, b'Bode Thomas'), (46, b'Bourdillon'), (47, b'Chisco'), (48, b'Constain-Ijora Olopa')], default=33),
        ),
    ]
