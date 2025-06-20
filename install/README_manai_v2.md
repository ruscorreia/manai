# Manai - Assistente Linux com IA (Versão 2.0)

## Descrição

O `manai` é um comando Linux que permite interagir com páginas de manual (man pages) de forma intuitiva, utilizando linguagem natural e inteligência artificial. Esta versão 2.0 integra-se com uma Azure Function que comunica com um agente de IA no Azure AI Foundry.

## Funcionalidades

### Versão 2.0 - Integração com Azure AI
- **Processamento com IA Real**: Utiliza um agente de IA no Azure AI Foundry
- **Suporte Multilingue**: Aceita perguntas em qualquer idioma e responde no mesmo idioma
- **Sessões Contínuas**: Mantém contexto entre perguntas para conversações naturais
- **Interface Melhorada**: Feedback visual e mensagens de erro mais claras
- **Configuração Flexível**: Suporte para diferentes ambientes através de variáveis de ambiente

### Funcionalidades Principais
- **Interação por Linguagem Natural**: Aceita perguntas em português, inglês ou qualquer outro idioma
- **Respostas Contextuais**: Fornece respostas precisas baseadas nas páginas man do Linux
- **Gestão de Sessões**: Mantém o contexto da conversa para perguntas de seguimento
- **Configuração Simples**: Fácil configuração através de variáveis de ambiente

## Instalação

### Pré-requisitos

1. **Python 3.6 ou superior**
2. **Biblioteca requests**: `pip install requests`
3. **Azure Function configurada** com o agente manai

### Passos de Instalação

1. **Descarregue o ficheiro `manai.py`**

2. **Instale as dependências**:
   ```bash
   pip install requests
   ```

3. **Torne o script executável**:
   ```bash
   chmod +x manai.py
   ```

4. **Copie para um directório no PATH** (opcional):
   ```bash
   sudo cp manai.py /usr/local/bin/manai
   ```

## Configuração

### Variáveis de Ambiente Obrigatórias

Configure a URL da sua Azure Function:

**Linux/macOS:**
```bash
export MANAI_AZURE_FUNCTION_URL='https://sua-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger'
```

**Windows:**
```cmd
set MANAI_AZURE_FUNCTION_URL=https://sua-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger
```

### Variáveis de Ambiente Opcionais

Se a sua Azure Function requer uma chave de acesso:

**Linux/macOS:**
```bash
export MANAI_FUNCTION_KEY='sua-chave-da-funcao'
```

**Windows:**
```cmd
set MANAI_FUNCTION_KEY=sua-chave-da-funcao
```

### Configuração Permanente

Para tornar a configuração permanente, adicione as variáveis ao seu ficheiro de perfil:

**Linux/macOS** (adicione ao `~/.bashrc` ou `~/.zshrc`):
```bash
echo 'export MANAI_AZURE_FUNCTION_URL="https://sua-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger"' >> ~/.bashrc
echo 'export MANAI_FUNCTION_KEY="sua-chave-da-funcao"' >> ~/.bashrc
source ~/.bashrc
```

## Utilização

### Comandos Básicos

```bash
# Pergunta simples
manai "como listar ficheiros ocultos no Linux?"

# Pergunta em inglês
manai "how to create a directory with specific permissions?"

# Ver informações de configuração
manai --config

# Iniciar nova sessão (ignorar contexto anterior)
manai --new-session "como usar o comando find?"

# Ver versão
manai --version

# Ver ajuda
manai --help
```

### Exemplos de Utilização

```bash
# Perguntas sobre comandos básicos
manai "como copiar ficheiros?"
manai "criar um directório"
manai "ver o conteúdo de um ficheiro"

# Perguntas mais específicas
manai "como encontrar ficheiros modificados nas últimas 24 horas?"
manai "definir permissões 755 para um ficheiro"
manai "comprimir uma pasta com tar"

# Conversação contínua
manai "como usar o comando grep?"
manai "e como posso usar grep com expressões regulares?"
manai "mostrar apenas o número da linha onde encontrou?"
```

### Gestão de Sessões

O manai mantém automaticamente o contexto da conversa:

```bash
# Primeira pergunta
manai "como criar um utilizador no Linux?"

# Pergunta de seguimento (usa o contexto anterior)
manai "e como definir uma palavra-passe para esse utilizador?"

# Iniciar nova conversa
manai --new-session "como instalar pacotes com apt?"
```

## Resolução de Problemas

### Erro: "URL da Azure Function não configurada"

**Causa**: A variável `MANAI_AZURE_FUNCTION_URL` não está definida.

**Solução**:
```bash
export MANAI_AZURE_FUNCTION_URL='https://sua-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger'
```

### Erro: "Erro de comunicação"

**Possíveis causas e soluções**:

1. **Sem ligação à internet**: Verifique a sua conectividade
2. **URL incorrecta**: Confirme a URL da Azure Function
3. **Chave inválida**: Verifique a chave da função
4. **Function App inactiva**: A função pode estar a "despertar" (cold start)

### Erro: "Resposta inválida do servidor"

**Causa**: A Azure Function retornou uma resposta não-JSON.

**Soluções**:
- Verifique se a Azure Function está a funcionar correctamente
- Confirme se está a usar a URL correcta do endpoint
- Verifique os logs da Azure Function para erros

### Problemas de Sessão

Se as sessões não estão a funcionar:

1. **Verificar permissões**: O ficheiro `~/.manai_session` precisa de permissões de escrita
2. **Espaço em disco**: Certifique-se de que há espaço disponível
3. **Reiniciar sessão**: Use `--new-session` para começar de novo

## Funcionalidades Avançadas

### Ficheiro de Sessão

O manai guarda o ID da thread em `~/.manai_session` para manter o contexto entre execuções. Este ficheiro é criado automaticamente e pode ser removido para reiniciar todas as sessões.

### Timeout e Retry

- **Timeout**: 60 segundos por requisição
- **Retry**: Não implementado (a Azure Function tem o seu próprio retry)

### Logging

Para debug, pode verificar:
- Mensagens de erro detalhadas no terminal
- Logs da Azure Function no portal Azure
- Conectividade de rede

## Migração da Versão 1.0

Se está a migrar da versão anterior do manai:

1. **Backup**: Guarde a versão anterior se necessário
2. **Configuração**: Configure as novas variáveis de ambiente
3. **Teste**: Teste com algumas perguntas simples
4. **Sessões**: As sessões antigas não são compatíveis

## Desenvolvimento

### Estrutura do Código

- `ManaiClient`: Classe principal para comunicação com a Azure Function
- `get_config()`: Gestão de configuração
- `main()`: Interface de linha de comando

### Dependências

- `requests`: Para comunicação HTTP
- `json`: Para processamento de dados
- `argparse`: Para interface de linha de comando
- `os`: Para variáveis de ambiente e ficheiros

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Suporte

Para problemas ou sugestões:
1. Verifique a secção de resolução de problemas
2. Confirme a configuração da Azure Function
3. Verifique os logs da Azure Function no portal Azure

## Changelog

### Versão 2.0.0
- Integração completa com Azure Function
- Suporte para múltiplos idiomas
- Sistema de sessões melhorado
- Interface de utilizador aprimorada
- Configuração através de variáveis de ambiente

### Versão 1.0.0
- Versão inicial com processamento local básico

