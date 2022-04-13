total = 0
nota = -5
lista_notas = list()
count = 0

while nota >= 0 or nota <= 10:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    elif nota >= 0 and nota <= 10:
        total += nota
        count += 1
        if count == 2:
            media = round(total/2,2)
            print("media = {:.2f}".format(media))
            count = 0
            total = 0
            print("novo calculo (1-sim 2-nao)")
            voltar = int(input())
            if voltar == 2:
                break
            while voltar > 2 or voltar < 1:
                print("novo calculo (1-sim 2-nao)")
                voltar = int(input())




aux=n=0
med=0.00
while True:
    nota=float(input())
    if nota>10 or nota<0:print("nota invalida")
    else:
        aux+=1
        med+=nota
        if aux==2:
            print("media = %.2f"%(med/2))
            while True:
                print("novo calculo (1-sim 2-nao)")
                n=int(input())
                if n==1:
                    aux=n=0
                    med=0.00
                    break
                elif n==2:
                    break
    if n==2:break