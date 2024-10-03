import numpy as np
import matplotlib.pyplot as plt
import math

dados = [

0.61600,739.59997,0.12452 ,

0.95200,841.59997,0.13599 ,

1.36000,947.20001,0.15230 ,
1.80800,1054.40002,0.18182 ,

2.32800,1171.19995,0.22221 ,

2.81600,1277.19995,0.27280 ,

3.24000,1363.19995,0.31960 ,

3.66400,1448.40002,0.36368 ,

4.16800,1544.40002,0.42784 ,

4.64000,1633.19995,0.48461 ,
5.12800,1638.00000,0.54532 ,

5.57600,1638.00000,0.62216 ,

6.06400,1638.00000,0.69154 ,

6.57600,1638.00000,0.77007 ,

7.04000,1638.00000,0.84603 ,

7.49600,1638.00000,0.92477 ,

7.91200,1638.00000,1.01502 ,

8.44800,1638.00000,1.09937 ,
8.91200,1638.00000,1.19962 ,
9.38400,1638.00000,1.34454 ,

9.86400,1638.00000,1.40589 ,

10.40800,1638.00000,1.51030 ,

10.80000,1638.00000,1.59243 ,
]


# Convertendo para array numpy e formatando em uma matriz com 3 colunas
data = np.array(dados).reshape(-1, 3)

# Exibindo o array numpy
print(data)

# Extração das colunas
tensao_lampada = data[:, 0]
corrente_lampada = data[:, 1]
tensao_termopilha = data[:, 2]

tensao_termopilha_log = np.log10(tensao_termopilha, where=tensao_termopilha > 0, out=np.full_like(tensao_termopilha, np.nan))

# Constantes fornecidas
const1 = 0.00482
const2 = 6.76E-7
const3 = 2.06068
#const3 = 0.3323 #lampada nova
#const3 = 0.77388
 
#const3 = const3 / (1 + const1 * 25 + const2*const2*25)

# Cálculo conforme a fórmula fornecida, com tratamento de divisão por zero
temperatura = np.zeros(tensao_lampada.shape)
temperatura_log = np.zeros(tensao_lampada.shape)
temperatura_quarta = np.zeros(tensao_lampada.shape)
potencia_lampada = np.zeros(tensao_lampada.shape)
for i in range(len(tensao_lampada)):
    if corrente_lampada[i] != 0:
        temperatura[i] = (np.sqrt(const1*const1 + 4*const2*(tensao_lampada[i]/(corrente_lampada[i]/1000)/const3 - 1)) - const1) / (2*const2) 
        temperatura_log[i] = np.log10(temperatura[i])
        temperatura_quarta[i] = temperatura[i]**4
        potencia_lampada[i] = tensao_lampada[i] * corrente_lampada[i]/1000 
    else:
        temperatura[i] = None

print(temperatura)
print(temperatura_log)
print(temperatura_quarta)
print(tensao_termopilha)
print(tensao_termopilha_log)
print(potencia_lampada)