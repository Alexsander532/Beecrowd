idade = int(input())
anos = 0
meses = 0
dias = 0
resto_anos = 0
resto_meses = 0
anos = idade//365
resto_anos = idade%365
meses = resto_anos//30
dias = resto_anos%30
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
