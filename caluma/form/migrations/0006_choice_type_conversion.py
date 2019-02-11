# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-08 10:30
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    Question = apps.get_model("form", "Question")
    Question.objects.filter(type="checkbox").update(type="multiple_choice")
    Question.objects.filter(type="radio").update(type="choice")


def reverse_func(apps, schema_editor):
    Question = apps.get_model("form", "Question")
    Question.objects.filter(type="multiple_choice").update(type="checkbox")
    Question.objects.filter(type="choice").update(type="radio")


class Migration(migrations.Migration):

    dependencies = [("form", "0005_auto_20190208_1016")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]