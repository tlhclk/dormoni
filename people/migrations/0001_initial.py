# Generated by Django 3.2.5 on 2021-11-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Kodu')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tam Adı')),
                ('id_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Kimlik Numarası')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='İlk Adı')),
                ('second_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='İkinci Adı')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ek Adı')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Soyadı')),
                ('nick_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Takma Adı')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ünvanı')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi')),
                ('hometown', models.CharField(blank=True, max_length=50, null=True, verbose_name='Memleketi')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adresi')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Ölüm Tarihi')),
                ('favorite', models.BooleanField(blank=True, default=0, null=True, verbose_name='Favori')),
                ('city_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.citymodel', verbose_name='İli')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.countrymodel', verbose_name='Ülkesi')),
                ('gender_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.gendermodel', verbose_name='Cinsiyeti')),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.peoplegroupmodel', verbose_name='Grubu')),
            ],
            options={
                'verbose_name': 'Rehber',
                'db_table': 'people_person',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='RelationshipModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kişi')),
                ('relation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.relationtypemodel', verbose_name='İlişki')),
            ],
            options={
                'verbose_name': 'Rehber İlişkisi',
                'db_table': 'people_relationtree',
                'ordering': ['person_id', 'relation_id'],
            },
        ),
        migrations.CreateModel(
            name='SocialMediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='Kullanıcı Adı')),
                ('hyperlink', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bağlantı Adresi')),
                ('media_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.mediatypemodel', verbose_name='Sosyal Medya Tipi')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kimin')),
            ],
            options={
                'verbose_name': 'Sosyal Medya Hesabı',
                'db_table': 'people_socialmedia',
                'ordering': ['person_id'],
            },
        ),
        migrations.CreateModel(
            name='RelationshipPersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kişi')),
                ('relation_tree_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.relationshipmodel', verbose_name='İlişki Ağacı')),
            ],
            options={
                'verbose_name': 'İlişki Ağacı - Kişi',
                'db_table': 'people_relationtreeperson',
                'ordering': ['person_id', 'relation_tree_id'],
            },
        ),
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('hyperlink', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bağlantı Adresi')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kimin')),
            ],
            options={
                'verbose_name': 'Kişi Fotoğrafı',
                'db_table': 'people_photo',
                'ordering': ['person_id'],
            },
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon Numarası')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kimin')),
                ('phone_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.phonetypemodel', verbose_name='Telefon Tipi')),
            ],
            options={
                'verbose_name': 'Telefonu Numarası',
                'db_table': 'people_phone',
                'ordering': ['person_id'],
            },
        ),
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='E-Mail Adresi')),
                ('email_type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.emailtypemodel', verbose_name='E-Mail Tipi')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kimin')),
            ],
            options={
                'verbose_name': 'Kişi E-Posta Adresi',
                'db_table': 'people_email',
                'ordering': ['person_id'],
            },
        ),
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Mezuniyet Yılı')),
                ('department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.departmentmodel', verbose_name='Bölümü')),
                ('person_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.personmodel', verbose_name='Kim')),
                ('school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.schoolmodel', verbose_name='Okul')),
                ('schooltype_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.schooltypemodel', verbose_name='Okul Tipi')),
            ],
            options={
                'verbose_name': 'Kişi Eğitimi',
                'db_table': 'people_education',
                'ordering': ['person_id'],
            },
        ),
    ]
