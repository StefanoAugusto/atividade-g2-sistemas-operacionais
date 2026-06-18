# Trabalho G2 — Sistemas Operacionais

**Aluno:** Stefano Augusto Mossi  
**Matrícula:** 1131685
**Aluna:** Rhayra Rodrigues Fiorentin  
**Matrícula:** 1135147
---

## Item 1 — Aplicação CRUD com Flask

Escolhi desenvolver a aplicação em Python por ser a linguagem com a qual tenho mais familiaridade.

A proposta foi criar um sistema CRUD para controle de atividades, com requisições a uma API REST construída com Flask. O desenvolvimento não apresentou grandes dificuldades, pois já trabalhamos com Flask na disciplina de Computação Distribuída e Hardware.

Para o front-end, utilizei IA como suporte, dado que não tenho tanta prática nessa área. O fluxo de trabalho foi: desenvolver o back-end primeiro e, em seguida, solicitar à LLM a criação da interface.

---

## Item 2 — Configuração do Dockerfile

> **Ordem de execução:** este foi, na prática, o **terceiro passo** realizado.

Nesta etapa, alterei o `Dockerfile` conforme a estrutura de referência. Ao pesquisar sobre a diferença entre `ENTRYPOINT` e `CMD`, optei pelo `CMD`, pois:

- Permite um comportamento padrão para o container;
- Facilita a substituição do comando via `docker run`, ao contrário do `ENTRYPOINT`, que é mais difícil de sobrescrever.

---

## Item 3 — Integração com Redis

> **Ordem de execução:** este foi, na prática, o **segundo passo** realizado.

Nesta etapa, atualizei o `app.py` para incluir o Redis. Durante o processo, encontrei o **Erro 1** (ver print anexo), causado pelo fato de o Redis não estar apontando para o meu ambiente local de desenvolvimento, mas sim para o Docker.

A partir desse ponto, fiquei limitado a testar o sistema exclusivamente via Docker. Após executar `docker compose up`, o sistema voltou a funcionar corretamente, conforme demonstrado na **Evidência 5**.

---

## Item 4 — Docker Compose e Resolução de Erros

Durante o `docker compose build`, meu PC desligou inesperadamente. Na segunda tentativa, ocorreu o **Erro 2**, causado por ter acessado o projeto sem antes abrir o Docker Desktop. Após abri-lo, esse erro foi resolvido.

Em seguida, surgiu o **Erro 3**: o WSL não estava instalado. Para resolver, habilitei as seguintes features do Windows:

- Virtual Machine Platform
- Windows Hypervisor Platform
- Windows Subsystem for Linux (WSL)

Passei algumas horas tentando resolver o problema seguindo instruções de fóruns, incluindo [esta thread no GitHub](https://github.com/microsoft/WSL/issues/9460). Como não obtive sucesso, lembrei que tenho o Docker instalado em outro PC — fiz o commit e migrei os testes para essa máquina.

No segundo PC, o build foi bem-sucedido. Ainda assim, apareceu o **Erro 4**: faltava a flag `-r` ao instalar os requirements (`pip install -r requirements.txt`). Após a correção, o build foi concluído com sucesso, conforme **Evidência 3**.

Por fim, executei `docker ps` para listar os containers em execução, conforme **Evidência 6**.

Além disso, ao finalizar a a atividade, fiz o **USO DE IA/LLM** apenas para a formatação do arquivo markdown, sendo utilizado o seguinte prompt: 

"Preciso que você melhore a formatação desse markdown. Não faça alterações no texto, apenas formate-o e deixe pronto para publicação."

## Item 5 — Teste de otimização da imagem Docker com no cache dir

Durante o desenvolvimento da imagem docker fiz uma tentativa de otimização do seu tamanho, utilizando a flag `--no-cache-dir` no comando `pip install`. O objetivo era diminuir o espaço da imagem final, evitando o armazenamento de arquivos temporários de instalação das dependências.

No fim das contas a diferença foi miníma, um pouco mais de 3MB, comparando os dois arquivos pelo docker desktop (Evidencia 9). Então optei por não utilizar a flag, preferindo a configuração mais simples sem impacto relevante no resultado final.

## Conclusão
Ao finalizar a atividade, conseguimos botar em práticas as teorias explicadas em aula pelo Professor. Entendendo como funciona um container e quando usar, entender qual é a melhor versão para cada aplicação e também botar em prática um pouco de programação.