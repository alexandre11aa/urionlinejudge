#### Ao voltar de um intenso jogo de RPG na casa de um amigo, o jovem Will desapareceu misteriosamente! Todos estão desesperadament
#### e procurando por ele por todos os cantos. Enquanto isso, coisas estranhas estão acontecendo em sua casa. Uma delas, entretanto
#### , lhe permite comunicar-se com o garoto! Há exatamente 26 lâmpadas penduradas na parede da sua sala, numeradas de 1 a 26 da es
#### querda para a direita. Além disso, há uma letra do alfabeto pintada na parede em baixo de cada lâmpada. Quando Will quer lhe e
#### nviar uma mensagem, ele irá (misteriosamente) piscar, uma a uma, as lâmpadas correspondentes a cada letra de sua mensagem. Por
#### exemplo, se ele quer enviar a mensagem HELP, ele irá piscar, nesta ordem, as lâmpadas acima das letras H, E, L e P. Dada a let
#### ra associada a cada lâmpada e a ordem das lâmpadas que foram piscadas por Will, decifre a mensagem que ele enviou! A entrada c
#### ontém vários casos de teste. A primeira linha de cada caso contém uma string de exatamente 26 letras maiúsculas contendo todas
#### as letras do alfabeto inglês. A primeira letra da string está associada à lâmpada 1; a segunda letra está associada à lâmpada2
#### ; e assim por diante. A próxima linha contém um inteiro N (1 ≤ N ≤ 104), o número de lâmpadas que foram piscadas. A terceira l
#### inha contém N inteiros li (1 ≤ li ≤ 26), indicando as lâmpadas que foram piscadas, em ordem. Para cada caso de teste, imprimau
#### ma única linha contendo a mensagem enviada por Will. Q:2523

while True:
	try:
		p = input()
		l = int(input())
		c = list(map(int,input().split()))

		f = ""

		for i in range(l):
			f += p[c[i] - 1]

		print(f)

	except:
		break
