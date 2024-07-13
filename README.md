# Jumps Project

Este projeto analisa dados de diferentes tipos de saltos utilizando Python. Ele calcula várias métricas como altura do salto, tempo de contato, índice de força reativa e pico de potência a partir dos dados coletados em uma plataforma de força.

## Estrutura do Projeto
O projeto é estruturado da seguinte forma:

- **jumps/**
	- **jump.py**: Define a classe base Jump.
	- **scm.py**: Define a classe Scm para análise de Saltos com Contramovimento (CMJ).
	- **drop_jump.py**: Define a classe Drop_Jump para análise de Saltos em Profundidade.
	- **lateral_jump.**: Define a classe Lateral_Jump para análise de Saltos Laterais .
- **data/**: Diretório contendo os arquivos de dados de saltos.
- **output/**: Diretório onde o arquivo Excel de saída é gerado.
- **main.py**: Script principal que processa os dados e gera o arquivo Excel com os resultados.

## Exemplos dos Gráficos e Dados Gerados

### Salto com Contramovimento

**SCM**:
**Impulse(N)**: 226.33
**Takeoff Velocity(m/s)**: 2.87
**Jump Height(m)**: 0.42 
**RSI**: 0.5004836491728751
**Peak Power(W)**: 2270.4077735383107