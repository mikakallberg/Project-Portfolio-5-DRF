# Generated by Django 3.2.15 on 2022-10-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imessages', '0005_alter_message_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
