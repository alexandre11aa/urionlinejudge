#### Iu-di-oh! é um jogo de cartas que virou uma verdadeira febre entre os jovens! Todo jogador de Iu-di-oh! tem seu próprio baralh
#### o, contendo várias cartas do jogo. Cada carta contém N atributos (como força, velocidade, inteligência, etc.). Os atributos sã
#### o numerados de 1 a N e são dados por inteiros positivos. Uma partida de Iu-di-oh! é sempre jogada por dois jogadores. Ao inici
#### ar a partida, cada jogador escolhe exatamente uma carta de seu baralho. Após as escolhas, um atributo é sorteado. Vence o joga
#### dor cujo atributo sorteado em sua carta escolhida é maior que na carta escolhida pelo adversário. Caso os atributos sejam igua
#### is, a partida empata. Marcos e Leonardo estão na grande final do campeonato brasileiro de Iu-di-oh!, cujo prêmio é um Dainavis
#### ion (que é quase um Plaisteition 2!). Dados os baralhos de ambos, a carta escolhida por cada um e o atributo sorteado, determi
#### ne o vencedor! A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 100), o núme
#### ro de atributos de cada carta. A segunda linha contém dois inteiros M e L (1 ≤ M, L ≤ 100), o número de cartas no baralho de M
#### arcos e de Leonardo, respectivamente. As próximas M linhas descrevem o baralho de Marcos. As cartas são numeradas de 1 a M, ea
#### i-ésima linha descreve a i-ésima carta. Cada linha contém N inteiros ai,1,ai,2,..., ai,N (1 ≤ ai,j ≤ 109). O inteiro ai,j indi
#### ca o atributo j da carta i. As próximas L linhas descrevem o baralho de Leonardo. As cartas são numeradas de 1 e L e são descr
#### itas de maneira análoga. A próxima linha contém dois inteiros CM e CL (1 ≤ CM ≤ M, 1 ≤ CL ≤ L), as cartas escolhidas por Marco
#### s e Leonardo, respectivamente. Por fim, a última linha contém um inteiro A (1 ≤ A ≤ N) indicando o atributo sorteado. A entrad
#### a termina com fim-de-arquivo (EOF). Para cada caso de teste, imprima uma linha contendo “Marcos” se Marcos é o vencedor, “Leon
#### ardo” se Leonardo é o vencedor, ou “Empate” caso contrário (sem aspas). Q:2542

while True:
	try:
		atributos = int(input())
		n_cartas = list(map(int,input().split()))

		cartas_m, cartas_l = [[],[]]

		for i in range(n_cartas[0]):
			cartas_m.append(list(map(int,input().split())))

		for i in range(n_cartas[1]):
			cartas_l.append(list(map(int,input().split())))

		c_esc = list(map(int,input().split()))
		a_esc = int(input())

		if cartas_m[c_esc[0] - 1][a_esc - 1] > cartas_l[c_esc[1] - 1][a_esc - 1]:
			print("Marcos")
		elif cartas_m[c_esc[0] - 1][a_esc - 1] < cartas_l[c_esc[1] - 1][a_esc - 1]:
			print("Leonardo")
		else:
			print("Empate")

	except:
		break
