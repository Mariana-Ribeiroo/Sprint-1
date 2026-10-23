
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Esporte, PerfilUsuario, PerfilEsporte


class Command(BaseCommand):
    help = "Cadastrar jogadores de exemplo"

    def handle(self, *args, **kwargs):

        # Jogadores ficticios para testar o site
        pessoas = [
            ("Ana", "Silva", "Futebol", "Intermediário"),
            ("Pedro", "Costa", "Tênis", "Iniciante"),
            ("Julia", "Martins", "Vôlei", "Avançado"),
            ("Lucas", "Almeida", "Basquete", "Intermediário"),
            ("Beatriz", "Rocha", "Corrida", "Iniciante"),
            ("Rafael", "Souza", "Futebol", "Avançado"),
            ("Camila", "Lima", "Tênis", "Intermediário"),
            ("Gabriel", "Oliveira", "Vôlei", "Iniciante"),
        ]

        for numero, (nome, sobrenome, esporte_nome, nivel) in enumerate(pessoas, start=1):

            # Criar usuario caso ainda nao exista
            usuario, criado = User.objects.get_or_create(
                username=f"exemplo_matchpoint_{numero}",
                defaults={
                    "first_name": nome,
                    "last_name": sobrenome,
                }
            )

            if criado:
                usuario.set_unusable_password()
                usuario.save()

            # Criar perfil
            PerfilUsuario.objects.get_or_create(usuario=usuario)

            # Criar esporte
            esporte, _ = Esporte.objects.get_or_create(nome=esporte_nome)

            # Associar esporte ao jogador
            PerfilEsporte.objects.get_or_create(
                usuario=usuario,
                esporte=esporte,
                defaults={"nivel": nivel}
            )

        print("Banco de dados populado com sucesso!")
