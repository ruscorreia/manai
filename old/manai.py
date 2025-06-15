#!/usr/bin/env python3

import argparse
import json
import os
import sys
import requests
from typing import Optional

class ManaiClient:
    """Cliente para interagir com o agente manai através da Azure Function."""
    
    def __init__(self, azure_function_url: str, function_key: Optional[str] = None):
        """
        Inicializa o cliente manai.
        
        Args:
            azure_function_url: URL da Azure Function
            function_key: Chave da função (opcional se usar autenticação diferente)
        """
        self.azure_function_url = azure_function_url
        self.function_key = function_key
        self.session_file = os.path.expanduser("$HOME/.local/.manai_session")
        
    def _get_headers(self) -> dict:
        """Retorna os cabeçalhos HTTP necessários."""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "manai-cli/1.0"
        }
        
        if self.function_key:
            headers["x-functions-key"] = self.function_key
            
        return headers
    
    def _load_session(self) -> Optional[str]:
        """Carrega o ID da thread da sessão anterior."""
        try:
            if os.path.exists(self.session_file):
                with open(self.session_file, 'r') as f:
                    data = json.load(f)
                    return data.get('thread_id')
        except (json.JSONDecodeError, IOError):
            pass
        return None
    
    def _save_session(self, thread_id: str):
        """Guarda o ID da thread para a próxima sessão."""
        try:
            with open(self.session_file, 'w') as f:
                json.dump({'thread_id': thread_id}, f)
        except IOError:
            # Se não conseguir guardar, continua sem sessão
            pass
    
    def ask_question(self, question: str, use_session: bool = True) -> dict:
        """
        Envia uma pergunta para o agente manai.
        
        Args:
            question: A pergunta a fazer ao agente
            use_session: Se deve usar a sessão anterior para contexto
            
        Returns:
            Dicionário com a resposta do agente
        """
        # Preparar o payload
        payload = {"Question": question}
        
        # Carregar thread ID se usar sessão
        if use_session:
            thread_id = self._load_session()
            if thread_id:
                payload["ThreadId"] = thread_id
        
        try:
            # Fazer a requisição HTTP
            response = requests.post(
                self.azure_function_url,
                headers=self._get_headers(),
                json=payload,
                timeout=60  # Timeout de 60 segundos
            )
            
            # Verificar se a resposta foi bem-sucedida
            response.raise_for_status()
            
            # Processar a resposta JSON
            result = response.json()
            
            # Guardar o thread ID se fornecido
            if use_session and result.get('threadId'):
                self._save_session(result['threadId'])
            
            return result
            
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"Erro de comunicação: {str(e)}"
            }
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Resposta inválida do servidor"
            }

def get_config() -> tuple:
    """
    Obtém a configuração da Azure Function a partir de variáveis de ambiente.
    
    Returns:
        Tupla com (url, function_key)
    """
    # URL da Azure Function
    azure_function_url = "https://manai-agent-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger"
    
    # Chave da função (opcional)
    function_key = "58H0KD8feP9x2e6uqY1wkwW-6MqwrNkWI6U4-jdsSa5EAzFuACdqNA=="
    
    return azure_function_url, function_key

def print_help():
    """Imprime informações de ajuda sobre configuração."""
    print("\n" + "="*60)
    print("\n" + "="*60)

def main():
    parser = argparse.ArgumentParser(
        description="Manai - O seu assistente de páginas man com IA",
        epilog="Exemplos:\n"
               "  manai 'como listar ficheiros ocultos?'\n"
               "  manai 'criar um directório com permissões específicas'\n"
               "  manai --new-session 'como usar o comando find?'\n"
               "  manai --config",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "query",
        type=str,
        nargs='?',
        help="A sua pergunta em linguagem natural sobre comandos Linux"
    )
    
    parser.add_argument(
        "--new-session",
        action="store_true",
        help="Iniciar uma nova sessão (ignorar contexto anterior)"
    )
    
    parser.add_argument(
        "--config",
        action="store_true",
        help="Mostrar informações de configuração"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="manai 2.0.0 - Integração com Azure AI"
    )

    args = parser.parse_args()
    
    # Mostrar configuração se solicitado
    if args.config:
        print_help()
        return
    
    # Verificar se foi fornecida uma pergunta
    if not args.query:
        parser.print_help()
        print_help()
        return
    
    # Obter configuração
    azure_function_url, function_key = get_config()
    
    # Verificar se a URL está configurada
    if not azure_function_url or azure_function_url.startswith("https://sua-function-app"):
        print("❌ Erro: URL da Azure Function não configurada.")
        print("Execute 'manai --config' para ver as instruções de configuração.")
        sys.exit(1)
    
    # Criar cliente e fazer a pergunta
    client = ManaiClient(azure_function_url, function_key)
    
    print(f"🤖 Pergunta: {args.query}")
    print("⏳ A processar com IA...")
    
    # Fazer a pergunta (nova sessão se solicitado)
    result = client.ask_question(args.query, use_session=not args.new_session)
    
    # Mostrar resultado
    if result.get('success'):
        print("\n✅ Resposta do manai:")
        print("-" * 50)
        print(result.get('answer', 'Sem resposta'))
        
        # Mostrar informação da sessão se disponível
        if result.get('threadId') and not args.new_session:
            print(f"\n💬 Sessão: {result['threadId'][-8:]}... (use --new-session para reiniciar)")
    else:
        print(f"\n❌ Erro: {result.get('error', 'Erro desconhecido')}")
        
        # Sugestões de resolução de problemas
        if "comunicação" in result.get('error', '').lower():
            print("\n🔧 Sugestões:")
            print("- Verifique a sua ligação à internet")
            print("- Confirme se a URL da Azure Function está correcta")
            print("- Verifique se a chave da função está válida")
        
        sys.exit(1)

if __name__ == "__main__":
    main()
