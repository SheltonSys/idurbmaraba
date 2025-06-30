# core/models.py
from django.db import models

class Sistema(models.Model):
    nome = models.CharField(max_length=100)
    link = models.URLField()
    
    def __str__(self):
        return self.nome


# noticias/models.py
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# servicos/models.py
from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


# webapp/models.py
from django.db import models

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.email}"



# models.py
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateField(auto_now_add=True, editable=False)
    publicado = models.BooleanField(default=False)  # <-- adicione isso

    def __str__(self):
        return self.titulo
