x = temperatura
y = tensao_termopilha

titulo_grafico = 'Tensão Termopilha (V) x Temperatura (K)'
titulo_x = 'log (Temperatura (K))'
titulo_y = 'log (Tensão Termopilha (V))'

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
plt.title(titulo_grafico)
plt.xlabel(titulo_x)
plt.ylabel(titulo_y)
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()