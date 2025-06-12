# manai/core.py
import os
import json
import argparse
import requests
from pathlib import Path

class ManaiClient:
    def __init__(self):
        self.function_url = "https://manai-agent-function-app.azurewebsites.net/api/ManaiAgentHttpTrigger"
        self.function_key = "58H0KD8feP9x2e6uqY1wkwW-6MqwrNkWI6U4-jdsSa5EAzFuACdqNA=="
        self.session_file = Path.home() / ".manai_session"

        if not self.function_url:
            raise EnvironmentError(
                "A variável MANAI_AZURE_FUNCTION_URL não está configurada."
            )

    def _save_session_id(self, session_id):
        with open(self.session_file, "w") as f:
            f.write(session_id)

    def _load_session_id(self):
        if self.session_file.exists():
            with open(self.session_file) as f:
                return f.read().strip()
        return None

    def _clear_session(self):
        if self.session_file.exists():
            self.session_file.unlink()

    def query(self, question, new_session=False):
        headers = {"Content-Type": "application/json"}
        if self.function_key:
            headers["x-functions-key"] = self.function_key

        payload = {"Question": question}

        if not new_session:
            session_id = self._load_session_id()
            if session_id:
                payload["ThreadId"] = session_id

        try:
            response = requests.post(self.function_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            if "ThreadId" in data:
                self._save_session_id(data["ThreadId"])
            return data.get("response", "Sem resposta.")
        except requests.exceptions.RequestException as e:
            return f"Erro de comunicação: {str(e)}"
        except json.JSONDecodeError:
            return "Resposta inválida do servidor."

def main():
    parser = argparse.ArgumentParser(description="Assistente Linux com IA")
    parser.add_argument("query", nargs="*", help="Pergunta em linguagem natural")
    parser.add_argument("--new-session", action="store_true", help="Ignorar contexto anterior")
    parser.add_argument("--config", action="store_true", help="Mostrar configuração")
    parser.add_argument("--version", action="store_true", help="Mostrar versão")
    parser.add_argument("--help", action="store_true", help="Mostrar ajuda")

    args = parser.parse_args()

    client = ManaiClient()

    if args.version:
        print("Manai v2.0.0")
    elif args.config:
        print(f"MANAI_AZURE_FUNCTION_URL={client.function_url}")
        print(f"MANAI_FUNCTION_KEY={'*' * len(client.function_key) if client.function_key else 'não definida'}")
    elif args.help:
        parser.print_help()
    elif args.query:
        question = " ".join(args.query)
        result = client.query(question, new_session=args.new_session)
        print(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()