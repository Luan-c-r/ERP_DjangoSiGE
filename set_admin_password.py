from django.contrib.auth import get_user_model
import os
import django

# Configurar o ambiente Django
# O DJANGO_SETTINGS_MODULE já deve estar configurado pelo manage.py ou ambiente
# No entanto, para scripts standalone, é bom garantir.
# O projeto parece usar djangosige.configs como settings module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosige.configs")
django.setup()

User = get_user_model()
try:
    user = User.objects.get(username="admin")
    user.set_password("Useradmin")
    user.save()
    print("Senha do usuário 'admin' alterada com sucesso para 'Useradmin'.")
except User.DoesNotExist:
    print("Usuário 'admin' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao tentar alterar a senha: {e}")

