# Generated by Django 3.2.12 on 2023-10-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt_integration', '0003_alter_chat_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemprompt',
            name='prompt',
            field=models.TextField(max_length=2048),
        ),
    ]
