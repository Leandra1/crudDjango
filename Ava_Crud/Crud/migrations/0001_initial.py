# Generated by Django 4.1 on 2022-08-31 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('fone', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('requisito', models.CharField(max_length=255)),
                ('carga_horaria', models.SmallIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('valor_hora', models.IntegerField()),
                ('certificados', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('carga_horaria', models.SmallIntegerField()),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crud.curso')),
                ('instrutor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crud.instrutor')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_matricula', models.DateField()),
                ('aluno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crud.aluno')),
                ('turma_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crud.turma')),
            ],
        ),
    ]
