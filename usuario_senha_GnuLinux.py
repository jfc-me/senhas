
from crypt import crypt as match


global password
global user



usuarios = dict(dbz="goku:$6$ywNxmw9k$EKgfZGohqTqrT/52v6F0RUdpi/EpsDSjTtaHNqFFLiwCvza5Jbhx97XpLVYzeUxd8heF1caqhe4e/vPX8SvfB.:17949:0:99999:7:::",
                dbzs="vegeta:$6$sVtchzCe$dnjL1N/YlXldU.fjyTXwuuoED7zwLCAsow4LSOqAOOYHFb.c1srsSD/E2UITxTe/HMICVY8FrckeoRz6vyrYW.:17949:0:99999:7:::",
                nt="naruto:$6$g8OCykgP$fSpQf5CEbXgJYVsr4wUltQCzWAKGcSD57nkh45kWVhzbcXD8n3pTIkv2LS5YnvbWTkDOuEHpcBlDMHVsHo/0R1:17949:0:99999:7:::")

lista_de_possiveis_senhas = ["treinar", "malditokakaroto", "sasuke", "test", "test123"]

for lista_all, valor in usuarios.items():
    for usuario_e in range(0, 20):
        if ":$" in valor[0:usuario_e]:
            user = valor[0:usuario_e - 2]
            password = valor[len(valor[0:usuario_e - 1]):len(valor)]
            break


    for senha in lista_de_possiveis_senhas:
        contido = match(senha,  password[0:12])
        if contido in password:
            print(user, senha)
