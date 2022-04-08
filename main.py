cnpj = input('digite um cnpj: ')
cnpj_list = []
cnpj_list2 = []
novo_cnpj = []
multiplos_digito_1 = [5,4,3,2,9,8,7,6,5,4,3,2]
multiplos_digito_2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]

for i in cnpj:
    i=int(i)
    cnpj_list.append(i)

digitos_multiplicados1 = cnpj_list[0] * (multiplos_digito_1[0])
digitos_multiplicados2 = cnpj_list[1] * (multiplos_digito_1[1])
digitos_multiplicados3 = cnpj_list[2] * (multiplos_digito_1[2])
digitos_multiplicados4 = cnpj_list[3] * (multiplos_digito_1[3])
digitos_multiplicados5 = cnpj_list[4] * (multiplos_digito_1[4])
digitos_multiplicados6 = cnpj_list[5] * (multiplos_digito_1[5])
digitos_multiplicados7 = cnpj_list[6] * (multiplos_digito_1[6])
digitos_multiplicados8 = cnpj_list[7] * (multiplos_digito_1[7])
digitos_multiplicados9 = cnpj_list[8] * (multiplos_digito_1[8])
digitos_multiplicados10 = cnpj_list[9] * (multiplos_digito_1[9])
digitos_multiplicados11 = cnpj_list[10] * (multiplos_digito_1[10])
digitos_multiplicados12 = cnpj_list[11] * (multiplos_digito_1[11])

soma_dos_digitos = digitos_multiplicados1 + digitos_multiplicados2  + digitos_multiplicados3 + digitos_multiplicados4 + digitos_multiplicados5 + digitos_multiplicados6 + digitos_multiplicados7 + digitos_multiplicados8 + digitos_multiplicados9 + digitos_multiplicados10 + digitos_multiplicados11 + digitos_multiplicados12

formula = 11 - (soma_dos_digitos % 11)
if formula > 9:
    formula = 0
else:
    pass

for i in cnpj:
    i = int(i)
    cnpj_list2.append(i)
digitos_multiplicados13 = cnpj_list2[0] * (multiplos_digito_2[0])
digitos_multiplicados14= cnpj_list2[1] * (multiplos_digito_2[1])
digitos_multiplicados15 = cnpj_list2[2] * (multiplos_digito_2[2])
digitos_multiplicados16 = cnpj_list2[3] * (multiplos_digito_2[3])
digitos_multiplicados17 = cnpj_list2[4] * (multiplos_digito_2[4])
digitos_multiplicados18 = cnpj_list2[5] * (multiplos_digito_2[5])
digitos_multiplicados19 = cnpj_list2[6] * (multiplos_digito_2[6])
digitos_multiplicados20 = cnpj_list2[7] * (multiplos_digito_2[7])
digitos_multiplicados21 = cnpj_list2[8] * (multiplos_digito_2[8])
digitos_multiplicados22 = cnpj_list2[9] * (multiplos_digito_2[9])
digitos_multiplicados23 = cnpj_list2[10] * (multiplos_digito_2[10])
digitos_multiplicados24 = cnpj_list2[11] * (multiplos_digito_2[11])
digitos_multiplicados25 = cnpj_list2[12] * (multiplos_digito_2[12])

soma_dos_digitos2 = digitos_multiplicados13 + digitos_multiplicados14  + digitos_multiplicados15 + digitos_multiplicados16 + digitos_multiplicados17 + digitos_multiplicados18 + digitos_multiplicados19 + digitos_multiplicados20 + digitos_multiplicados21 + digitos_multiplicados22 + digitos_multiplicados23 + digitos_multiplicados24 + digitos_multiplicados25 

formula2 = 11 - (soma_dos_digitos2 % 11)
if formula2 > 9:
        formula2 = 0
novo_cnpj.append(cnpj_list[:-2])

novo_cnpj2 = []
for i in novo_cnpj:
    novo_cnpj2.append(i[0])
    novo_cnpj2.append(i[1])
    novo_cnpj2.append(i[2])
    novo_cnpj2.append(i[3])
    novo_cnpj2.append(i[4])
    novo_cnpj2.append(i[5])
    novo_cnpj2.append(i[6])
    novo_cnpj2.append(i[7])
    novo_cnpj2.append(i[8])
    novo_cnpj2.append(i[9])
    novo_cnpj2.append(i[10])
    novo_cnpj2.append(i[11])

novo_cnpj2.append(formula)
novo_cnpj2.append(formula2)

new_cnpj = []
for i in novo_cnpj2:
    new_cnpj.append(i)

a = ''.join([str(c) for c in new_cnpj])

if cnpj == a:
    print('CNPJ Válido.')
else:
    print('CNPJ Inválido.')
