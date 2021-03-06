# Generated by Django 3.1.4 on 2022-02-25 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20220225_1741'),
        ('people', '0003_auto_20220225_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmodel',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_info', to='authentication.branchmodel', verbose_name='Şube'),
        ),
        migrations.AlterField(
            model_name='emailmodel',
            name='company_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_info', to='authentication.companymodel', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_info', to='authentication.branchmodel', verbose_name='Şube'),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='company_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_info', to='authentication.companymodel', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone_info', to='authentication.branchmodel', verbose_name='Şube'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='company_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phone_info', to='authentication.companymodel', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_info', to='authentication.branchmodel', verbose_name='Şube'),
        ),
        migrations.AlterField(
            model_name='photomodel',
            name='company_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo_info', to='authentication.companymodel', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='socialmediamodel',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social_info', to='authentication.branchmodel', verbose_name='Şube'),
        ),
        migrations.AlterField(
            model_name='socialmediamodel',
            name='company_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='social_info', to='authentication.companymodel', verbose_name='Firma'),
        ),
    ]
