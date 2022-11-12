#-*-coding:utf8;-*-
import androidhelper
from datetime import date
import os
import sys
import socket 
import datetime
import time
droid = androidhelper.Android()
print("====="*3)
nome = input("digite seu nome: ")
print("====="*3)
droid.ttsSpeak("bem vindo ao programa ")
droid.ttsSpeak(nome)
droid.makeToast('Hello, bem vindo')
print('Hello world!')
os.system('clear')
print('bem_vindo ao robodroid')
print('carregando...')
time.sleep(3)
print('•••'*10)
print('vamos começar')
print('•••'*10)
while True:
    print(''''[hora]-ver hora atual
[date]-data atual
[modulo]-baixar biblioteca py
[whois]-informaçoes do sites
[wi-fi on]-ligar o wifi e of desligar
[tabuada]-entra na tabuada
[portas]-ver portas aberta de ip
[ip]-para ver ip do site
[meu-ip]-mostra seu ip interno
[desligar]-sair do programa  ''')
    print('==='*10)
    resposta=input('o que dejesa: ')
    os.system('clear')
    print('==='*10)
    if resposta == 'hora':
       droid.ttsSpeak("acessando a hora")
       curr_time = time.localtime() 
       curr_clock = time.strftime("%H:%M:%S", curr_time)
       droid.ttsSpeak(curr_clock)
       print(curr_clock)
       print('==='*10)
    if resposta == 'date':
       droid.ttsSpeak("acessando a horas atual")
       data_atual= date.today()
       print(data_atual)
       print('==='*10)
    if resposta == 'modulo':
       ferramenta = input('nome da ferramenta: ')
       pip.main(['install',ferramenta])
    if resposta == 'whois':
        dominio=input('example.com: ')
        whoisData = whois.whois(dominio)
        print(whoisData.text)
    if resposta == 'tabuada':
       droid.ttsSpeak("digite número para ver a tabuada dele")
       tabuada=int(input("Tabuada do numero: ")) 
       for count in range(10):
           print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
    if resposta == 'portas':
        droid.ttsSpeak("digite um o ip para ver as portas")
        alvo = input('Digite o IP: ')
        droid.ttsSpeak("ate que numeros podes procurar")
        number=int(input('ate que porta: '))
        for porta in range(1, number):
            client = socket.socket()
            client.settimeout(0.05) 
            if client.connect_ex((alvo, porta)) == 0:
                print('•••'*10)
                print('scaneando...')
                print('•••'*10)
                print('Porta Aberta ==>', porta)
                print('•••'*10)
                time.sleep(2)
    resultado =input('aperte entre para continuar: ')
    if resposta == 'ip':
        droid.ttsSpeak("digite o nome do site")
        site = input('nome do site .com: ')
        addr1 = socket.gethostbyname(site)
        print('==='*10) 
        print(addr1)
        print('==='*10)
        time.sleep(2) 
    if resposta == 'wi-fi on':
       droid.toggleWifiState(True)
    if resposta =='wi-fi of':
       droid.toggleWifiState(False)
    if resposta == 'desligar':
       droid.dialogCreateAlert(
    "Titulo do alerta",
    "A mensagem é, você quer sair?")
       droid.dialogSetPositiveButtonText("Sim")
       droid.dialogSetNegativeButtonText("Não")
       droid.dialogShow()
       escolha = droid.dialogGetResponse().result
       escolhas=(f"A escolha foi: {escolha['which']}") 
       if escolhas =='A escolha foi: positive':
          droid.ttsSpeak("programa encerrado")
          print(escolhas)
          break
    elif resposta == 'meu-ip':
       droid.ttsSpeak("mostrando seu Ip aguarde")
       ip_local = socket.gethostbyname(socket.gethostname()) 
       print(f'IP Local: {ip_local}')
       time.sleep(2)
