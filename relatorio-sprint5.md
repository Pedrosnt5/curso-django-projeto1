# Relatorio Sprint 5 - Submissoes e Fluxo de Apresentacao

**Data de Inicio:** 30 de maio de 2026  
**Responsavel:** Pedro SS  
**Status:** Em andamento

---

## Objetivo da Sprint

Consolidar o fluxo de submissoes com regras de negocio mais consistentes entre frontend e backend, com foco em:
- Integracao de campos dinamicos por modalidade
- Padronizacao do fluxo de evento/espaco
- Qualidade do fluxo de edicao/listagem
- Estabilidade para entrega e suporte operacional

---

## Regra de Registro (Obrigatoria)

A partir desta sprint, **toda alteracao relevante** deve ser registrada neste arquivo no momento em que for concluida, com:
1. Data
2. Arquivo(s)
3. O que foi alterado
4. Impacto funcional
5. Status de validacao (manual, lint, teste, etc.)

---

## Changelog da Sprint 5

### [30/05/2026] - Inicializacao do relatorio da Sprint 5

- **Arquivos:** `relatorio-sprint5.md`
- **Alteracao:** Criacao da estrutura base do relatorio da sprint com padrao de registro continuo.
- **Impacto funcional:** Melhora a rastreabilidade das entregas e facilita comunicacao com equipe e cliente.
- **Validacao:** Estrutura criada e pronta para atualizacao a cada alteracao.
- **Status:** Concluido

### [30/05/2026] - Atração usando área de conhecimento do model

- **Arquivos:** `backend/api/views/choices_atracao_view.py`
- **Alteracao:** Endpoint `atracoes/opcoes/` atualizado para carregar `areas_conhecimento` a partir do model `AreaConhecimento`, em vez de usar o enum direto.
- **Impacto funcional:** O formulário de submissão de atração passa a refletir as áreas efetivamente cadastradas no banco.
- **Validacao:** Revisao do endpoint e checagem de sintaxe sem erros.
- **Status:** Concluido

### [30/05/2026] - Remocao de espaco na submissao/edicao de atracao

- **Arquivos:** `frontend/src/components/common/criarAtracaoCard.jsx`, `frontend/src/pages/AdicionarAtracao.jsx`, `frontend/src/pages/ListarAtracoes.jsx`, `frontend/src/services/atracaoService.js`
- **Alteracao:** Campo `Espaço` removido das telas de submissão e edição de atração; validações de obrigatoriedade removidas; payload de submissão/edição ajustado para não enviar `espaco`.
- **Impacto funcional:** O local passa a não ser definido no momento da submissão, ficando disponível para definição posterior no fluxo de programação por coordenadores.
- **Validacao:** Checagem de sintaxe nos arquivos alterados sem erros.
- **Status:** Concluido

### [31/05/2026] - Multi selecao de nivel de ensino (submissao e edicao)

- **Arquivos:** `backend/api/serializers/atracao_serializer.py`, `frontend/src/components/common/criarAtracaoCard.jsx`, `frontend/src/pages/AdicionarAtracao.jsx`, `frontend/src/pages/ListarAtracoes.jsx`, `frontend/src/services/atracaoService.js`, `frontend/src/utils/formatNivelEnsino.js`
- **Alteracao:** Fluxo de `nivel_ensino` atualizado para permitir selecao de multiplos itens por checkbox no frontend e persistencia em CSV no backend, com validacao de escolhas permitidas e exibicao formatada na listagem/edicao.
- **Impacto funcional:** Usuarios conseguem selecionar mais de um nivel de ensino de forma usavel, sem depender de seletor multiplo com Ctrl.
- **Validacao:** Checagem de erros nos arquivos alterados e testes manuais de submissao/edicao.
- **Status:** Concluido

### [31/05/2026] - Filtro de modalidades elegiveis para submissao

- **Arquivos:** `backend/api/views/choices_atracao_view.py`
- **Alteracao:** Endpoint de opcoes da atracao passou a listar somente modalidades ativas com `requer_avaliacao_submissao=True`.
- **Impacto funcional:** Modalidades que nao exigem avaliacao de submissao deixam de aparecer no formulario de envio de trabalho.
- **Validacao:** Revisao do endpoint e validacao manual de opcoes no frontend.
- **Status:** Concluido

### [31/05/2026] - Sugestao opcional de vagas por modalidade

- **Arquivos:** `backend/api/models/atracao.py`, `backend/api/serializers/atracao_serializer.py`, `frontend/src/components/common/criarAtracaoCard.jsx`, `frontend/src/pages/AdicionarAtracao.jsx`, `frontend/src/pages/ListarAtracoes.jsx`, `frontend/src/services/atracaoService.js`
- **Alteracao:** Adicionado campo opcional de sugestao de vagas na atracao, com checkbox para habilitar no formulario, limite maximo baseado em `modalidade.limite_vagas` e mensagem contextual por modalidade.
- **Impacto funcional:** Submissor pode sugerir quantidade de vagas para o trabalho respeitando a regra da modalidade, sem tornar o preenchimento obrigatorio.
- **Validacao:** Testes manuais de criacao e edicao, incluindo cenarios com limite definido e sem limite.
- **Status:** Concluido

### [31/05/2026] - Ajustes de robustez de validacao e persistencia

- **Arquivos:** `backend/api/serializers/atracao_serializer.py`, `backend/api/models/atracao.py`
- **Alteracao:** Tratamento de entradas de `nivel_ensino` com aspas/JSON para evitar erro de choice invalida; ajuste no `save()` para gerar `slug` a partir de `titulo`; exclusao de `slug` no `full_clean` do serializer para evitar validacao precoce indevida.
- **Impacto funcional:** Reducao de erros de submissao em payloads variaveis e maior estabilidade na criacao de atracoes.
- **Validacao:** Reproducao dos erros reportados e confirmacao da correcao apos ajuste.
- **Status:** Concluido

### [31/05/2026] - Observacao de processo (migrations)

- **Arquivos:** N/A (processo da equipe)
- **Alteracao:** Mantida a regra do projeto de nao versionar migrations no commit desta entrega.
- **Impacto funcional:** Cada desenvolvedor deve gerar/aplicar migrations localmente no proprio ambiente quando sincronizar as alteracoes.
- **Validacao:** Regra aplicada no fluxo de commit/push desta sessao.
- **Status:** Concluido

### [31/05/2026] - Implementacao do model Autoria

- **Arquivos:** `backend/api/enumerations/tipo_autoria.py`, `backend/api/models/autoria.py`, `backend/api/serializers/autoria_serializer.py`
- **Como era:** A equipe da submissao era tratada apenas pelo fluxo legado de `Coautor`, sem entidade especifica para autoria com ordenacao.
- **Como ficou:** Criada a entidade `Autoria` com `ordem`, `tipo`, `usuario` e `submissao`, incluindo enum de tipos (`AUTOR`, `COAUTOR`, `ORIENTADOR`) e serializer dedicado.
- **Impacto funcional:** Passamos a ter estrutura de dominio propria para autoria, preparando filtro e ordenacao por autoria.
- **Validacao:** Revisao de codigo, checagem de erros no editor e persistencia funcionando no fluxo de submissao.
- **Status:** Concluido

### [31/05/2026] - Integracao de autoria no serializer de Atracao

- **Arquivos:** `backend/api/serializers/atracao_serializer.py`
- **Como era:** O backend recebia `equipe_json` como principal e nao garantia regras completas de autoria.
- **Como ficou:** O backend passou a receber/processar `autoria_json`, sincronizar autorias na submissao e manter fallback temporario de compatibilidade com `equipe_json`.
- **Impacto funcional:** Criacao e edicao de submissao passaram a persistir equipe via `Autoria`, com transicao segura sem quebrar telas antigas.
- **Validacao:** Testes manuais de criacao/edicao e verificacao do retorno com `autorias`.
- **Status:** Concluido

### [31/05/2026] - Regras de negocio de autoria (autor unico e ordem)

- **Arquivos:** `backend/api/serializers/atracao_serializer.py`, `backend/api/serializers/autoria_serializer.py`
- **Como era:** Nao havia validacao completa para ordem e cardinalidade de autor no novo payload de autoria.
- **Como ficou:** Validacoes adicionadas para: exatamente 1 `AUTOR`, `ordem` inteira/positiva/nao repetida e usuario sem duplicidade; serializer de autoria passou a expor `usuario_nome/nome`.
- **Impacto funcional:** Evita inconsistencias de equipe e melhora exibicao de autores no frontend.
- **Validacao:** `manage.py check`, testes de payload invalido e teste de submissao valida.
- **Status:** Concluido

### [31/05/2026] - Frontend migrado para autoria_json/autorias

- **Arquivos:** `frontend/src/services/atracaoService.js`, `frontend/src/pages/ListarAtracoes.jsx`, `frontend/src/pages/ProgramacaoEvento.jsx`, `frontend/src/pages/SessaoBoard.jsx`
- **Como era:** Frontend dependia majoritariamente do fluxo legado de equipe (`equipe_json` e endpoint antigo de equipe) para envio/edicao/exibicao.
- **Como ficou:** Frontend passou a enviar `autoria_json`, priorizar leitura de `autorias` e usar fallback legado somente para compatibilidade temporaria.
- **Impacto funcional:** Fluxo principal alinhado ao novo dominio de Autoria em criacao, edicao, listagem e exibicao na programacao/sessao.
- **Validacao:** Revisao de diff, checagem de erros no editor e teste manual de submissao/edicao.
- **Status:** Concluido

### [31/05/2026] - Correcao de slug unico na criacao de submissao

- **Arquivos:** `backend/api/models/atracao.py`
- **Como era:** `slug` era gerado somente com `slugify(titulo)`, causando erro de chave unica quando titulos repetiam.
- **Como ficou:** Implementada geracao de slug unico com sufixo incremental (`titulo`, `titulo-1`, `titulo-2`, ...).
- **Impacto funcional:** Eliminou `IntegrityError` por colisao de slug em novos POSTs de atracao.
- **Validacao:** Reproducao do erro e reteste de criacao apos ajuste.
- **Status:** Concluido

### [31/05/2026] - Correcao de compatibilidade no fallback de Coautor

- **Arquivos:** `backend/api/serializers/atracao_serializer.py`
- **Como era:** O fallback legado tentava criar `Coautor` com campos nao suportados (`user_id`, `ordem`), gerando `TypeError`.
- **Como ficou:** Payload legado de equipe passou a ser normalizado antes de criar `Coautor`, mantendo apenas campos validos (`nome`, `instituicao_curso`, `funcao`).
- **Impacto funcional:** Corrigiu falha de criacao de submissao durante periodo de transicao entre equipe antiga e autoria nova.
- **Validacao:** Erro reproduzido e confirmado como resolvido apos novo POST.
- **Status:** Concluido

### [31/05/2026] - Alinhamento de banco local para campo permite_submissao

- **Arquivos:** processo local de banco (`makemigrations/migrate`) e migration gerada localmente
- **Como era:** Ambiente local apresentou erro `no such column: api_modalidade.permite_submissao` por schema defasado.
- **Como ficou:** Schema local alinhado com migrations aplicadas no ambiente de execucao.
- **Impacto funcional:** Endpoints voltaram a responder sem erro de coluna ausente.
- **Validacao:** `manage.py migrate`, `manage.py check` e reteste manual do endpoint.
- **Status:** Concluido

---

## Backlog Tecnico (Sprint 5)

- [ ] Revisar pontos pendentes do fluxo de submissoes apos integracoes recentes
- [ ] Confirmar se o relacionamento de equipe precisa evoluir para vinculo total com usuarios
- [ ] Revisar exibicao e consistencia de espaco/local na listagem
- [ ] Documentar estado final do upload de PDF e estrategia de armazenamento
- [ ] Fechamento tecnico para commit final da sprint

---

## Observacoes

- Manter linguagem clara para leitura por perfil tecnico e nao tecnico.
- Evitar termos ambiguos entre "atracao" e "submissao" quando o contexto ainda estiver em avaliacao.
- Sempre que houver mudanca de regra de negocio, registrar tambem a justificativa.
