n1, n2, n3, n4 = map(float, input().split())
media_do_momento = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: {:.1f}".format(media_do_momento))
if media_do_momento > 6.9:
    print("Aluno aprovado.")

if media_do_momento < 5.0:
    print("Aluno reprovado.")

if media_do_momento >= 5.0 and media_do_momento <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame:", nota_exame)
    media_com_exame = (nota_exame + media_do_momento) / 2
    if media_com_exame >= 5.0:
        print("Aluno aprovado.")
        print("Media final:", media_com_exame)
    else:
        print("Aluno reprovado.")
        print("Media final:", media_com_exame)