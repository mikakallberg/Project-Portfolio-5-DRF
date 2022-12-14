# Generated by Django 3.2.15 on 2022-10-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20221019_1555'),
        ('imessages', '0002_auto_20221019_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_contact', to='contacts.contacts'),
        ),
        migrations.AlterField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_owner', to='contacts.contacts'),
        ),
    ]
