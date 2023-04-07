import random
import string

# passar o tamanho da senha a ser gerada
# Função de gerar senha, por padrão se o usuário não passar tamanho será 8.
def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    # Criar uma variavel de string vazia
    password_user = ""

    # Percorrer por posição do tamanho da senha
    for i in range(0, len_pass):
        # Escolhendo uma opção da string options e salvando na variável "digit" - de forma randomica
        digit = random.choice(options)         
        # Agregar com o dgito escolhido - Concatenando
        password_user = password_user + digit

    return password_user

choice_user = input("Quantos digitos na senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida, por favor digite um número!")
    quit()
    

response = password_generator(len_pass = choice_user)
print(f"Senha gerada:\n{response}")