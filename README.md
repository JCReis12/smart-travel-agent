# ✈️ Smart Travel Agent

O **Smart Travel Agent** é um sistema baseado em agentes inteligentes desenvolvido para auxiliar usuários no planejamento de viagens de forma personalizada e organizada.

A aplicação utiliza uma arquitetura **multiagente**, na qual um agente principal é responsável por entender a solicitação do usuário e coordenar agentes especialistas, cada um focado em uma etapa específica do planejamento da viagem.

## Objetivo

O projeto tem como objetivo oferecer uma experiência mais completa na organização de viagens, reunindo informações e recomendações em um único fluxo de conversa. A partir das preferências do usuário, o sistema é capaz de sugerir opções de voos, hospedagens, roteiros e estimativas de orçamento.

## Agentes

- **Concierge Agent:** interpreta a solicitação do usuário e coordena os demais agentes.
- **Flights Agent:** pesquisa e recomenda opções de voos.
- **Hotels Agent:** sugere hospedagens de acordo com o perfil da viagem.
- **Itinerary Agent:** cria roteiros personalizados com atividades e atrações.
- **Budget Agent:** estima os custos da viagem e auxilia no planejamento financeiro.

## Tecnologias

- Python
- Google Agent Development Kit (ADK)
- Large Language Models (LLMs)

## Arquitetura

A divisão das responsabilidades entre agentes especialistas torna o sistema mais organizado, modular e escalável, permitindo a adição de novos agentes e funcionalidades conforme a evolução do projeto.

```
Usuário
    │
    ▼
Concierge Agent
    │
 ┌──┼───────────────┬──────────────┬─────────────┐
 ▼                  ▼              ▼             ▼
Flights        Hotels        Itinerary      Budget
 Agent           Agent          Agent         Agent
```
