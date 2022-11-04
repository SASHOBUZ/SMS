# Generated by Django 4.1 on 2022-09-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='amount',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fees',
            name='fee_type',
            field=models.CharField(choices=[('Admission', 'Admission'), ('Monthly Fees', 'Monthly Fees'), ('Exam Fees', 'Exam Fees'), ('Other Fees', 'Other Fees')], max_length=200, null=True),
        ),
    ]