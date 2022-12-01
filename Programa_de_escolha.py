# Programa de escolha 
# Opções do Usuário 
print("[1] - Unidade de Entrada""\n[2] - Unidade de Saída""\n[3] - Mémoria Principal""\n[4] - Memória Secundaria""\n[5] - Unidade de Controle")
# O usuário vai inserir o número de sua escolha entre as opções
resposta = int(input("Digite o número de sua escolha: "))
# O número escolhido pelo usuário vai retornar a informação 
if resposta == 1:
    print("A Unidade de Entrada são responsáveis para levar a informação de fora para dentro do computador ")
if resposta == 2 : 
    print("A Unidade de Saída são responsáveis por levar a informação de dento para fora do computador  ")
if resposta == 3 :
    print("Memória Principal armazena os programas em processamento pela CPU, num dado momento")
if resposta == 4 : 
    print("Memória Secundária armazena todos os programas e toda diversidade de informação residente no computador, mesmo que ele desligue ")
if resposta == 5 : 
    print("Unidade de Controle lê, interpreta cada instrução aciona o dispositivo que irá executar-lá ")
#  Se o número for maior que 5 vai retorar um aviso ao usuário
else:
    if resposta > 5 :
        print("Não há uma escolha com esse número")