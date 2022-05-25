from random import choice
print('''
    BEM VINDO (A) AO JOGO DA FORCA !
    O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. 
    A cada rodada, os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte da palavra. 
    Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. Ao contrário, o jogador será enforcado.
    Você tem 6 chances.
    BOA SORTE !
''')
palavras = ['JABOTICABA', 'PINHA', 'MELANCIA', 'MANGA', 'GOIABA','GRAMADO', 'PARATI', 'SALVADOR', 'BANANEIRAS', 'MEXICO','TECLADO', 'POLTRONA', 'QUADRO', 'TAPETE', 'TALHER']
sorteio_palavras = choice(palavras)
qtd_caracteres = len(sorteio_palavras)
gabarito = [''] * qtd_caracteres
print('A palavra é:{}'.format(gabarito))
cont = 0
for i in range(6):
        usuario = input('Digite uma letra ou palavra:')
        usuario = usuario.upper()
        cont = cont + 1
        print(cont)
        if len(usuario) > 1 and usuario == sorteio_palavras:
            print(('PARABÉNS, você ganhou. A palavra era {} !'.format(sorteio_palavras)))
            print('🪘🥇')
            break
        elif usuario in sorteio_palavras:
            for x in range(len(sorteio_palavras)):
              if (sorteio_palavras[x]) == usuario:
                  gabarito[x] = usuario
            print(gabarito)
        elif usuario not in sorteio_palavras:
            print('ERROU, letra ou palavra não encontrada!')
            if cont == 6:
                print('VOCÊ FOI ENFORCADO! A palavra era {}!'.format(sorteio_palavras))
                print('💀️')

