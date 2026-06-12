### Trabalho G2 de Sistemas Operacionais
#### Stefano Augusto Mossi - 1131685

#### Item 1: 
Escolhi por fazer uma aplicação com python porque é o que mais tenho familiaridade de atuar.
A ideia aqui foi fazer um sistema CRUD para controle de atividades, fazendo requisições em uma API rest com Flask.
Não houve uma dificuldade em aplicar o desenvolvimento aqui, já atuamos com flask na matéria de Computação Distribuida e Hardware.
Ainda assim, para o front-end, fiz o uso de IA, por não ter tanta prática.
Então, fiz o desenvolvimento do back-end e depois solicitei a LLM para fazer a criação de um front-end.

#### Item 2:
Apesar de ser o item 2, esse foi o meu terceiro passo, que foi alterar o dockerfile, conforme a estrutura de referência. Pesquisando sobre a diferença entre o ENTRYPOINT e o CMD, optei pelo CMD, porque espero um comportamento padrão e que eu possa facilmente passar outro comando no docker run, visto que o ENTRYPOINT é mais difícil de substituir.

#### Item 3:
Apesar de ser o item 3, esse foi o segundo passo, que foi realizar a atualização do app.py para contar com o redis, enfrentei o erro 1, conforme o print. Isso estava acontecendo porque o redis não está aponhtando direto no meu computador de desenvolvimento, mas sim pro docker.
Então, a partir do "erro 1", eu fiquei "limitado" a testar o sistema apenas com o docker, que é o que foi desenvolvido logo após o "item 3".

#### Item 4:
Enquanto fazia o docker composer build meu PC desligou, e durante a segunda tentativa, ocorreu o "erro 2". O erro ocorreu porque eu fui direto para o projeto antes de abrir o docker desktop. Após abri-lo, o erro parou de acontecer. Então, começou o "erro 3", que era o wsl não estar instalado, tive que habilitar as features do windows como virtual machine platform, windows hypervisor platform e windows subsystem for linux. Passei algumas horas tentando resolver esse bug e seguir algumas instruções de fóruns da internet (https://github.com/microsoft/WSL/issues/9460), lembrei que tenho o docker instalado em outro PC, então fiz o commit e testarei nesse outro PC.