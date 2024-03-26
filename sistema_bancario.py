def obter_valor(mensagem):
  while True:
    valor = float(input(mensagem))
    if valor > 0:
      return valor
    print("Valor inválido. Tente novamente!")

def realizar_operacao(opcao, saldo, limite, extrato):
 
  if opcao == "d":
    valor = obter_valor("Informe o valor do depósito: ")
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
  elif opcao == "s":
    valor = obter_valor("Informe o valor do saque: ")
    if valor > saldo:
      print("Saldo insuficiente.")
    elif valor > limite:
      print("Valor do saque excedeu o limite de R${limite:.2f}")
    else:
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 100
limite = 500
extrato = ""

while True:
  opcao = input(menu)
  if opcao not in ("d", "s", "e", "q"):
    print("Operação inválida.")
    continue

  if opcao in ("d", "s"):
    realizar_operacao(opcao, saldo, limite, extrato)

  if opcao == "e":
    print("\n=============EXTRATO==============")
    print(extrato or "Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================")

  if opcao == "q":
    break



