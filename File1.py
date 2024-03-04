import random
import string

def generate_random_code(length):
    # Caracteres possíveis para o código
    chars = string.ascii_letters + string.digits
    
    # Gerar o código aleatório
    code = ''.join(random.choice(chars) for _ in range(length))
    return code

# Exemplo de uso: gerar um código com 8 caracteres
random_code = generate_random_code(8)
print("Código aleatório:", random_code)
