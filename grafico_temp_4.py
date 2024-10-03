x = temperatura_quarta
y = tensao_termopilha

# Calculando os coeficientes da reta de regressão linear
a, b = np.polyfit(x, y, 1)  # 1 indica uma reta (polinômio de grau 1)

# Imprimindo os valores de a e b
print(f"Valor de a: {a}")
print(f"Valor de b: {b}")

# Avaliando a reta nos pontos x
reta = np.polyval([a, b], x)

# Criando o gráfico
plt.scatter(x, y, color='red', label='Dados originais')  # Pontos originais
#plt.plot(x, reta, label='Reta de regressão linear')

# Adicionando título e rótulos aos eixos
plt.title("Tensão Termopilha (V) x Temperatura^4 (K)")
plt.xlabel("Temperatura^4 (K)")
plt.ylabel("Tensão Termopilha (V)")
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()