# 🐍 Snake AI - Aprendizado por Reforço com PyTorch

**Autor:** Lucca Maximus Romagnolli

Um projeto de inteligência artificial que utiliza Deep Q-Learning (DQN) para treinar um agente a jogar o clássico jogo Snake. O agente aprende através de tentativa e erro, melhorando seu desempenho ao longo do tempo.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação no macOS](#-instalação-no-macos)
- [Instalação no Windows](#-instalação-no-windows)
- [Como Usar](#-como-usar)
- [Como Funciona](#-como-funciona)
- [Troubleshooting](#-troubleshooting)
- [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🎯 Sobre o Projeto

Este projeto implementa um agente de aprendizado por reforço que aprende a jogar Snake usando uma rede neural profunda. O algoritmo Deep Q-Network (DQN) permite que o agente aprenda a estratégia ótima através da experiência, sem necessidade de programação explícita das regras do jogo.

### Características Principais:
- ✅ Deep Q-Learning (DQN) para aprendizado
- ✅ Visualização em tempo real do treinamento
- ✅ Gráficos de progresso do aprendizado
- ✅ Salvamento automático do modelo quando bate recorde
- ✅ Modo de jogo manual para humanos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+** - Linguagem de programação
- **PyTorch 2.9.1+** - Framework de deep learning
- **Pygame 2.6.1+** - Biblioteca para desenvolvimento de jogos
- **NumPy 2.3.5+** - Computação numérica
- **Matplotlib 3.10.7+** - Visualização de dados
- **IPython 9.7.0+** - Ambiente interativo

---

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter:

- **Python 3.13 ou superior** instalado
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)

### Verificar Instalações:

```bash
# Verificar Python
python3 --version
# Deve mostrar: Python 3.13.x ou superior

# Verificar pip
pip3 --version
# Deve mostrar: pip 24.x ou similar
```

---

## 🍎 Instalação no macOS

### Passo 1: Instalar Homebrew (se não tiver)

O Homebrew é o gerenciador de pacotes para macOS. Se você ainda não tem, instale:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verificar instalação:**
```bash
which brew
```

### Passo 2: Instalar Dependências do Sistema (SDL2)

O Pygame precisa das bibliotecas SDL2 para funcionar. Instale-as via Homebrew:

```bash
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
```

**O que cada biblioteca faz:**
- `sdl2`: Biblioteca principal para gráficos e eventos
- `sdl2_image`: Suporte para imagens
- `sdl2_mixer`: Suporte para áudio
- `sdl2_ttf`: Suporte para fontes TrueType (necessário para renderizar texto)

### Passo 3: Navegar até o Diretório do Projeto

```bash
cd /Users/luccaromagnolli/Documents/Neural-Networks/snake-ai-pytorch
```

### Passo 4: Criar Ambiente Virtual (Recomendado)

Criar um ambiente virtual isola as dependências do projeto:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate
```

**Resultado esperado:** O prompt mostrará `(venv)` no início.

**Para desativar depois:**
```bash
deactivate
```

### Passo 5: Instalar Dependências Python

```bash
# Opção 1: Instalação via pyproject.toml (Recomendado)
pip install -e .

# Opção 2: Instalação manual (se a opção 1 não funcionar)
pip install torch pygame numpy matplotlib ipython
```

### Passo 6: Verificar Instalação

```bash
pip list | grep -E "(torch|pygame|numpy|matplotlib|ipython)"
```

Todas as 5 bibliotecas devem aparecer na lista.

---

## 🪟 Instalação no Windows

### Passo 1: Instalar Python

1. Baixe o Python 3.13+ do site oficial: [python.org/downloads](https://www.python.org/downloads/)
2. Durante a instalação, **marque a opção "Add Python to PATH"**
3. Verifique a instalação:

```cmd
python --version
```

### Passo 2: Instalar Visual C++ Build Tools (Opcional, mas Recomendado)

O Pygame pode precisar compilar algumas extensões. Para isso, você pode precisar do Visual C++ Build Tools:

1. Baixe o **Visual Studio Build Tools** ou **Visual Studio Community** (versão gratuita)
2. Durante a instalação, selecione "Desktop development with C++"
3. Ou instale diretamente: [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)

**Alternativa mais simples:** O Pygame geralmente vem com wheels pré-compiladas, então este passo pode não ser necessário.

### Passo 3: Abrir Terminal/Prompt de Comando

- Pressione `Win + R`, digite `cmd` e pressione Enter
- Ou use PowerShell (clique com botão direito no menu Iniciar → Windows PowerShell)

### Passo 4: Navegar até o Diretório do Projeto

```cmd
cd C:\Users\SeuUsuario\Documents\Neural-Networks\snake-ai-pytorch
```

**Nota:** Ajuste o caminho conforme a localização do seu projeto.

### Passo 5: Criar Ambiente Virtual (Recomendado)

```cmd
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate
```

**Resultado esperado:** O prompt mostrará `(venv)` no início.

**Para desativar depois:**
```cmd
deactivate
```

### Passo 6: Instalar Dependências Python

```cmd
# Atualizar pip primeiro (recomendado)
python -m pip install --upgrade pip

# Opção 1: Instalação via pyproject.toml (Recomendado)
pip install -e .

# Opção 2: Instalação manual (se a opção 1 não funcionar)
pip install torch pygame numpy matplotlib ipython
```

**Nota:** Se encontrar problemas com PyTorch, tente instalar separadamente:

```cmd
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Passo 7: Verificar Instalação

```cmd
pip list | findstr "torch pygame numpy matplotlib ipython"
```

Todas as 5 bibliotecas devem aparecer na lista.

---

## 🎮 Como Usar

### Treinar a IA (Modo Principal)

Para treinar o agente de IA, execute:

```bash
# macOS/Linux
python3 agent.py

# Windows
python agent.py
```

**O que acontece:**
- Uma janela do jogo (640x480 pixels) será aberta
- A cobra será controlada pela IA
- Gráficos em tempo real mostrarão o progresso do aprendizado
- O modelo será salvo automaticamente na pasta `model/` quando um novo recorde for alcançado

**O que você verá:**
1. **Janela do Jogo:**
   - Cobra (azul) se movendo
   - Comida (vermelha)
   - Pontuação atual no canto superior esquerdo

2. **Gráficos:**
   - Pontuação de cada jogo (linha azul)
   - Média de pontuação ao longo do tempo (linha laranja)

3. **Console:** Mensagens como:
   ```
   Game 1 Score 0 Record: 0
   Game 2 Score 1 Record: 1
   Game 3 Score 0 Record: 1
   ...
   ```

**Para parar:** Feche a janela do jogo ou pressione `Ctrl+C` no terminal.

### Jogar Manualmente (Modo Humano)

Para jogar o jogo manualmente (sem IA):

```bash
# macOS/Linux
python3 snake_game_human.py

# Windows
python snake_game_human.py
```

**Controles:**
- ⬆️ **Seta para cima:** Mover para cima
- ⬇️ **Seta para baixo:** Mover para baixo
- ⬅️ **Seta para esquerda:** Mover para esquerda
- ➡️ **Seta para direita:** Mover para direita

**Objetivo:** Comer a comida (quadrado vermelho) sem colidir com as paredes ou com seu próprio corpo.

---

## 🧠 Como Funciona

### Deep Q-Learning (DQN)

O agente utiliza uma rede neural para aproximar a função Q, que estima o valor de tomar uma ação específica em um estado dado.

### Entrada da Rede Neural (11 características):

1. **Perigo à frente** (1 valor)
2. **Perigo à direita** (1 valor)
3. **Perigo à esquerda** (1 valor)
4. **Direção atual do movimento** (4 valores: esquerda, direita, cima, baixo)
5. **Localização da comida relativa à cabeça** (4 valores: esquerda, direita, cima, baixo)

### Saída da Rede Neural (3 ações):

- **Ação 0:** Continuar em frente
- **Ação 1:** Virar à direita
- **Ação 2:** Virar à esquerda

### Sistema de Recompensas:

- **+10 pontos:** Quando a cobra come a comida
- **-10 pontos:** Quando a cobra colide (parede ou próprio corpo)

### Estratégia de Exploração (ε-greedy):

- Inicialmente, o agente explora mais (movimentos aleatórios)
- Gradualmente, explora menos e explora mais (usa a rede neural)
- O valor de ε diminui conforme o número de jogos aumenta: `ε = 80 - n_games`

### Memória de Experiência (Replay Buffer):

O agente armazena experiências (estado, ação, recompensa, próximo estado) em uma memória de replay:

- **Treinamento de memória curta:** Aprende imediatamente após cada ação
- **Treinamento de memória longa:** Aprende a partir de um batch aleatório de experiências passadas (tamanho: 1000)

### Parâmetros de Treinamento:

- `MAX_MEMORY = 100,000` - Tamanho máximo da memória de replay
- `BATCH_SIZE = 1000` - Tamanho do batch para treinamento
- `LR = 0.001` - Taxa de aprendizado
- `gamma = 0.9` - Fator de desconto para recompensas futuras

---

## 🔧 Troubleshooting

### Problema 1: "SDL.h file not found" (macOS)

**Causa:** SDL2 não está instalado ou não está sendo encontrado.

**Solução:**
```bash
# Instalar SDL2
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf

# Reinstalar pygame
pip uninstall pygame
pip install pygame
```

### Problema 2: "SDL.h file not found" (Windows)

**Causa:** Pygame tentando compilar do código-fonte.

**Solução:**
```cmd
# Desinstalar pygame
pip uninstall pygame

# Instalar versão pré-compilada
pip install pygame

# Se ainda não funcionar, tente:
pip install pygame --only-binary :all:
```

### Problema 3: "ModuleNotFoundError: No module named 'torch'"

**Causa:** As dependências não foram instaladas.

**Solução:**
```bash
# macOS/Linux
pip install -e .

# Windows
pip install -e .
```

### Problema 4: Erro ao instalar PyTorch

**Causa:** Problemas de compatibilidade ou falta de espaço.

**Solução:**
```bash
# Instalar PyTorch separadamente (CPU)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Ou com suporte CUDA (se tiver GPU NVIDIA)
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Problema 5: "arial.ttf not found"

**Causa:** O arquivo de fonte não está no diretório correto.

**Solução:** Certifique-se de estar executando o comando dentro da pasta `snake-ai-pytorch`:

```bash
# Verificar localização
pwd  # macOS/Linux
cd   # Windows

# Navegar até o diretório correto
cd /caminho/para/snake-ai-pytorch
```

### Problema 6: Janela do jogo não abre (Windows)

**Causa:** Problemas com o display gráfico ou drivers.

**Solução:**
1. Atualize os drivers da sua placa gráfica
2. Certifique-se de que está executando em um ambiente com interface gráfica
3. Tente executar como administrador

### Problema 7: Erro de permissão ao instalar (macOS)

**Causa:** Problemas de permissão com pip.

**Solução:**
```bash
# Usar --user
pip install --user -e .

# Ou corrigir permissões
sudo chown -R $(whoami) /usr/local/lib/python3.13/site-packages
```

### Problema 8: Ambiente virtual não ativa (Windows)

**Causa:** Política de execução do PowerShell.

**Solução:**
```powershell
# Executar no PowerShell como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📁 Estrutura do Projeto

```
snake-ai-pytorch/
├── agent.py              # Implementação do agente de aprendizado por reforço
├── game.py               # Lógica do jogo Snake para treinamento da IA
├── model.py              # Arquitetura da rede neural e treinador
├── helper.py             # Funções auxiliares para visualização
├── snake_game_human.py   # Versão do jogo para jogadores humanos
├── arial.ttf             # Fonte para renderização de texto
├── pyproject.toml        # Configuração do projeto e dependências
└── model/                # Criado automaticamente durante o treinamento
    └── model.pth         # Modelo salvo quando bate recorde
```

### Descrição dos Arquivos:

- **`agent.py`**: Contém a classe `Agent` que implementa o algoritmo DQN e a lógica de treinamento
- **`game.py`**: Implementa a classe `SnakeGameAI` com a lógica do jogo Snake
- **`model.py`**: Define a arquitetura da rede neural (`Linear_QNet`) e o treinador (`QTrainer`)
- **`helper.py`**: Funções para plotar gráficos em tempo real do progresso do treinamento
- **`snake_game_human.py`**: Versão do jogo para jogadores humanos testarem suas habilidades
- **`arial.ttf`**: Fonte TrueType necessária para renderizar o texto da pontuação no jogo

---

## 📊 Progresso Esperado do Treinamento

Durante o treinamento, você pode esperar:

- **Jogos 1-10:** Pontuação baixa (0-2), muitos movimentos aleatórios
- **Jogos 10-50:** Começa a melhorar, pontuação média 2-5
- **Jogos 50-100:** Melhora significativa, pontuação média 5-10
- **Jogos 100+:** Pode alcançar pontuações altas (10-20+)

**Nota:** O treinamento pode levar várias horas para alcançar um bom desempenho. Seja paciente e observe a melhoria gradual nas pontuações!

---

## 🎯 Melhorias Futuras

Algumas melhorias possíveis para o projeto:

- ✅ Implementar Double DQN
- ✅ Adicionar Dueling DQN
- ✅ Implementar experiência prioritizada (Prioritized Experience Replay)
- ✅ Adicionar mais características ao estado (visão da grade completa)
- ✅ Ajustar hiperparâmetros para melhor desempenho
- ✅ Adicionar suporte para GPU (CUDA)

---

## ✅ Checklist de Instalação

Antes de executar, verifique:

- [ ] Python 3.13+ instalado
- [ ] Homebrew instalado (macOS) ou Visual C++ Build Tools (Windows)
- [ ] SDL2 instalado via Homebrew (macOS) ou pygame instalado (Windows)
- [ ] Dependências Python instaladas (`pip install -e .`)
- [ ] Arquivo `arial.ttf` presente
- [ ] No diretório correto (`snake-ai-pytorch`)
- [ ] Ambiente virtual criado e ativado (recomendado)

---

## 📝 Licença

Este projeto é de código aberto e está disponível para uso educacional e pessoal.

---

## 👨‍💻 Autor

**Lucca Maximus Romagnolli**

Desenvolvido como projeto de aprendizado em Deep Reinforcement Learning.

---

## 🙏 Agradecimentos

Este projeto foi desenvolvido como uma implementação educacional do algoritmo Deep Q-Learning para aprendizado por reforço.

---

**Boa sorte com o treinamento! 🚀**

