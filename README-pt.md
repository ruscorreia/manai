# ManAI - Assistente Linux Inteligente

<div align="center">

![ManAI Logo](https://img.shields.io/badge/ManAI-v2.0-blue?style=for-the-badge)
[![Python](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)](https://python.org)
[![Azure](https://img.shields.io/badge/Azure-Functions-blue?style=for-the-badge&logo=microsoft-azure)](https://azure.microsoft.com)
[![Licença](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)](LICENSE)

**Transforme a sua experiência com comandos Linux através de inteligência artificial**

[🚀 Instalação](#instalação) • [📖 Documentação](#utilização) • [🤝 Contribuir](#contribuição) • [🌍 English](README-en.md)

</div>

---

## 🎯 Visão Geral

O **ManAI** revoluciona a forma como interage com o sistema Linux, transformando consultas em linguagem natural em respostas precisas e contextualizadas sobre comandos e funcionalidades do sistema. Desenvolvido pela Rosco Edutec, o ManAI elimina a barreira entre o conhecimento técnico e a utilização eficaz do terminal Linux.

### 🔍 O Problema que Resolvemos

Quantas vezes já se encontrou numa destas situações?

- Precisava de um comando específico mas não se lembrava da sintaxe exacta
- Gastou tempo a navegar por páginas man extensas para encontrar uma funcionalidade simples
- Teve dificuldade em compreender opções complexas de comandos
- Queria uma explicação clara e contextualizada em vez de documentação técnica densa

O ManAI foi criado precisamente para resolver estes desafios, oferecendo uma interface intuitiva que compreende as suas necessidades e fornece respostas imediatas e práticas.

### ✨ Por que Escolher o ManAI?

**Inteligência Artificial Avançada**: Utiliza o poder do Azure AI Foundry para compreender e responder às suas perguntas com precisão excepcional.

**Multilingue por Natureza**: Aceita perguntas em português, inglês, espanhol, francês, alemão, italiano, japonês, chinês, russo e árabe, respondendo sempre no idioma da pergunta.

**Contexto Persistente**: Mantém o contexto das suas conversas, permitindo perguntas de seguimento naturais como "e como posso fazer isso com permissões específicas?"

**Simplicidade de Utilização**: Uma única dependência Python e instalação automatizada tornam o ManAI acessível a todos os utilizadores Linux.

**Integração Cloud Robusta**: Beneficia da escalabilidade e fiabilidade da infraestrutura Azure, garantindo respostas rápidas e disponibilidade constante.

## 🚀 Funcionalidades Principais

### 🧠 Processamento de IA Avançado
O ManAI utiliza modelos de linguagem de última geração hospedados no Azure AI Foundry, garantindo respostas precisas, contextualizadas e actualizadas. O sistema compreende não apenas comandos básicos, mas também cenários complexos e fluxos de trabalho avançados.

### 🌐 Suporte Multilingue Completo
Comunique na sua língua preferida. O ManAI detecta automaticamente o idioma da sua pergunta e responde no mesmo idioma, mantendo a precisão técnica e a clareza da explicação.

### 💬 Gestão Inteligente de Sessões
O sistema mantém o contexto das suas conversas, permitindo diálogos naturais e progressivos. Pode fazer perguntas de seguimento, pedir esclarecimentos ou explorar tópicos relacionados sem perder o fio da conversa.

### ⚡ Performance Optimizada
Com tempos de resposta optimizados e cache inteligente, o ManAI fornece respostas rápidas mesmo para consultas complexas, mantendo a produtividade do seu fluxo de trabalho.

### 🔒 Sistema de Utilizadores Robusto
Inclui sistema completo de registo, autenticação e gestão de perfis, com suporte para diferentes níveis de acesso e funcionalidades premium.

## 📋 Pré-requisitos

Antes de instalar o ManAI, certifique-se de que o seu sistema cumpre os seguintes requisitos:

### Sistema Operativo
- **Linux**: Qualquer distribuição moderna (Ubuntu 18.04+, Debian 10+, CentOS 7+, Fedora 30+, Arch Linux)
- **Arquitectura**: x86_64 (AMD64) ou ARM64

### Software
- **Python**: Versão 3.6 ou superior
- **pip**: Gestor de pacotes Python (normalmente incluído com Python)
- **curl**: Para comunicação HTTP (pré-instalado na maioria das distribuições)

### Conectividade
- **Ligação à Internet**: Necessária para comunicação com os serviços Azure
- **Portas**: Acesso HTTPS (porta 443) para comunicação com a API

### Verificação do Ambiente

Execute os seguintes comandos para verificar se o seu sistema está preparado:

```bash
# Verificar versão do Python
python3 --version

# Verificar se pip está disponível
pip3 --version

# Verificar conectividade
curl -s https://httpbin.org/ip
```

## 🛠 Instalação

### Método Recomendado: Script Automático

O método mais simples e seguro para instalar o ManAI:

```bash
# 1. Clonar o repositório
git clone https://github.com/ruscorreia/manai.git
cd manai

# 2. Navegar para o directório de instalação
cd install

# 3. Tornar o script executável
chmod +x install_v2.sh

# 4. Executar a instalação
./install_v2.sh

# 5. Reiniciar o terminal ou recarregar o perfil
source ~/.bashrc  # para bash
# ou
source ~/.zshrc   # para zsh
```

### Instalação Manual

Para utilizadores que preferem controlo total sobre o processo:

```bash
# 1. Instalar dependências
pip3 install --user requests

# 2. Clonar e configurar
git clone https://github.com/ruscorreia/manai.git
cd manai/install

# 3. Copiar para directório local
mkdir -p ~/.local/bin
cp manai.py ~/.local/bin/manai
chmod +x ~/.local/bin/manai

# 4. Adicionar ao PATH (se necessário)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Verificação da Instalação

Confirme que a instalação foi bem-sucedida:

```bash
# Verificar se o comando está disponível
which manai

# Testar conectividade
manai --test-connection

# Verificar versão
manai --version
```

## 🎮 Primeiros Passos

### 1. Registo de Utilizador

Antes de utilizar o ManAI, é necessário criar uma conta:

```bash
manai --register
```

O sistema irá solicitar:
- **Email**: O seu endereço de email (será o seu identificador)
- **Password**: Palavra-passe segura (mínimo 8 caracteres)
- **Nome**: Primeiro e último nome
- **Idioma**: Idioma preferido para as respostas

### 2. Primeiro Teste

Após o registo, teste o sistema com uma pergunta simples:

```bash
manai "como listar ficheiros ocultos?"
```

### 3. Explorar Funcionalidades

Experimente diferentes tipos de perguntas:

```bash
# Pergunta básica
manai "como copiar ficheiros?"

# Pergunta específica
manai "como encontrar ficheiros modificados nas últimas 24 horas?"

# Pergunta em inglês
manai "how to compress a folder with tar?"

# Pergunta de seguimento (mantém contexto)
manai "e como posso excluir determinados tipos de ficheiro?"
```

## 📚 Utilização Detalhada

### Comandos Básicos

#### Perguntas Simples
```bash
# Comandos fundamentais
manai "como criar um directório?"
manai "como ver o conteúdo de um ficheiro?"
manai "como alterar permissões de ficheiro?"

# Gestão de processos
manai "como ver processos em execução?"
manai "como terminar um processo?"
manai "como executar um comando em segundo plano?"
```

#### Consultas Avançadas
```bash
# Operações complexas
manai "como fazer backup incremental com rsync?"
manai "como configurar um cron job para executar às 2h da manhã?"
manai "como monitorizar utilização de disco em tempo real?"

# Resolução de problemas
manai "como resolver erro 'permission denied'?"
manai "como recuperar espaço em disco?"
manai "como diagnosticar problemas de rede?"
```

### Gestão de Sessões

#### Sessões Contínuas
O ManAI mantém automaticamente o contexto entre perguntas:

```bash
# Primeira pergunta
manai "como usar o comando grep?"

# Pergunta de seguimento (usa contexto anterior)
manai "e como posso usar expressões regulares com ele?"

# Mais detalhes
manai "podes dar um exemplo prático?"
```

#### Nova Sessão
Para começar uma conversa completamente nova:

```bash
manai --new-session "como instalar software no Ubuntu?"
```

### Suporte Multilingue

#### Exemplos em Diferentes Idiomas

**Português:**
```bash
manai "como comprimir uma pasta com tar?"
```

**Inglês:**
```bash
manai "how to find files larger than 100MB?"
```

**Espanhol:**
```bash
manai "¿cómo crear un usuario en Linux?"
```

**Francês:**
```bash
manai "comment changer le mot de passe d'un utilisateur?"
```

### Comandos de Gestão

#### Informações da Conta
```bash
# Ver estado da conta
manai --status

# Ver estatísticas de utilização
manai --stats

# Verificar acesso a funcionalidades
manai --check-feature "longTermMemory"
```

#### Gestão de Sessão
```bash
# Fazer login
manai --login

# Fazer logout
manai --logout

# Testar conectividade
manai --test-connection
```

## 🔧 Configuração Avançada

### Variáveis de Ambiente

O ManAI pode ser configurado através de variáveis de ambiente:

```bash
# URL personalizada da API
export MANAI_API_URL="https://sua-instancia.azurewebsites.net/api"

# Chave de função personalizada
export MANAI_FUNCTION_KEY="sua-chave-personalizada"

# Idioma padrão
export MANAI_DEFAULT_LANGUAGE="en"
```

### Ficheiros de Configuração

O ManAI armazena configurações em:
- **Configuração**: `~/.config/manai/config.json`
- **Sessão**: `~/.config/manai/session.json`

### Personalização

#### Aliases Úteis
Adicione ao seu `.bashrc` ou `.zshrc`:

```bash
# Aliases para uso frequente
alias m="manai"
alias mhelp="manai --help"
alias mstatus="manai --status"
alias mnew="manai --new-session"
```

## 🚨 Resolução de Problemas

### Problemas Comuns

#### Erro: "Não autenticado"
**Sintoma**: Mensagem "É necessário fazer login primeiro"
**Solução**:
```bash
manai --login
```

#### Erro: "Limite de consultas atingido"
**Sintoma**: Mensagem sobre limite diário
**Soluções**:
- Aguardar até ao dia seguinte
- Considerar upgrade para ManAI Pro
- Verificar estatísticas: `manai --stats`

#### Erro: "Erro de comunicação"
**Sintomas**: Timeouts ou falhas de conexão
**Diagnóstico**:
```bash
# Testar conectividade básica
ping google.com

# Testar conectividade específica do ManAI
manai --test-connection

# Verificar configuração
manai --status
```

**Soluções**:
1. Verificar ligação à internet
2. Confirmar que não há firewall a bloquear HTTPS
3. Tentar novamente após alguns minutos

#### Erro: "Resposta inválida do servidor"
**Causa**: Problema temporário nos serviços Azure
**Soluções**:
1. Aguardar alguns minutos e tentar novamente
2. Verificar estado dos serviços Azure
3. Contactar suporte se persistir

### Diagnóstico Avançado

#### Verificação Completa do Sistema
```bash
# Script de diagnóstico completo
echo "=== Diagnóstico ManAI ==="
echo "Versão Python: $(python3 --version)"
echo "Versão ManAI: $(manai --version)"
echo "Conectividade:"
manai --test-connection
echo "Estado da conta:"
manai --status
```

#### Logs e Debug
Para obter informações detalhadas de debug:
```bash
# Executar com verbose (se disponível)
python3 ~/.local/bin/manai --debug "sua pergunta"
```

## 🤝 Contribuição

### Como Contribuir

Agradecemos contribuições da comunidade! Existem várias formas de ajudar:

#### Reportar Problemas
1. Verificar se o problema já foi reportado
2. Criar issue detalhada no GitHub
3. Incluir informações do sistema e passos para reproduzir

#### Sugerir Melhorias
1. Abrir discussion no GitHub
2. Descrever a funcionalidade proposta
3. Explicar o benefício para os utilizadores

#### Contribuir com Código
1. Fork do repositório
2. Criar branch para a funcionalidade
3. Implementar alterações com testes
4. Submeter pull request

### Padrões de Desenvolvimento

#### Estilo de Código
- Seguir PEP 8 para Python
- Usar type hints quando possível
- Documentar funções e classes
- Manter compatibilidade com Python 3.6+

#### Testes
- Escrever testes para novas funcionalidades
- Garantir que todos os testes passam
- Manter cobertura de testes elevada

## 📊 Roadmap

### Versão 2.1 (Próxima)
- Cache local para respostas frequentes
- Suporte para configurações personalizadas
- Melhorias na interface de utilizador
- Optimizações de performance

### Versão 2.2
- Plugin system para extensões
- Integração com editores de código
- Suporte para scripts personalizados
- Analytics avançados

### Versão 3.0 (Futuro)
- Interface gráfica opcional
- Suporte para outros sistemas operativos
- IA local para funcionalidades básicas
- Integração com ferramentas DevOps

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Isto significa que pode:

- ✅ Usar comercialmente
- ✅ Modificar o código
- ✅ Distribuir
- ✅ Usar privadamente

**Condições:**
- Incluir a licença e copyright
- Não responsabilizar os autores

## 🙏 Agradecimentos

### Equipa de Desenvolvimento
- **Rosco Edutec**: Desenvolvimento principal e arquitectura
- **Comunidade**: Contribuições, testes e feedback

### Tecnologias Utilizadas
- **Python**: Linguagem de programação principal
- **Azure Functions**: Infraestrutura cloud
- **Azure AI Foundry**: Motor de inteligência artificial
- **Requests**: Biblioteca HTTP para Python

### Inspiração
O ManAI foi inspirado pela necessidade de tornar o Linux mais acessível a utilizadores de todos os níveis, combinando a potência dos comandos tradicionais com a intuitividade da linguagem natural.

## 📞 Suporte

### Canais de Suporte

**GitHub Issues**: Para reportar bugs e solicitar funcionalidades
- [Reportar Bug](https://github.com/ruscorreia/manai/issues/new?template=bug_report.md)
- [Solicitar Funcionalidade](https://github.com/ruscorreia/manai/issues/new?template=feature_request.md)

**Discussions**: Para perguntas gerais e discussões
- [GitHub Discussions](https://github.com/ruscorreia/manai/discussions)

**Email**: Para questões comerciais ou parcerias
- rusacorreia@hotmail.com

### FAQ

**P: O ManAI funciona offline?**
R: Não, o ManAI requer ligação à internet para comunicar com os serviços Azure AI.

**P: Existe limite de utilização?**
R: Sim, contas gratuitas têm limite diário. Contacte-nos para opções premium.

**P: Os meus dados são seguros?**
R: Sim, seguimos as melhores práticas de segurança e privacidade. As perguntas são processadas de forma segura e não são armazenadas permanentemente.

**P: Posso usar o ManAI em scripts?**
R: Sim, o ManAI pode ser integrado em scripts bash e outros automatismos.

---

<div align="center">

**Desenvolvido com ❤️ pela [Rosco Edutec](https://github.com/ruscorreia)**

[⬆️ Voltar ao topo](#manai---assistente-linux-inteligente)

</div>


