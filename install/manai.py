#!/usr/bin/env python3

import argparse
import json
import os
import sys
import requests
import getpass
from typing import Optional, Dict, Any
from datetime import datetime

class ManaiFreemiumAzureClient:
    """Cliente para interagir com o ManAI Freemium através das Azure Functions em produção."""
    
    def __init__(self, base_url: str = "https://manai-agent-function-app.azurewebsites.net/api", 
                 function_key: str = "58H0KD8feP9x2e6uqY1wkwW-6MqwrNkWI6U4-jdsSa5EAzFuACdqNA=="):
        """
        Inicializa o cliente ManAI Freemium para Azure.
        
        Args:
            base_url: URL base das Azure Functions em produção
            function_key: Chave de acesso às Azure Functions
        """
        self.base_url = base_url.rstrip('/')
        self.function_key = function_key
        self.config_dir = os.path.expanduser("~/.config/manai")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.session_file = os.path.join(self.config_dir, "session.json")
        
        # Criar directório de configuração se não existir
        os.makedirs(self.config_dir, exist_ok=True)
        
        # Carregar configuração
        self.config = self._load_config()
        
    def _load_config(self) -> Dict[str, Any]:
        """Carrega a configuração do utilizador."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
        return {}
    
    def _save_config(self):
        """Guarda a configuração do utilizador."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except IOError as e:
            print(f"⚠️  Aviso: Não foi possível guardar configuração: {e}")
    
    def _load_session(self) -> Optional[Dict[str, Any]]:
        """Carrega informações da sessão anterior."""
        try:
            if os.path.exists(self.session_file):
                with open(self.session_file, 'r') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
        return None
    
    def _save_session(self, session_data: Dict[str, Any]):
        """Guarda informações da sessão."""
        print(f"🔒 Guardando sessão...{session_data}")
        try:
            with open(self.session_file, 'w') as f:
                json.dump(session_data, f, indent=2)
        except IOError as e:
            print(f"⚠️  Aviso: Não foi possível guardar sessão: {e}")
    
    def _get_headers(self, include_auth: bool = True, include_function_key: bool = True) -> Dict[str, str]:
        """Retorna os cabeçalhos HTTP necessários."""
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "manai-freemium-azure-cli/2.0"
        }
        
        # Adicionar chave da função Azure
        if include_function_key and self.function_key:
            headers["x-functions-key"] = self.function_key
        
        # Adicionar token JWT se disponível
        if include_auth and self.config.get('token'):
            headers["Authorization"] = f"Bearer {self.config['token']}"
            
        return headers
    
    def _make_request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None, 
                     include_auth: bool = True, include_function_key: bool = True) -> Dict[str, Any]:
        """Faz uma requisição HTTP para a API Azure."""
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers(include_auth, include_function_key)
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=120)  # Timeout maior para Azure
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=120)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data, timeout=120)
            else:
                return {"success": False, "error": f"Método HTTP não suportado: {method}"}
            
            # Verificar status codes específicos
            if response.status_code == 401:
                return {"success": False, "error": "Token inválido ou expirado. Execute 'manai login'"}
            elif response.status_code == 403:
                return {"success": False, "error": "Acesso negado. Verifique a chave da função Azure"}
            elif response.status_code == 404:
                return {"success": False, "error": f"Endpoint não encontrado: {endpoint}"}
            elif response.status_code == 429:
                return {"success": False, "error": "Limite de consultas atingido. Considere fazer upgrade para ManAI Pro"}
            elif response.status_code == 500:
                return {"success": False, "error": "Erro interno do servidor Azure. Tente novamente mais tarde"}
            
            response.raise_for_status()
            
            # Tentar fazer parse do JSON
            try:
                return response.json()
            except json.JSONDecodeError:
                # Se não for JSON válido, retornar texto como resposta
                return {"success": True, "message": response.text}
            
        except requests.exceptions.Timeout:
            return {"success": False, "error": "Timeout na comunicação com Azure. Tente novamente"}
        except requests.exceptions.ConnectionError:
            return {"success": False, "error": "Erro de conexão com Azure. Verifique sua internet"}
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Erro de comunicação: {str(e)}"}
    
    def register(self, email: str, password: str, first_name: str, last_name: str, 
                language: str = "pt") -> Dict[str, Any]:
        """Regista um novo utilizador."""
        data = {
            "Email": email,
            "Password": password,
            "FirstName": first_name,
            "FastName": last_name,
            "PreferredLanguage": language
        }
        
        result = self._make_request("RegisterUser", "POST", data, include_auth=False)
        
        if result.get("success"):
            # Guardar token e informações do utilizador
            self.config["token"] = result["token"]
            self.config["user"] = result["user"]
            self._save_config()
            
        return result
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Faz login do utilizador."""
        data = {
            "Email": email,
            "Password": password
        }
        
        result = self._make_request("LoginUser", "POST", data, include_auth=False)
        
        if result.get("success"):
            # Guardar token e informações do utilizador
            self.config["token"] = result["token"]
            self.config["user"] = result["user"]
            self._save_config()
            
        return result
    
    def logout(self):
        """Faz logout do utilizador."""
        self.config.pop("token", None)
        self.config.pop("user", None)
        self._save_config()
        
        # Limpar sessão
        if os.path.exists(self.session_file):
            os.remove(self.session_file)
    
    def get_profile(self) -> Dict[str, Any]:
        """Obtém o perfil do utilizador."""
        return self._make_request("GetUserProfile", "GET")
    
    def get_tier_config(self) -> Dict[str, Any]:
        """Obtém a configuração do tier actual."""
        return self._make_request("GetTierConfiguration", "GET")
    
    def check_usage_limits(self, language: str = "pt") -> Dict[str, Any]:
        """Verifica os limites de utilização."""
        data = {"Language": language}
        return self._make_request("CheckUsageLimit", "POST", data)
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas de utilização."""
        return self._make_request("GetUsageStatistics", "GET")
    
    def check_feature_access(self, feature_name: str) -> Dict[str, Any]:
        """Verifica acesso a uma funcionalidade específica."""
        data = {"featureName": feature_name}
        return self._make_request("CheckFeatureAccess", "POST", data)
    
    def ask_question(self, question: str, language: str = "pt", use_session: bool = True) -> Dict[str, Any]:
        """
        Envia uma pergunta para o agente ManAI.
        
        Args:
            question: A pergunta a fazer ao agente
            language: Idioma da resposta
            use_session: Se deve usar a sessão anterior para contexto
            
        Returns:
            Dicionário com a resposta do agente
        """
        # Verificar se está autenticado
        if not self.config.get('token'):
            return {"success": False, "error": "É necessário fazer login primeiro. Execute 'manai login'"}
        
        # Preparar o payload
        payload = {
            "Question": question,
            "Language": language
        }
        
        # Carregar thread ID se usar sessão
        if use_session:
            session = self._load_session()
            if session and session.get('ThreadId'):
                payload["ThreadId"] = session['ThreadId']
        
        # Tentar primeiro a função freemium (se disponível)
        result = self._make_request("ManaiAgentFreemiumHttpTrigger", "POST", payload)
        
        # Guardar informações da sessão se bem-sucedido
        if result.get('success') and use_session:
            thread_id = result.get('ThreadId') or result.get('threadId')
            session_id = result.get('SessionId') or result.get('sessionId')
            
            if thread_id:
                session_data = {
                    'ThreadId': thread_id,
                    'SessionId': session_id,
                    'lastUsed': datetime.now().isoformat()
                }
                self._save_session(session_data)
        
        return result
    
    def is_authenticated(self) -> bool:
        """Verifica se o utilizador está autenticado."""
        if not self.config.get('token'):
            return False
        
        # Tentar validar token (se função disponível)
        result = self._make_request("ValidateToken", "POST")
        if result.get('valid') is not None:
            return result.get('valid', False)
        
        # Se função de validação não disponível, assumir que token existe = autenticado
        return True
    
    def test_connection(self) -> Dict[str, Any]:
        """Testa a conexão com as Azure Functions."""
        try:
            # Testar função original primeiro
            result = self._make_request("ManaiAgentHttpTrigger", "GET", include_auth=False)
            
            if result.get('success') or "método não permitido" in result.get('error', '').lower():
                return {
                    "success": True, 
                    "message": "Conexão com Azure Functions estabelecida",
                    "functions_available": ["ManaiAgentHttpTrigger"]
                }
            else:
                return {
                    "success": False,
                    "error": f"Falha na conexão: {result.get('error')}"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao testar conexão: {str(e)}"
            }

def print_welcome():
    """Imprime mensagem de boas-vindas."""
    print("🤖 ManAI Freemium Azure - O seu assistente de comandos Linux com IA")
    print("🌐 Conectado às Azure Functions em produção")
    print("=" * 65)

def print_tier_info(client: ManaiFreemiumAzureClient):
    """Mostra informações sobre o tier actual."""
    if not client.is_authenticated():
        print("❌ Não autenticado. Execute 'manai login' primeiro.")
        return
    
    # Tentar obter informações do perfil freemium
    profile = client.get_profile()
    tier_config = client.get_tier_config()
    usage_stats = client.get_usage_stats()
    
    # Se funções freemium não disponíveis, mostrar informação básica
    if not profile.get('success', True) and "não encontrado" in profile.get('error', '').lower():
        print("ℹ️  Usando função Azure original (sem sistema freemium)")
        print(f"👤 Utilizador: {client.config.get('user', {}).get('email', 'N/A')}")
        print("🎯 Tier: ORIGINAL (sem limitações)")
        print("📊 Consultas: Ilimitadas")
        print("🌍 Idiomas: Todos suportados")
        return
    
    if not profile.get('success', True):
        print(f"❌ Erro ao obter perfil: {profile.get('error')}")
        return
    
    if not tier_config.get('success', True):
        print(f"❌ Erro ao obter configuração: {tier_config.get('error')}")
        return
    
    print(f"\n👤 Utilizador: {client.config.get('user', {}).get('email', 'N/A')}")
    print(f"🎯 Tier: {tier_config.get('tierType', 'N/A').upper()}")
    
    if tier_config.get('dailyQueryLimit', 0) > 0:
        today_usage = 0
        if usage_stats.get('success', True) and usage_stats.get('dailyStatistics'):
            # Data de hoje
            today_str = datetime.now().date()

            # Buscar estatísticas de hoje
            today_stats = next(
                (s for s in usage_stats['dailyStatistics']
                if datetime.fromisoformat(s['date']).date() == today_str),
                None
            )
            if today_stats:
                today_usage = today_stats['queriesCount']
        
        print(f"📊 Utilização hoje: {today_usage}/{tier_config['dailyQueryLimit']}")
    else:
        print("📊 Consultas: Ilimitadas")
    
    print(f"🌍 Idiomas: {', '.join(tier_config.get('supportedLanguages', []))}")
    
    features = tier_config.get('features', {})
    print(f"✨ Funcionalidades:")
    print(f"   • Memória longo prazo: {'✅' if features.get('longTermMemory') else '❌'}")
    print(f"   • Comandos personalizados: {'✅' if features.get('customCommands') else '❌'}")
    print(f"   • Integração IDEs: {'✅' if features.get('ideIntegration') else '❌'}")
    print(f"   • Analytics: {'✅' if features.get('analytics') else '❌'}")

def interactive_register(client: ManaiFreemiumAzureClient):
    """Processo interactivo de registo."""
    print("\n📝 Registo de novo utilizador")
    print("-" * 30)
    
    email = input("Email: ").strip()
    if not email:
        print("❌ Email é obrigatório")
        return False
    
    password = getpass.getpass("Password: ")
    if len(password) < 8:
        print("❌ Password deve ter pelo menos 8 caracteres")
        return False
    
    first_name = input("Primeiro nome: ").strip()
    last_name = input("Último nome: ").strip()
    
    print("\nIdiomas disponíveis: pt (português), en (inglês), es (espanhol)")
    language = input("Idioma preferido [pt]: ").strip() or "pt"
    
    print("\n⏳ A registar utilizador no Azure...")
    result = client.register(email, password, first_name, last_name, language)
    
    if result.get("success"):
        print("✅ Registo bem-sucedido!")
        print(f"🎯 Tier inicial: {result['user']['tierType'].upper()}")
        return True
    else:
        error_msg = result.get('error', '')
        if "não encontrado" in error_msg.lower():
            print("⚠️  Função de registo não disponível na versão actual do Azure")
            print("💡 Contacte o administrador para criar conta manualmente")
        else:
            print(f"❌ Erro no registo: {error_msg}")
        return False

def interactive_login(client: ManaiFreemiumAzureClient):
    """Processo interactivo de login."""
    print("\n🔐 Login")
    print("-" * 10)
    
    email = input("Email: ").strip()
    if not email:
        print("❌ Email é obrigatório")
        return False
    
    password = getpass.getpass("Password: ")
    
    print("\n⏳ A fazer login no Azure...")
    result = client.login(email, password)
    
    if result.get("success"):
        print("✅ Login bem-sucedido!")
        print(f"👤 Bem-vindo, {result['user']['firstName']}!")
        print(f"🎯 Tier: {result['user']['tierType'].upper()}")
        return True
    else:
        error_msg = result.get('error', '')
        print(f"❌ Erro no login: {error_msg}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="ManAI Freemium Azure - O seu assistente de comandos Linux com IA",
        epilog="Exemplos:\n"
               "  manai 'como listar ficheiros ocultos?'\n"
               "  manai 'criar um directório com permissões específicas'\n"
               "  manai --new-session 'como usar o comando find?'\n"
               "  manai --register\n"
               "  manai --login\n"
               "  manai --status\n"
               "  manai --test-connection",
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
        "--language", "-l",
        type=str,
        default="pt",
        choices=["pt", "en", "es", "fr", "de", "it", "ja", "zh", "ru", "ar"],
        help="Idioma da resposta (padrão: pt)"
    )
    
    parser.add_argument(
        "--register",
        action="store_true",
        help="Registar novo utilizador"
    )
    
    parser.add_argument(
        "--login",
        action="store_true",
        help="Fazer login"
    )
    
    parser.add_argument(
        "--logout",
        action="store_true",
        help="Fazer logout"
    )
    
    parser.add_argument(
        "--status",
        action="store_true",
        help="Mostrar estado actual e informações do tier"
    )
    
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Mostrar estatísticas de utilização"
    )
    
    parser.add_argument(
        "--check-feature",
        type=str,
        help="Verificar acesso a uma funcionalidade específica"
    )
    
    parser.add_argument(
        "--test-connection",
        action="store_true",
        help="Testar conexão com Azure Functions"
    )
    
    parser.add_argument(
        "--url",
        type=str,
        default="https://manai-agent-function-app.azurewebsites.net/api",
        help="URL base da API Azure (padrão: https://manai-agent-function-app.azurewebsites.net/api)"
    )
    
    parser.add_argument(
        "--function-key",
        type=str,
        default="58H0KD8feP9x2e6uqY1wkwW-6MqwrNkWI6U4-jdsSa5EAzFuACdqNA==",
        help="Chave de acesso às Azure Functions"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="manai-freemium-azure 2.0.0 - Modelo Freemium com Azure Functions"
    )

    args = parser.parse_args()
    
    # Criar cliente Azure
    client = ManaiFreemiumAzureClient(args.url, args.function_key)
    
    # Testar conexão se solicitado
    if args.test_connection:
        print("🔍 Testando conexão com Azure Functions...")
        result = client.test_connection()
        if result.get('success'):
            print(f"✅ {result.get('message')}")
            if result.get('functions_available'):
                print(f"📋 Funções disponíveis: {', '.join(result['functions_available'])}")
        else:
            print(f"❌ {result.get('error')}")
        return
    
    # Mostrar boas-vindas se nenhum comando específico
    if not any([args.register, args.login, args.logout, args.status, args.stats, args.check_feature, args.query]):
        print_welcome()
        parser.print_help()
        return
    
    # Processar comandos de gestão de conta
    if args.register:
        interactive_register(client)
        return
    
    if args.login:
        interactive_login(client)
        return
    
    if args.logout:
        client.logout()
        print("✅ Logout realizado com sucesso")
        return
    
    if args.status:
        print_tier_info(client)
        return
    
    if args.stats:
        if not client.is_authenticated():
            print("❌ É necessário fazer login primeiro")
            return
        
        stats = client.get_usage_stats()
        if stats.get('success', True):
            print(f"\n📊 Estatísticas de Utilização")
            print("-" * 30)
            print(f"Total de consultas: {stats.get('totalQueries', 0)}")
            print(f"Média por dia: {stats.get('averageQueriesPerDay', 0):.1f}")
            print(f"Tier actual: {stats.get('currentTier', 'N/A').upper()}")
            
            if stats.get('dailyStatistics'):
                print("\nÚltimos 7 dias:")
                for stat in stats['dailyStatistics'][:7]:
                    date = datetime.fromisoformat(stat['date']).strftime('%d/%m')
                    print(f"  {date}: {stat['queriesCount']} consultas")
        else:
            if "não encontrado" in stats.get('error', '').lower():
                print("ℹ️  Estatísticas não disponíveis na versão actual")
            else:
                print(f"❌ Erro ao obter estatísticas: {stats.get('error')}")
        return
    
    if args.check_feature:
        if not client.is_authenticated():
            print("❌ É necessário fazer login primeiro")
            return
        
        result = client.check_feature_access(args.check_feature)
        if result.get('success', True):
            feature = result.get('featureName', args.check_feature)
            has_access = result.get('hasAccess', False)
            required_tier = result.get('requiredTier', 'unknown')
            
            status = "✅ Disponível" if has_access else f"❌ Requer tier {required_tier.upper()}"
            print(f"Funcionalidade '{feature}': {status}")
        else:
            if "não encontrado" in result.get('error', '').lower():
                print("ℹ️  Verificação de funcionalidades não disponível na versão actual")
            else:
                print(f"❌ Erro: {result.get('error')}")
        return
    
    # Processar pergunta
    if args.query:
        
        if not client.is_authenticated():
            print("❌ Não autenticado. Execute 'manai login' primeiro.")
            return
        
        # Verificar limites se sistema freemium disponível
        limits = client.check_usage_limits(args.language)
        if limits.get('success') and not limits.get('canMakeQuery', True):
            print("❌ Limite de consultas diárias atingido!")
            print(f"📊 Utilização: {limits.get('currentUsage', 0)}/{limits.get('dailyLimit', 0)}")
            print("💡 Considere fazer upgrade para ManAI Pro para consultas ilimitadas")
            return
        
        print(f"🤖 Pergunta: {args.query}")
        print("⏳ A processar com IA no Azure...")
        
        # Fazer a pergunta
        result = client.ask_question(args.query, args.language, use_session=not args.new_session)
        
        # Mostrar resultado
        if result.get('success'):
            # Obter resposta (compatível com ambos os formatos)
            answer = result.get('answer') or result.get('Answer', 'Sem resposta')
            
            print("\n✅ Resposta do ManAI:")
            print("-" * 50)
            print(answer)
            
            # Mostrar informação da utilização se disponível
            usage_info = result.get('usageInfo', {})
            if usage_info and usage_info.get('queriesUsedToday') != 'N/A':
                used = usage_info.get('queriesUsedToday', 0)
                limit = usage_info.get('dailyLimit', 0)
                if limit > 0:
                    print(f"\n📊 Utilização: {used}/{limit}")
                    if used >= limit * 0.8:  # Aviso quando atingir 80%
                        print("⚠️  Está próximo do limite diário. Considere upgrade para ManAI Pro")
                else:
                    print(f"\n📊 Consultas hoje: {used} (ilimitadas)")
            
            # Mostrar informação da sessão
            thread_id = result.get('ThreadId') or result.get('ThreadId')
            if thread_id and not args.new_session:
                thread_short = thread_id[-8:] if len(thread_id) > 8 else thread_id
                print(f"💬 Sessão: {thread_short}... (use --new-session para reiniciar)")
        else:
            print(f"\n❌ Erro: {result.get('error', 'Erro desconhecido')}")
            
            # Sugestões baseadas no tipo de erro
            error_msg = result.get('error', '').lower()
            if "token" in error_msg or "autenticação" in error_msg:
                print("\n🔧 Solução: Execute 'manai --login' para autenticar")
            elif "limite" in error_msg:
                print("\n🔧 Solução: Aguarde até amanhã ou faça upgrade para ManAI Pro")
            elif "conexão" in error_msg or "timeout" in error_msg:
                print("\n🔧 Sugestões:")
                print("- Verifique a sua ligação à internet")
                print("- Confirme se as Azure Functions estão disponíveis")
                print(f"- Teste a conexão: manai --test-connection")
            elif "chave" in error_msg or "403" in error_msg:
                print("\n🔧 Solução: Verifique a chave de acesso às Azure Functions")
            
            sys.exit(1)

if __name__ == "__main__":
    main()
