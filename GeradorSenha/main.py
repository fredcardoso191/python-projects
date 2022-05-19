from random import choice
import string
    
def gerador(tamanho):
  senha = ''
  valores = string.ascii_letters + string.digits  #+ string.punctuation
  for i in range(tamanho):
    senha += choice(valores)
  print(senha)


while True:
  try:
    tamanho = int(input("Digite o tamanho da senha: (8 até 1000 caractéres): "))
    if tamanho > 1000 or tamanho < 8:
      raise ValueError("Digite um tamanho válido!")
  except ValueError as e:
    print("Digite um tamanho válido!")
  else:
    gerador(tamanho)
    break