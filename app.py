from flask import Flask, jsonify, request
import os
import redis

app = Flask(__name__)


r = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379, decode_responses=True)

#Uso de IA: Utilizei O IA para fazer o front-end porque não conto com tanta prática
HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gerenciador de Tarefas</title>
<style>
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #eef1f5;
    color: #2b2b2b;
    margin: 0;
    padding: 40px 15px;
  }
  .container {
    max-width: 620px;
    margin: 0 auto;
    background: #fff;
    border: 1px solid #d8dde3;
    border-radius: 8px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    overflow: hidden;
  }
  .cabecalho {
    background: #3b6ea5;
    color: #fff;
    padding: 16px 24px;
  }
  .cabecalho h1 {
    font-size: 20px;
    margin: 0;
    font-weight: 600;
  }
  .cabecalho p {
    margin: 4px 0 0;
    font-size: 13px;
    color: #d6e2f0;
  }
  .conteudo {
    padding: 20px 24px 24px;
  }
  .form {
    display: flex;
    gap: 8px;
    margin-bottom: 18px;
  }
  .form input {
    flex: 1;
    padding: 9px 11px;
    border: 1px solid #b8c0c9;
    border-radius: 5px;
    font-size: 14px;
  }
  .form input:focus {
    outline: none;
    border-color: #3b6ea5;
  }
  button {
    padding: 8px 14px;
    border: 1px solid #b8c0c9;
    border-radius: 5px;
    background: #f1f3f5;
    color: #2b2b2b;
    cursor: pointer;
    font-size: 13px;
  }
  button:hover {
    background: #e4e8ec;
  }
  .btn-add {
    background: #3b6ea5;
    color: #fff;
    border-color: #335f8e;
    font-size: 14px;
  }
  .btn-add:hover {
    background: #335f8e;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    text-align: left;
    padding: 9px 8px;
    border-bottom: 1px solid #e4e8ec;
    font-size: 14px;
  }
  th {
    color: #6b7682;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }
  tbody tr:hover {
    background: #f7f9fb;
  }
  td.acoes {
    text-align: right;
    white-space: nowrap;
  }
  td.acoes button {
    margin-left: 5px;
    padding: 5px 11px;
  }
  .btn-excluir {
    color: #b23b3b;
    border-color: #d9b3b3;
  }
  .btn-excluir:hover {
    background: #f7eaea;
  }
  .vazio {
    color: #8a939d;
    font-style: italic;
    padding: 16px 0;
    text-align: center;
  }
  td input {
    width: 90%;
    padding: 6px 8px;
    border: 1px solid #b8c0c9;
    border-radius: 5px;
    font-size: 14px;
  }
</style>
</head>
<body>
<div class="container">
  <div class="cabecalho">
    <h1>Gerenciador de Tarefas</h1>
    <p>Adicione, edite e remova suas tarefas</p>
  </div>

  <div class="conteudo">
  <div class="form">
    <input id="campoTarefa" placeholder="Digite uma tarefa" autocomplete="off">
    <button class="btn-add" onclick="adicionar()">Adicionar</button>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:50px">#</th>
        <th>Tarefa</th>
        <th style="width:170px"></th>
      </tr>
    </thead>
    <tbody id="corpoTabela"></tbody>
  </table>
  </div>
</div>

<script>
  async function carregar() {
    const resp = await fetch('/api/tasks');
    const lista = await resp.json();
    const corpo = document.getElementById('corpoTabela');

    if (lista.length === 0) {
      corpo.innerHTML = '<tr><td colspan="3" class="vazio">Nenhuma tarefa cadastrada.</td></tr>';
      return;
    }

    corpo.innerHTML = '';
    lista.forEach(function (t) {
      const tr = document.createElement('tr');
      tr.innerHTML =
        '<td>' + t.id + '</td>' +
        '<td>' + t.text + '</td>' +
        '<td class="acoes">' +
          '<button onclick="editar(' + t.id + ', this)">Editar</button>' +
          '<button class="btn-excluir" onclick="excluir(' + t.id + ')">Excluir</button>' +
        '</td>';
      corpo.appendChild(tr);
    });
  }

  async function adicionar() {
    const campo = document.getElementById('campoTarefa');
    const texto = campo.value.trim();
    if (texto === '') return;

    await fetch('/api/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: texto })
    });

    campo.value = '';
    campo.focus();
    carregar();
  }

  function editar(id, botao) {
    const linha = botao.closest('tr');
    const celulaTexto = linha.children[1];
    const celulaAcoes = linha.children[2];
    const valorAtual = celulaTexto.textContent;

    celulaTexto.innerHTML = '<input value="' + valorAtual + '">';
    celulaAcoes.innerHTML =
      '<button onclick="salvar(' + id + ', this)">Salvar</button>' +
      '<button onclick="carregar()">Cancelar</button>';
    celulaTexto.querySelector('input').focus();
  }

  async function salvar(id, botao) {
    const linha = botao.closest('tr');
    const texto = linha.querySelector('input').value.trim();
    if (texto === '') return;

    await fetch('/api/tasks/' + id, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: texto })
    });

    carregar();
  }

  async function excluir(id) {
    if (!confirm('Excluir esta tarefa?')) return;
    await fetch('/api/tasks/' + id, { method: 'DELETE' });
    carregar();
  }

  document.getElementById('campoTarefa').addEventListener('keydown', function (e) {
    if (e.key === 'Enter') adicionar();
  });

  carregar();
</script>
</body>
</html>"""


"""
Explicação rápida da aplicação: escolhi por fazer uma aplicação com python porque é o que mais tenho familiaridade de atuar.
A ideia aqui foi fazer um sistema CRUD para controle de atividades, fazendo requisições em uma API rest com Flask.
Não há uma dificuldade em aplicar o desenvolvimento aqui, já atuamos com flask na matéria de Computação Distribuida e Hardware.
"""

#Essa é a rota principal que será acessada pelo usuário na porta 5000
@app.route('/')
def index():
    return HTML

"""
Essa é a rota de GET para retornar as atividades, se o usuário acessar diretamente o link (http://localhost:5000/api/tasks)
ele vai ter um retorno parecido o que está no "Evidencia 1.png".
"""
@app.route('/api/tasks', methods=['GET'])
def getTasks():
    dados = r.hgetall('tasks')
    lista = [{'id': int(i), 'text': t} for i, t in dados.items()]
    lista.sort(key=lambda x: x['id'])
    return jsonify(lista)

# Requisição post para criar uma atividade
@app.route('/api/tasks', methods=['POST'])
def createTask():
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()
    if not text:
        return jsonify({'error': 'O texto está vazio'}), 400
    novoId = r.incr('next_id')
    r.hset('tasks', novoId, text)
    return jsonify({'id': novoId, 'text': text}), 201

#Requisição que atualiza a task
@app.route('/api/tasks/<int:taskId>', methods=['PUT'])
def updateTask(taskId):
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()
    if not text:
        return jsonify({'error': 'O texto está vazio'}), 400
    if not r.hexists('tasks', taskId):
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    r.hset('tasks', taskId, text)
    return jsonify({'id': taskId, 'text': text})

@app.route('/api/tasks/<int:taskId>', methods=['DELETE'])
def deleteTask(taskId):
    r.hdel('tasks', taskId)
    return '', 204



if __name__ == '__main__':
    print("Servidor rodando em http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)