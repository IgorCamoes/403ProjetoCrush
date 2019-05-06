from django.db import models

# Create your models here.
class Crush(models.Model):
    signo_opcoes =  [
        ('ar', 'Áries'),
        ('tr', 'Touro'),
        ('gm', 'Gêmeos'),
        ('cr', 'Câncer'),
        ('le', 'Leão'),
        ('vr', 'Virgem'),
        ('lb', 'Libra'),
        ('es', 'Escorpião'),
        ('sp', 'Serpentário'),
        ('sg', 'Sargitário'),
        ('cp', 'Capricórnio'),
        ('aq', 'Aquário'),
        ('px', 'Peixes')
    ]
    
    nome = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 50)
    data = models.DateField()
    signo = models.CharField(max_length=2, choices = signo_opcoes)
    qualidade = models.CharField(max_length = 100)
    defeito = models.CharField(max_length = 100, default='Não está comigo')
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to = '', null = True)

    def __str__(self):
        return self.nome


