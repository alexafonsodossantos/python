#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de 
# download do arquivo usando este link (em minutos).

velocidade = int(input("Digite a velocidade da conexão: (em Mb) "))
tamanho = int(input("Digite o tamanho do arquivo (em MB:) "))

v_MB = velocidade / 8

tempo_s = tamanho / v_MB

tempo_m = tempo_s / 60

print("Tempo estimado: ", tempo_m)