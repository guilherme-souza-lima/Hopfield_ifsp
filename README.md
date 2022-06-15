Hopfield Network IA
==============================

## :art: Resumo ##
Este código Python é apenas uma implementação simples de Hopfield Network discreta (http://en.wikipedia.org/wiki/Hopfield_network). A Discrete Hopfield Network pode aprender/memorizar padrões e lembrar/recuperar os padrões quando a rede alimenta aqueles com ruídos.

![IMAGE](img/Hopfield-net.png)


## :memo: Como executar o código ##
Use o comando para atualizar o `pip`:
```
make update
```
Use o comando para instalar as `bibliotecas`:
```
make install
```
Use o comando para rodar a `aplicação`:
```
make run
```

## :sparkles: Instruções ##
* A aplicação vai memorizar a foto que esta na pasta `train_pics`.
* A aplicação vai pegar a foto que esta na pasta `test_pics`, e com a memorização vai retirar os ruídos da foto.
* E salvar a foto na raiz.

## :construction: Informações ##
- `theta` é o limiar de ativação do neurônio.
- `time` é um parâmetro que informa os passos de memorização das imagens aprendidas. À medida que o número de etapas aumenta, a imagem lembrada é mais precisa.
- `size` é o tamanho da imagem em pixels. Se você colocar uma foto com tamanhos diferentes, o código redimensiona.
- `threshold` é o limite de corte para binarizar o brilho de 1 byte (0 a 255).
- `current_path` deve ser o caminho da pasta de trabalho atual (o modo usual é os.getcwd())
- #### Essas opções estão no arquivo [main.py](https://github.com/guilherme-souza-lima/Hopfield_ifsp/blob/master/main.py#L14).