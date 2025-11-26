# Snake AI - Aprendizado por Reforço com PyTorch

Um projeto de inteligência artificial que utiliza Deep Q-Learning (DQN) para treinar um agente a jogar o clássico jogo Snake. O agente aprende através de tentativa e erro, melhorando seu desempenho ao longo do tempo.

## 🎯 Sobre o Projeto

Este projeto implementa um agente de aprendizado por reforço que aprende a jogar Snake usando uma rede neural profunda. O algoritmo Deep Q-Network (DQN) permite que o agente aprenda a estratégia ótima através da experiência, sem necessidade de programação explícita das regras do jogo.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **PyTorch** - Framework de deep learning
- **Pygame** - Biblioteca para desenvolvimento de jogos
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de dados
- **IPython** - Ambiente interativo

## 📁 Estrutura do Projeto

```
snake-ai-pytorch/
├── agent.py              # Implementação do agente de aprendizado por reforço
├── game.py               # Lógica do jogo Snake para treinamento da IA
├── model.py              # Arquitetura da rede neural e treinador
├── helper.py             # Funções auxiliares para visualização
├── snake_game_human.py   # Versão do jogo para jogadores humanos
├── arial.ttf             # Fonte para renderização de texto
└── pyproject.toml        # Configuração do projeto e dependências
```

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd snake-ai-pytorch
```

2. Instale as dependências:
```bash
pip install -e snake-ai-pytorch/
```

Ou instale manualmente:
```bash
pip install torch pygame numpy matplotlib ipython
```

## 🎮 Como Usar

### Treinar a IA

Para treinar o agente de IA, execute:

```bash
cd snake-ai-pytorch
python agent.py
```

O agente começará a jogar e aprender. Durante o treinamento, você verá:
- A janela do jogo com a cobra sendo controlada pela IA
- Gráficos mostrando a evolução da pontuação
- Informações no console sobre o progresso do treinamento

O modelo será salvo automaticamente na pasta `model/` sempre que um novo recorde for alcançado.

### Jogar Manualmente

Para jogar o jogo manualmente (sem IA), execute:

```bash
cd snake-ai-pytorch
python snake_game_human.py
```

Use as setas do teclado para controlar a cobra:
- ⬆️ Seta para cima
- ⬇️ Seta para baixo
- ⬅️ Seta para esquerda
- ➡️ Seta para direita

## 🧠 Como Funciona

### Deep Q-Learning (DQN)

O agente utiliza uma rede neural para aproximar a função Q, que estima o valor de tomar uma ação específica em um estado dado. A rede neural recebe:

**Entrada (11 características):**
- Perigo à frente, à direita e à esquerda
- Direção atual do movimento (4 valores)
- Localização da comida relativa à cabeça (4 valores)

**Saída (3 ações):**
- Continuar em frente
- Virar à direita
- Virar à esquerda

### Sistema de Recompensas

- **+10 pontos**: Quando a cobra come a comida
- **-10 pontos**: Quando a cobra colide (parede ou próprio corpo)

### Estratégia de Exploração

O agente utiliza uma estratégia ε-greedy:
- Inicialmente, explora mais (movimentos aleatórios)
- Gradualmente, explora menos e explora mais (usa a rede neural)
- O valor de ε diminui conforme o número de jogos aumenta

### Memória de Experiência

O agente armazena experiências (estado, ação, recompensa, próximo estado) em uma memória de replay. Durante o treinamento:
- **Treinamento de memória curta**: Aprende imediatamente após cada ação
- **Treinamento de memória longa**: Aprende a partir de um batch aleatório de experiências passadas

## 📊 Parâmetros de Treinamento

Os principais hiperparâmetros configuráveis em `agent.py`:

- `MAX_MEMORY = 100,000` - Tamanho máximo da memória de replay
- `BATCH_SIZE = 1000` - Tamanho do batch para treinamento
- `LR = 0.001` - Taxa de aprendizado
- `gamma = 0.9` - Fator de desconto para recompensas futuras
- `epsilon = 80 - n_games` - Taxa de exploração (diminui com o tempo)

## 📈 Monitoramento

Durante o treinamento, o sistema gera gráficos em tempo real mostrando:
- Pontuação de cada jogo
- Média de pontuação ao longo do tempo

Isso permite visualizar o progresso do aprendizado do agente.

## 🎯 Objetivos de Melhoria

Algumas melhorias possíveis para o projeto:
- Implementar Double DQN
- Adicionar Dueling DQN
- Implementar experiência prioritizada
- Adicionar mais características ao estado
- Ajustar hiperparâmetros para melhor desempenho

## 📝 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

## 👨‍💻 Autor

Desenvolvido como projeto de aprendizado em Deep Reinforcement Learning.

---

**Nota**: O treinamento pode levar várias horas para alcançar um bom desempenho. Seja paciente e observe a melhoria gradual nas pontuações!
```

O README inclui:
- Descrição do projeto
- Tecnologias utilizadas
- Estrutura do projeto
- Instruções de instalação e uso
- Explicação do algoritmo DQN
- Parâmetros de treinamento
- Informações sobre monitoramento

Você está em modo de leitura. Para aplicar as alterações, copie o conteúdo acima para o arquivo `README.md` ou alterne para o modo de edição.
