from API import API
import base64
import requests

class CeogameAPI:

	def __init__(self, email, password=""):
		self.session = requests.Session()
		self.session.headers["Authorization"] = "Bearer YOUR_TOKEN"
		self.session.headers["Host"] = "api.ceogame.com.br"
		self.session.headers["User-Agent"] = "okhttp/3.12.6"
		self.session.headers["Content-Type"] = "text/plain; charset=utf-8"

		self.email = email

	def login(self, email, senha):
		data = {
			"email": self.email,
			"senha": senha
		}

		# To login you need a token which is weird, I'm not putting the token here yet
		# because I don't know what information it contains, tldr not showing for security reasons :)
		self.session.headers["Authorization"] = "Basic ANOTHER_TOKEN"
		response = self.session.post(API.LOGIN, json=data)
		if response.status_code == 200:
			self.session.headers["Authorization"] = "Bearer " + response.json().get("access_token", "")

		return response

	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_empresa_financeiro(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_FINANCEIRO, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_personagens(self):
		
		data =	{
			"email": self.email
		}

		response = self.session.post(API.GET_PERSONAGENS, json=data)
		if response.status_code == 200:
			return response.json()
		return {}


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def pagar_tipo_conta_empresa_assistente(self, id_empresa, rodada_vencto, contas_selecionadas):
		
		data =	{
			"email": self.email,
			"rodada_vencto":rodada_vencto,
			"contas_selecionadas":contas_selecionadas
		}

		return self.session.post(API.PAGAR_TIPO_CONTA_EMPRESA_ASSISTENTE.format(id_empresa), json=data).json()


	def get_ranking_personagem_info(self, id_personagem):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_RANKING_PERSONAGEM_INFO.format(id_personagem), json=data).json()


	def get_rankings_personagens(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_RANKINGS_PERSONAGENS, json=data).json()


	def get_empresa_contas_apagar_assistente(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR_ASSISTENTE, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_empresa_contas_apagar(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_empresa_ultimos_relatorios_venda(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_ULTIMOS_RELATORIOS_VENDA, json=data).json()


	def transferir_dinheiro_empresa(self):
		
		data =	{
			"email": self.email,
			"valor":123.0,
			"tipo_transferencia":"R"
		}

		return self.session.post(API.TRANSFERIR_DINHEIRO_EMPRESA, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_rankings_personagens(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_RANKINGS_PERSONAGENS, json=data).json()


	def get_email_relatorio_venda(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMAIL_RELATORIO_VENDA, json=data).json()


	def get_empresa_contas_apagar(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR, json=data).json()


	def get_empresa_contas_apagar_assistente(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR_ASSISTENTE, json=data).json()


	def get_personagem_propriedades(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_PROPRIEDADES, json=data).json()


	def get_empresa_financeiro(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_FINANCEIRO, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_personagem_alertas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_ALERTAS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_empresa_ultimas_atividades(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_ULTIMAS_ATIVIDADES, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_email_relatorio_venda(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMAIL_RELATORIO_VENDA, json=data).json()


	def get_personagem_emails(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_EMAILS, json=data).json()


	def get_empresa_contas_apagar(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR, json=data).json()


	def get_empresa_saque_programado(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_SAQUE_PROGRAMADO, json=data).json()


	def get_empresa_ultimas_atividades(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_ULTIMAS_ATIVIDADES, json=data).json()


	def get_personagem_emails(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_EMAILS, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_personagem_emails(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_EMAILS, json=data).json()


	def get_empresa_financeiro(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_FINANCEIRO, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_novidades(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_NOVIDADES, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def transferir_dinheiro_empresa(self):
		
		data =	{
			"email": self.email,
			"valor":456.0,
			"tipo_transferencia":"D"
		}

		return self.session.post(API.TRANSFERIR_DINHEIRO_EMPRESA, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_personagem_redes_empresas(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_REDES_EMPRESAS, json=data).json()


	def get_empresa_contas_apagar_assistente(self, id_empresa):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_CONTAS_APAGAR_ASSISTENTE.format(id_empresa), json=data).json()


	def get_empresa_ultimos_relatorios_venda(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_ULTIMOS_RELATORIOS_VENDA, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_empresa_financeiro(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_FINANCEIRO, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()


	def get_dados_personagem(self):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource": 1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM, json=data).json()


	def get_dados_personagem(self, id_personagem):
		
		data =	{
			"email": self.email,
			"is_compat_ironsource":1
		}

		return self.session.post(API.GET_DADOS_PERSONAGEM.format(id_personagem), json=data).json()


	def get_empresa_relatorio_venda(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_RELATORIO_VENDA, json=data).json()


	def get_empresa_financeiro(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_FINANCEIRO, json=data).json()


	def get_personagem_emails(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_PERSONAGEM_EMAILS, json=data).json()


	def get_empresa_modulos(self):
		
		data =	{
			"email": self.email
		}

		return self.session.post(API.GET_EMPRESA_MODULOS, json=data).json()

if __name__ == "__main__":
	import json

	ceogame = CeogameAPI("email@email.com")
	
	for personagem in ceogame.get_personagens()['personagens']:
		id_personagem = personagem['id_personagem']
		nome_sobrenome = personagem['nome'] + ' ' + personagem['sobrenome']

		dados = ceogame.get_dados_personagem(id_personagem)

		rodada = int(dados["rodada"])

		_rpi = ceogame.get_ranking_personagem_info(id_personagem)

		print(f"Nome: {nome_sobrenome}\nRodada: {rodada}\nID: {id_personagem}")

		for empresa in _rpi["empresas"]:
			id_empresa = empresa["id_empresa"]
			nome = empresa["nome_fantasia"]

			_cap = ceogame.get_empresa_contas_apagar_assistente(id_empresa)
			contas = _cap["contas_a_pagar"]

			print(f"\tEmpresa: {nome}\n\tID: {id_empresa}")

			# Conta mais recente
			for conta in contas:
				rodada_vencto = int(conta["rodada_vencto"])

				if rodada_vencto <= (rodada + 1):
					# Pagar conta
					conta_ids = list(map(lambda cnt: int(cnt["id_tipo_conta"]), conta["contas_a_pagar"]))
					
					resultado = ceogame.pagar_tipo_conta_empresa_assistente(id_empresa, rodada_vencto, conta_ids)
					
					if resultado["retorno"] == "ok":
						print(f"\tConta Paga, turnos: {resultado['turnos']}")
					else:
						print(f"\tOcorreu um problema:\n\t{resultado}")
					

				# Só a mais recente
				break
