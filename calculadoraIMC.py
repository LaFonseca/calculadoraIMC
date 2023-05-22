altura_cm = float(input("Digite sua altura em centímetros: "))
peso = float(input("Digite seu peso em quilogramas: "))

# Convertendo altura de cm para m
altura_m = altura_cm / 100  

## Fórmula do IMC
imc = peso / (altura_m ** 2)

if imc < 18.5:
    classificacao = "Magreza"
    grau_obesidade = 0
elif imc < 25:
    classificacao = "Normal"
    grau_obesidade = 0
elif imc < 30:
    classificacao = "Sobrepeso"
    grau_obesidade = "I"
elif imc < 40:
    classificacao = "Obesidade"
    grau_obesidade = "II"
else:
    classificacao = "Obesidade Grave"
    grau_obesidade = "III"

### Retorna o IMC calculado com base nas respostas do usuário
print("Seu IMC é:", imc)
print("Classificação:", classificacao)
print("Obesidade grau:", grau_obesidade)

#### Retorna a tabela para consulta do IMC
print("\nTabela de classificação do IMC:")
print("IMC\tCLASSIFICAÇÃO\tOBESIDADE (GRAU)")
print("Menor que 18.5\tMagreza\t\t0")
print("18.5 - 24.9\tNormal\t\t0")
print("25.0 - 29.9\tSobrepeso\tI")
print("30.0 - 39.9\tObesidade\tII")
print("Maior que 40.0\tObesidade Grave\tIII")

### IMC	CLASSIFICAÇÃO	OBESIDADE (GRAU)
### MENOR QUE 18,5	MAGREZA	0
### ENTRE 18,5 E 24,9	NORMAL	0
### ENTRE 25,0 E 29,9	SOBREPESO	I
### ENTRE 30,0 E 39,9	OBESIDADE	II
### MAIOR QUE 40,0	OBESIDADE GRAVE	III