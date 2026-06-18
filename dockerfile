# Imagem base: Python 3.14 escolhi essa porque é a versão que eu estamos rodando localmente, além disso é uma imagem oficial do Python, garantindo compatibilidade e padronização do ambiente.
# O slim é bem mais leve que a imagem cheia, então acaba sendo relativamente fácil para aplicar. Isso se dá pois a versão "slim" remove ferramentas de desenvolvimento e pacotes não essenciais
# Seria recomendado usar a versão full se fosse necessário compilar dependências nativas, que não é o nosso caso.
# 120 MB a 150 MB VS 900 MB a 1 GB

FROM python:3.14-slim

#Aqui é definido o diretório padrão
WORKDIR /app

#Copiado apenas o requirements para não haver necessidade de reinstalar tudo em cada mudança de código, facilitando os rebuilds.
COPY requirements.txt .

#Instala as dependências para que rodem na imagem, o uso do --no-cache-dir é para evitar que o pip armazene os arquivos de instalação em cache, economizando espaço da imagem.
#Realizamos um teste e a diferença foi mínima 215.49 MB para 212.06 MB, então optamos por não usar o --no-cache-dir.
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Documenta que a app usa a porta 5000 (porta padrão do Flask). 
EXPOSE 5000

#Pesquisando sobre a diferença entre o ENTRYPOINT e o CMD, optei pelo CMD, porque espero um comportamento padrão e que eu possa facilmente passar outro comando no docker run, visto que o ENTRYPOINT é mais difícil de substituir.
CMD ["python", "app.py"]