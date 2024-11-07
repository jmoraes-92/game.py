
# Mario Flappy Bird

Este é um jogo desenvolvido em Python com a biblioteca `pygame`, inspirado no famoso `Flappy Bird`, mas com o personagem Mario e uma progressão de níveis que aumenta a dificuldade.

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Jogar](#como-jogar)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Créditos](#créditos)

## Pré-requisitos

Para rodar este jogo, você precisa de:

- Python 3.x instalado
- Biblioteca `pygame`

Para instalar a `pygame`, execute:

```bash
pip install pygame
```

## Instalação

1. Clone este repositório ou baixe o código.
2. Certifique-se de que as imagens necessárias estão presentes na pasta `img`, incluindo:
   - `background.png`, `background1.png`, `background2.png`, `background3.png`
   - `mario-yoshi.png`
   - `mario-yes.png`
   - `tubo.png`

## Como Jogar

1. Execute o jogo com o comando:

    ```bash
    python mario_flappy_bird.py
    ```

2. Use a barra de espaço para fazer o Mario "voar" e evitar os canos. O objetivo é passar o maior número possível de canos e aumentar sua pontuação.

3. A cada 10 pontos, a dificuldade aumenta, tornando o jogo mais desafiador com o aumento da velocidade e mudanças no fundo.

4. Caso Mario colida com um cano ou saia dos limites da tela, o jogo termina. Pressione a barra de espaço para reiniciar.

5. O jogo termina com vitória quando o jogador atinge o nível final. Ao vencer, uma mensagem de parabéns será exibida junto com uma imagem especial.

## Funcionalidades

- **Progressão de Dificuldade**: A cada 10 pontos, o nível do jogo aumenta, acelerando a velocidade dos canos e trocando o fundo.
- **Pontuação e Nível**: O jogo exibe a pontuação atual e o nível no topo da tela.
- **Estados do Jogo**: Há modos de jogo ativo, game over, e tela de vitória.
- **Imagens Dinâmicas**: Mudanças de imagem ocorrem com o aumento de nível e na tela de vitória.

## Estrutura do Projeto

```plaintext
mario_flappy_bird/
├── img/
│   ├── background.png
│   ├── background1.png
│   ├── background2.png
│   ├── background3.png
│   ├── mario-yoshi.png
│   ├── mario-yes.png
│   └── tubo.png
├── mario_flappy_bird.py
└── README.md
```

- **img/**: Diretório contendo todas as imagens usadas no jogo.
- **mario_flappy_bird.py**: Script principal que executa o jogo.

## Créditos

Jogo desenvolvido com `pygame`, inspirado no conceito de `Flappy Bird`, adaptado com personagens e tema do universo Mario.
