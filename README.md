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
**Impulse(N)**: 246.55
**Takeoff Velocity(m/s)**: 2.18
**Jump Height(m)**: 0.24  
**Reactive Strength Index(m/W)**: 0.284
**Peak Power(W)**: 2270.407



**Drop Jump**:
**Takeoff Velocity(m/s)**: 1.72
**Jump Height(m)**: 0.15
**Contact Time(s)**: 0.257
**Flight Time(s)**: 0.35
**Reactive Strength Index(m/W)**: 0.584
**Peak Power(W)**: 2852.726

**Lateral Jump**:   

**First Peak Force(N)**: 1865,362
**Second Peak Force(N)**: 1682,281
**Third Peak Force(N)**: 2356,501