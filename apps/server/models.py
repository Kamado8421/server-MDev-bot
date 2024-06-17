from django.db import models

class Rank(models.Model):
    name = models.CharField(max_length=35, null=False, blank=False, unique=True)
    bonus = models.IntegerField(blank=False, null=False)
    minLevel = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return f"Rank {self.name}"


class Usuario(models.Model):
    jid = models.CharField(max_length=35, unique=True, null=False, blank=False)
    nome = models.CharField(max_length=35)
    saldo = models.FloatField(default=0)
    debito = models.FloatField(default=0)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    banido = models.BooleanField(default=False, null=False, blank=False)
    isPremium = models.BooleanField(default=False, null=False, blank=False)
    
    def editarSaldo(self, quantidade, adicionarSaldo=True):
        if adicionarSaldo:
            self.saldo += quantidade
        else:
            self.saldo -= quantidade

        self.save()

    
    def editarIsPremium(self, promoverPremium=True):
        if promoverPremium and not self.banido:
            self.isPremium = promoverPremium
        else:
            self.isPremium = False
        
        self.save()
        

    def editarDebito(self, quantidade, pagarDebito=False):
        if pagarDebito:
            self.debito += quantidade
        else:
            debito = self.debito - quantidade

            if debito <= 0:
                self.debito = 0
            else:
                self.debito - quantidade

        self.save()


    def adicionarXp(self, quantidade):
        self.xp += quantidade

        self.save()


    def __str__(self):
        return f'{self.nome} - {self.jid}'


class APIKey(models.Model):
    password = models.CharField(max_length=4, null=False, blank=False, default='1234')
    key = models.CharField(max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"API - {self.name}"
    

