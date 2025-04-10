def calcularmedia(nota1, nota2, optativa):
    if  nota1 < optativa or nota2 < optativa:
        if nota1 < nota2:
                   nota1 = optativa
        else:
             nota2 = optativa
    media = (nota1 + nota2 )/2
    return media


def media1(media):
    if media >6:
      print(f'parabéns vc foi aprovado sua media é: {media}')
    elif media <=6 and media >3 :
      print(f'vocé esta de recuperação  sua media é: {media}')
    else:
      print(f"vc esta reprovado sua media foi: {media}")

nota1 = int(input("digite sua nota: "))
nota2 = int(input("digite sua nota: "))
optativa = int(input("digite sua nota optativa, caso não tenha feito digite 0: "))

media_calculada = calcularmedia(nota1, nota2, optativa)
media1(media_calculada)