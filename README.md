# Benchmarking 

A ideia é criar um benchmarking para comparar o desempenho de diferentes servidores web e linguagens de programação.

Para isso vamos utilizar um pacote golang chamado [bombardier](https://github.com/codesenberg/bombardier).

## Instalação

```bash
go install github.com/codesenberg/bombardier@latest
```

Mover o binário para o diretório de binários do sistema operacional. Exemplo:
```bash
sudo mv $(go env GOPATH)/bin/bombardier /usr/local/bin
```

## Execução

### Servidor .NET Core
```bash
cd dotnet 
dotnet run
```

### Servidor Go
```bash
cd go
go run main.go
```

### Servidor Python
```bash
cd python
virtualenv --python=python3.11 venv
source venv/bin/activate
pip install .
python main.py
```

### Executando o benchmarking
Para .NET Core
```bash
bombardier -n 50000 -m GET -r 10000 -l http://localhost:5000/api/v1/products
```

Para Go
```bash
bombardier -n 50000 -m GET -r 10000 -l http://localhost:8080/api/v1/products
```

Para Python
```bash
bombardier -n 50000 -m GET -r 10000 -l http://localhost:7000/api/v1/products
```

Para entender os parâmetros do comando, execute:
```bash
bombardier -help
```

Legenda de parâmetros:
- `-n` número de requisições
- `-m` método HTTP
- `-r` número de requisições por segundo

Veja mais exemplos em [bombardier](https://pkg.go.dev/github.com/codesenberg/bombardier).

## Referências
https://github.com/codesenberg/bombardier  
https://pkg.go.dev/github.com/codesenberg/bombardier



