Perfeito! Agora vou criar um README profissional e detalhado para o Wordle Pro:

```markdown
# 🎮 WORDLE PRO — Multi-Modo 2026

> Um jogo de adivinhação de palavras desenvolvido em Python com CustomTkinter. Versão profissional e modular do clássico Wordle com suporte a múltiplas palavras simultâneas, diferentes tamanhos (5-7 letras), teclado interativo e sistema de feedback visual com cores oficiais Wordle.

[![Python](https://img.shields.io/badge/python-3.7+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Game](https://img.shields.io/badge/Game-Word%20Puzzle-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Production-brightgreen.svg)]()
[![Language](https://img.shields.io/badge/Language-Portuguese-green.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [🎮 Como Jogar](#-como-jogar) • [📖 Documentação](#-arquitetura-e-estrutura) • [🎨 Modos](#-modos-de-jogo) • [🧠 Lógica](#️-lógica-do-jogo)**

</div>

---

## 🌟 Visão Geral

**WORDLE PRO** é uma versão profissional e expandida do clássico jogo Wordle, adaptado para português e com **recursos avançados**. Permite jogar com **1 a 4 palavras simultâneas**, escolher **tamanho de palavras (5, 6 ou 7 letras)**, e oferece **feedback visual preciso** com as cores oficiais do Wordle.

### ✨ Destaques Principais

- 🎯 **Múltiplos Modos**: 1, 2, 3 ou 4 palavras simultâneas
- 📏 **3 Tamanhos**: 5, 6 ou 7 letras por palavra
- 🎨 **Cores Oficiais**: Verde (correto), Amarelo (misplaced), Cinza (errado)
- ⌨️ **Teclado Interativo**: Clique ou use teclado físico
- 📊 **Grid Dinâmico**: Layout adapta conforme número de palavras
- 💾 **100+ Palavras**: Lista abrangente em português
- 🎭 **Feedback Visual**: Teclado muda cor conforme seu desempenho
- 📱 **Responsivo**: Funciona bem em diferentes resoluções
- 🏆 **Sistema de Pontos**: Tentativas limitadas por número de palavras
- 🌙 **Dark Mode**: Interface escura confortável

---

## 🎮 Como Jogar

### 📋 Objetivo

```
1. Adivinhe a palavra (ou palavras)
2. 6 tentativas (7 se 6-7 letras)
3. Feedback em cada tentativa:
   🟩 Verde = Letra correta no lugar certo
   🟨 Amarelo = Letra certa no lugar errado
   ⬜ Cinza = Letra não existe na palavra
4. Resolva todas as palavras para vencer
```

---

### ⌨️ Controles

| Ação | Mouse | Teclado |
|------|-------|---------|
| Adicionar letra | Clique no botão | Digit letra (A-Z) |
| Deletar letra | Clique ⌫ | BACKSPACE |
| Submeter palpite | Clique ENTER | ENTER |

---

### 🎯 Exemplo de Gameplay

```
MENU INICIAL:
┌──────────────────────────┐
│  WORDLE MULTI-MODO       │
│                          │
│ Quantidade de Palavras:  │
│ [1] 2  3  4             │
│                          │
│ Tamanho das Letras:      │
│ [5] 6  7                │
│                          │
│ [JOGAR AGORA]            │
└──────────────────────────┘

↓ (Escolhe 2 palavras de 5 letras)

DURANTE O JOGO:
┌─────────────────┬─────────────────┐
│ PALAVRA 1       │ PALAVRA 2       │
├─────────────────┼─────────────────┤
│ 🟩🟨⬜🟩🟩    │ ⬜⬜🟨🟩⬜    │
│ ⬜⬜⬜⬜⬜    │ 🟨⬜🟨⬜⬜    │
│ ...             │ ...             │
└─────────────────┴─────────────────┘

Teclado:
[Q][W][E][R][T]...[P]
[A][S][D][F][G]...[L]
[ENTER][Z][X][C]...[M][⌫]

Digitou "PIZZA" na palavra 1 ✓
Digitou "GATOS" na palavra 2 (feedback recebido)
```

---

## 🎨 Modos de Jogo

### 1️⃣ **Modo Solo (1 Palavra)**

```
Dificuldade: ⭐ Fácil
Layout: 1 grid central
Tentativas: 6 (5 letras) / 7 (6-7 letras)
Tempo: ~5-15 minutos

Ideal para:
✓ Iniciantes
✓ Treino rápido
✓ Desafio casual
```

---

### 2️⃣ **Modo Duplo (2 Palavras)**

```
Dificuldade: ⭐⭐ Médio
Layout: 2 grids lado a lado
Tentativas: 7 (5 letras) / 8 (6-7 letras)
Tempo: ~10-25 minutos

Ideal para:
✓ Desafio moderado
✓ Jogar com amigo (reveza)
✓ Melhorar estratégia
```

---

### 3️⃣ **Modo Triplo (3 Palavras)**

```
Dificuldade: ⭐⭐⭐ Difícil
Layout: 3 grids em grid 2x2
Tentativas: 8 (5 letras) / 9 (6-7 letras)
Tempo: ~15-40 minutos

Ideal para:
✓ Veteranos
✓ Desafio intenso
✓ Provar habilidades
```

---

### 4️⃣ **Modo Extremo (4 Palavras)**

```
Dificuldade: ⭐⭐⭐⭐ Extremo
Layout: 4 grids em grid 2x2
Tentativas: 9 (5 letras) / 10 (6-7 letras)
Tempo: ~20-60 minutos

Ideal para:
✓ Desafio máximo
✓ Recorde pessoal
✓ Competição extrema
```

---

## 📏 Tamanhos de Palavras

### 5️⃣ **5 Letras**

```
Dificuldade: ⭐ Fácil
Exemplos: PIZZA, GATOS, ZEBRA, MUNDO, TESLA
Palavras na lista: ~20
Tempo por tentativa: Rápido
```

---

### 6️⃣ **6 Letras**

```
Dificuldade: ⭐⭐ Médio
Exemplos: QUEIJO, BANANA, GOOGLE, PYTHON, DESIGN
Palavras na lista: ~30
Tempo por tentativa: Normal
Padrão do jogo original
```

---

### 7️⃣ **7 Letras**

```
Dificuldade: ⭐⭐⭐ Difícil
Exemplos: LARANJA, NETFLIX, ARQUIVO, USUARIO, BOOLEAN
Palavras na lista: ~25
Tempo por tentativa: Mais tempo para pensar
Desafio significativo
```

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Propósito |
|-----------|-----------|----------|
| **Linguagem** | Python | 3.7+ |
| **GUI** | CustomTkinter | Interface moderna |
| **Lógica** | Python nativo | Mecânicas do jogo |

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo do Jogo

```
┌─────────────────┐
│   Inicializa    │
│   WordlePro     │
└────────┬────────┘
         │
    ┌────▼──────────────┐
    │ Menu Principal    │
    │ (1-4 palavras)    │
    │ (5-7 letras)      │
    └────┬──────────────┘
         │
    ┌────▼──────────────┐
    │ Seleciona opções  │
    │ Clica JOGAR AGORA │
    └────┬──────────────┘
         │
    ┌────▼──────────────────┐
    │ Inicializa Jogo       │
    │ - Seleciona palavras  │
    │ - Cria grids          │
    │ - Mostra teclado      │
    └────┬──────────────────┘
         │
    ┌────▼────────────────────────────────┐
    │ LOOP DO JOGO                         │
    │ ├─ Espera input (teclado/mouse)    │
    │ ├─ Adiciona letra ao palpite       │
    │ ├─ Atualiza grid visual            │
    │ └─ Aguarda ENTER                   │
    └────┬───────────────────────────────┘
         │
    ┌────▼──────────────────────┐
    │ Processa Palpite         │
    │ ├─ Valida comprimento    │
    │ ├─ Verifica todas palavras│
    │ ├─ Calcula cores         │
    │ ├─ Atualiza teclado      │
    │ └─ Incrementa tentativas │
    └────┬────────────────────┘
         │
         ├─→ [Todas resolvidas?] ─→ VITÓRIA
         │
         ├─→ [Tentativas esgotadas?] ─→ GAME OVER
         │
         └─→ [Continuar?] ─→ LOOP
```

---

### 🧩 Componentes Principais

```
termo.py
│
└── 📦 CLASSE: WordlePro (CustomTkinter)
    │
    ├── INICIALIZAÇÃO
    │   ├── __init__()
    │   ├── full_word_list (100+ palavras)
    │   └── Configurações de cores
    │
    ├── MENU
    │   ├── setup_menu()
    │   │   ├─ Selector: Número de palavras
    │   │   ├─ Selector: Tamanho de letras
    │   │   └─ Botão: JOGAR AGORA
    │   │
    │   └── start_game()
    │       ├─ Filtra palavras por tamanho
    │       ├─ Seleciona randomicamente
    │       └─ Inicia interface do jogo
    │
    ├── INTERFACE (UI)
    │   ├── setup_ui()
    │   │   ├─ Header
    │   │   ├─ Scroll container
    │   │   ├─ Grids (dinâmicos)
    │   │   └─ Teclado
    │   │
    │   └── setup_keyboard()
    │       ├─ 3 linhas de botões (QWERTY)
    │       ├─ Botão ENTER
    │       └─ Botão ⌫ (delete)
    │
    ├── CONTROLES
    │   ├── handle_keypress(event)
    │   ├── add_letter(char)
    │   ├── delete_letter()
    │   └── submit_guess()
    │
    ├── LÓGICA
    │   ├── update_grid()
    │   │   └─ Mostra letras no grid
    │   │
    │   ├── submit_guess()
    │   │   ├─ Valida palpite
    │   │   ├─ Calcula cores
    │   │   ├─ Atualiza teclado
    │   │   ├─ Verifica vitória
    │   │   └─ Verifica game over
    │   │
    │   └── update_key_color(char, color)
    │       └─ Muda cor do botão
    │
    └── UTILITÁRIOS
        └── Constantes de cores
```

---

## 📚 Lógica do Jogo

### 🎯 Sistema de Cores

```python
COLOR_CORRECT = "#6aaa64"      # Verde (letra certa, lugar certo)
COLOR_MISPLACED = "#c9b458"    # Amarelo (letra certa, lugar errado)
COLOR_WRONG = "#787c7e"        # Cinza (letra não existe)
COLOR_EMPTY = "#3a3a3c"        # Cinza escuro (célula vazia)
```

**Prioridade de cores**:
1. Se green (correto) em posição: GREEN
2. Se yellow (misplaced): YELLOW (mas não sobrescreve GREEN)
3. Se gray (errado): GRAY

---

### 🔍 Verificação do Palpite

```python
def submit_guess(self):
    guess = self.current_guess
    
    # Para cada palavra:
    for w_idx in range(self.num_words):
        secret = list(self.secret_words[w_idx])
        colors = [COLOR_WRONG] * self.word_len
        
        # PASSO 1: Marcar corretos (green)
        for i in range(self.word_len):
            if guess[i] == secret[i]:
                colors[i] = COLOR_CORRECT
                secret[i] = None  # Marca como usado
        
        # PASSO 2: Marcar misplaced (yellow)
        for i in range(self.word_len):
            if colors[i] != COLOR_CORRECT and guess[i] in secret:
                colors[i] = COLOR_MISPLACED
                secret[secret.index(guess[i])] = None  # Marca como usado
        
        # PASSO 3: Aplicar cores ao grid
        for i, color in enumerate(colors):
            cell.configure(fg_color=color)
        
        # PASSO 4: Verificar vitória
        if guess == self.secret_words[w_idx]:
            self.words_solved[w_idx] = True
    
    # PASSO 5: Verificar fim do jogo
    if all(self.words_solved):
        VITÓRIA!
    elif self.current_attempt == self.max_attempts - 1:
        GAME OVER!
```

---

### 📊 Exemplo Passo a Passo

```
PALAVRA SECRETA: PIZZA
PALPITE: PARRA

PASSO 1 (Corretos):
P I R R A
✓ - - - -
Posições 0 corretas
secret = [None, I, Z, Z, A]

PASSO 2 (Misplaced):
P I R R A
✓ 🟨 - - ✓
I está em secret mas em posição errada
A está em secret e em posição correta
secret = [None, None, Z, Z, None]

RESULTADO:
P=GREEN    (posição 0 correta)
I=YELLOW   (existe mas posição errada)
R=GRAY     (não existe segunda vez)
R=GRAY     (não existe segunda vez)
A=GREEN    (posição 4 correta)

TECLADO:
P: GREEN (não muda mais)
I: YELLOW
R: GRAY
A: GREEN
```

---

## 📊 Fórmula de Tentativas

```
Tentativas = Num_Palavras + 5

1 palavra: 1 + 5 = 6 tentativas
2 palavras: 2 + 5 = 7 tentativas
3 palavras: 3 + 5 = 8 tentativas
4 palavras: 4 + 5 = 9 tentativas
```

---

## 🚀 Como Rodar

### ✅ Pré-requisitos

- Python 3.7+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/wordle-pro.git
cd wordle-pro
```

2. **Crie ambiente virtual**:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências**:
```bash
pip install customtkinter
```

4. **Execute**:
```bash
python termo.py
```

5. **Interface deve aparecer**:
   - Menu de seleção
   - Escolha modo e tamanho
   - Comece a jogar!

---

## 📄 requirements.txt

```
customtkinter>=5.0.0
```

---

## 🎯 Estratégias de Jogo

### 📝 Dicas para Ganhar

1. **Primeira Palavra**:
   - Use vogais (A, E, I, O, U)
   - Exemplo: AUDIO, ORADE
   - Objetivo: descobrir quais letras existem

2. **Segunda Palavra**:
   - Use consoantes comuns
   - Exemplo: CINTA, FORTE
   - Objetivo: refinar posições

3. **Terceira Palavra**:
   - Use feedback anterior
   - Mude letras que não funcionam
   - Objetivo: descobrir a palavra

4. **Dica Final**:
   - Pense em padrões
   - Considere palavras comuns
   - Não adivinhe aleatoriamente

---

## 🐛 Troubleshooting

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: Letras não aparecem no grid
**Causa**: Jogo não iniciado  
**Solução**: Clique "JOGAR AGORA" no menu

### ❌ Problema: Teclado não funciona
**Causa**: Janela sem foco  
**Solução**: Clique na janela do jogo

### ❌ Problema: Não consigo submeter palpite
**Causa**: Palavra não tem comprimento correto  
**Solução**: Preencha todas as letras antes de ENTER

### ❌ Problema: Palavra não existe na lista
**Causa**: Palavra não foi adicionada  
**Solução**: Veja a lista em `term.py` (linhas 21-37)

---

## ⚙️ Customização

### Adicionar Novas Palavras

```python
self.full_word_list = [
    # 5 LETRAS
    "ARROZ", "PIZZA", "CARNE",
    # Adicione aqui:
    "SAPATO",  # Nova palavra de 6 letras
    
    # 6 LETRAS
    "QUEIJO", "BANANA", "TOMATE",
    # ...
]
```

### Alterar Cores

```python
COLOR_CORRECT = "#6aaa64"      # Mude para "#00FF00" (verde puro)
COLOR_MISPLACED = "#c9b458"    # Mude para "#FFFF00" (amarelo puro)
COLOR_WRONG = "#787c7e"        # Mude para "#808080" (cinza puro)
```

### Aumentar Tentativas

```python
# Altere a fórmula:
# Padrão:
self.max_attempts = self.num_words + 5

# Novo:
self.max_attempts = self.num_words + 10  # Mais fácil
```

---

## 💡 Extensões Possíveis

- [ ] **Persistência**: Salvar score/histórico
- [ ] **Temas**: Light/Dark mode customizável
- [ ] **Dificuldade**: Hard mode (sem hints)
- [ ] **Multiplayer**: Online vs outro jogador
- [ ] **Estatísticas**: Gráficos de desempenho
- [ ] **Achievements**: Badges por desafios
- [ ] **Som**: Efeitos sonoros
- [ ] **Idiomas**: Suportar múltiplos idiomas
- [ ] **API**: Banco de dados de palavras
- [ ] **Mobile**: Versão mobile responsiva

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use livremente para fins educacionais e comerciais!

---

## 🌟 Se gostou, considere dar uma ⭐!

```
   🎮 WORDLE PRO: JOGUE MAIS, ADIVINHE MELHOR

   Múltiplos modos, tamanhos variáveis,
   feedback profissional

   ⭐ DESAFIE SEU VOCABULÁRIO ⭐
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Multi-Modo Edition  
**Status**: ✅ Production Ready  
**Foco**: Jogabilidade, Customização, Desafio

---
