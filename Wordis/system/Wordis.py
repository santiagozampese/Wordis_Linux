#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
from unicodedata import normalize
import os
import time
from pathlib import Path

def menu():
    while True:
        os.system('clear')
        print('[ 1 ] - Jogar/Play\n[ 2 ] - Mudar idioma/Change language\n')
        escolha = int(input('Resposta/Answer: '))
        if escolha == 1:
            game()
        elif escolha == 2:
            os.system('clear')
            os.chdir(os.path.dirname(__file__))
            with open('lingua.json', 'w', encoding='utf-8') as f:
                json.dump(escolha_idioma(), f, ensure_ascii=False, indent=4)
               
def encontrar_arquivo(arquivo, diretorio='.'):
    caminho = os.path.join(diretorio, arquivo)

    if os.path.isfile(caminho):
        return caminho
    
    for raiz, dir, arquivos in os.walk(diretorio):
        if arquivo in arquivos:
            return os.path.join(raiz, arquivo)
        
    return None

def verificar_escolha():
        try:
            entrada = input('Digite o número da escolha!/Type the number of your choice!: ')
            numero_inteiro = int(entrada)
            return numero_inteiro
        except ValueError:
            print('Digite apenas números!/Type only numbers!')
            time.sleep(1.5)
            escolha_idioma()

def escolha_idioma():
    os.system('clear')
    print('Escolha o idioma:    Choose language:')
    print('[ 1 ] - Português\n[ 2 ] - English\n')
    opcao = verificar_escolha()
    if opcao == 1:
        return "portugues"
    elif opcao == 2:
        return "english"
    else:
        print('Escolha inválida    Invalid choice')
        time.sleep(1.5)
        escolha_idioma()

if not os.path.isfile('lingua.json'):
    os.chdir(os.path.dirname(__file__))
    with open('lingua.json', 'w', encoding='utf-8') as f:
        json.dump(escolha_idioma(), f, ensure_ascii=False, indent=4)

lingua = open(encontrar_arquivo('lingua.json'), encoding='utf-8')
language = json.load(lingua)
if language == None:
   with open('lingua.json', 'w', encoding='utf-8') as f:
        json.dump("portugues", f, ensure_ascii=False, indent=4)

words_f = open(encontrar_arquivo('words.json'), encoding="utf8")
words = json.load(words_f)


def game():
    os.system('clear')
    lingua = open(encontrar_arquivo('lingua.json'), encoding='utf-8')
    language = json.load(lingua)
    words_f = open(encontrar_arquivo('words.json'), encoding="utf8")
    words = json.load(words_f)
    words_language = words[language]
    choice_c = random.choice(list(words_language.keys()))
    choice_v = random.choice(words_language[choice_c])

    print('Seja Bem-vindo ao Wordis, Seu objetivo é acertar a palavra da vez!\nPara fazer isso digite uma palavra e as letras que corresponderem com a palavra da vez ficarão destacadas\nCom as letras corretas você poderá acertar a palavra da vez mais facilmente!\nWelcome to Wordis! Your goal is to guess the word of the day!\nTo do this, type a word and the letters that match the word will be highlighted.\nWith the correct letters, you can guess the word of the day more easily!')
    print('Lembre-se que acentos e letras maíusculas não mudam o resultado!\nA letra "Ç" Equivale a "C"!\nRemember that accents and capital letters dont change the result!\nThe letter "Ç" is equivalent to "C"!')
    print('Você terá 5 tentativas! Boa Sorte!\nYou will have 5 attempts! Good luck!\n')

    tamanho_palavra = len(choice_v)

    n_guesses = 5
    vez = 1
    win = False

    check_rodadas_palavra = []
    check_rodadas_palpite = []

    while n_guesses > 0 and win is not True:
        os.system('clear')
        print('     Tentativas/Attemps      Digite "Q" para voltar ao menu!/Type "Q" to go back for the menu!\n')
        for p in range(len(check_rodadas_palpite)):
            print(check_rodadas_palavra[p])
            print(check_rodadas_palpite[p])

        print(f'Categoria/Category: {choice_c}')
        print(f'Palavra/Word: {'❔'*tamanho_palavra}')
        
        print(f'Dígitos/Digits: {tamanho_palavra}\n')
        palpite = str(input(f'Palpite {vez}: '))
        if palpite.lower() == 'q':
            menu()

        elif len(palpite) != tamanho_palavra:
            print('Tamanho das palavras devem corresponder!\nThe size of the words should match!\n')
            time.sleep(1.5)
            continue

        elif palpite.isalpha():
            vez += 1
            check = []
            pontuation = 0

            for i in range(tamanho_palavra):
                digito = str(choice_v[i]).lower()
                digito_limpo = normalize('NFKD', digito).encode('ASCII', 'ignore').decode('ASCII')
                palpite_limpo = normalize('NFKD', (palpite[i].lower())).encode('ASCII', 'ignore').decode('ASCII')
                if palpite_limpo == digito_limpo:
                    check.append('✅')
                    pontuation += 1
                else:
                    check.append('💢')

          

            check_rodadas_palavra.append("|".join(check))
            check_rodadas_palpite.append("| ".join(palpite))

            if pontuation == tamanho_palavra:
                win = True

        else:
            print('O Palpite deve ser uma palavra!\nThe guess should be a word')
            time.sleep(1.5)
            continue

        n_guesses -= 1

    if win == True:
        os.system('clear')
        print('     Tentativas      ')
        for p in range(len(check_rodadas_palpite)):
            print(check_rodadas_palavra[p])
            print(check_rodadas_palpite[p])
        print('VITÓRIA!/VICTORY!')

    else:
        print(f'DERROTA!\nA Palavra era {choice_v}\nDefeat!The word was {choice_v}')

    input('Pressione qualquer tecla para Fechar!/Press any key to close!')

menu()