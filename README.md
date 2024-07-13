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

**SCM**:
- **Impulse(N)**: 246.55
- **Takeoff Velocity(m/s)**: 2.18
- **Jump Height(m)**: 0.24  
- **Reactive Strength Index(m/W)**: 0.284
- **Peak Power(W)**: 2270.407

<div align="center">
	<img src="https://github.com/user-attachments/assets/0c70f707-51e7-4587-8b44-ec79b3cb966e" alt="scm" width="700">
</div>

**Drop Jump**:
- **Takeoff Velocity(m/s)**: 1.72
- **Jump Height(m)**: 0.15
- **Contact Time(s)**: 0.257
- **Flight Time(s)**: 0.35
- **Reactive Strength Index(m/W)**: 0.584
- **Peak Power(W)**: 2852.726

<div align="center">
  <img src="https://github.com/user-attachments/assets/5a47549e-5f7d-44ed-afed-c87d42936b27" alt="drop" width="700">
</div>

**Lateral Jump**:   
- **First Peak Force(N)**: 1865,362
- **Second Peak Force(N)**: 1682,281
- **Third Peak Force(N)**: 2356,501
- **Fourth  Peak Force(N)**: 2848,445
- **Fifth Peak Force(N)**: 2693,777517

<div align="center">
  <img src="https://github.com/user-attachments/assets/ce659e66-f063-481b-883f-8bdd32226685" alt="sl" width="500">
</div>
