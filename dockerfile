# Imagem base: Python 3.14 escolhi essa porque é a versão que eu estou rodando na minha máquina. Também não queria baixar uma imagem de um sistema linux.
# O slim é bem mais leve que a imagem cheia, então acaba relativamente fácil para aplicar.
FROM python:3.14-slim

#Aqui é definido o diretório padrão
WORKDIR /app

#Copiado apenas o requirements para não haver necessidade de reinstalar tudo em cada mudança de código, facilitando os rebuilds.
COPY requirements.txt .

#Instala as dependências para que rodem na imagem.
RUN pip install -r requirements.txt
COPY . .

# Documenta que a app usa a porta 5000 (porta padrão do Flask). 
EXPOSE 5000

#Pesquisando sobre a diferença entre o ENTRYPOINT e o CMD, optei pelo CMD, porque espero um comportamento padrão e que eu possa facilmente passar outro comando no docker run, visto que o ENTRYPOINT é mais difícil de substituir.
CMD ["python", "app.py"]