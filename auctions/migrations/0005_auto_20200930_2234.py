# Generated by Django 3.1.1 on 2020-09-30 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userlistings', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categorylistings', to='auctions.category'),
        ),
    ]