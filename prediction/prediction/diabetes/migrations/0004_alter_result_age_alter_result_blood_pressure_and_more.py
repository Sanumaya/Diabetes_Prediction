# Generated by Django 4.0.6 on 2023-05-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0003_ans_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='age',
            field=models.CharField(max_length=3, verbose_name='Age (1 - 100)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='blood_pressure',
            field=models.CharField(max_length=3, verbose_name='Blood Pressure (1 - 122)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='bmi',
            field=models.FloatField(max_length=4, verbose_name='BMI 0 - 67.1)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='diabetes_pedigree_function',
            field=models.FloatField(max_length=5, verbose_name='Diabetes Pedigree Function (0.08 - 2.42)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='glucose',
            field=models.CharField(max_length=3, verbose_name='Glucose (1 - 199)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='insulin',
            field=models.CharField(max_length=3, verbose_name='Insulin (0 - 846)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='pregnancies',
            field=models.CharField(max_length=2, verbose_name='Pregnancies (1 - 17)'),
        ),
        migrations.AlterField(
            model_name='result',
            name='skin_thickness',
            field=models.CharField(max_length=2, verbose_name='Skin Thickness (1 - 99)'),
        ),
    ]
