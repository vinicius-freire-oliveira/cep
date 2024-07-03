import random

class GeradorCEP:
    # Dicionário que mapeia o primeiro dígito do CEP para as faixas de CEPs correspondentes e suas descrições.
    regioes = {
        "0": [
            ("01000000", "05999999", "SP capital e região metropolitana"),
            ("08000000", "08499999", "SP capital e região metropolitana"),
            ("06000000", "09999999", "SP Região Metropolitana de São Paulo")
        ],
        "1": [
            ("11000000", "11999999", "SP Litoral"),
            ("12000000", "19999999", "SP Interior")
        ],
        "2": [
            ("20000000", "23799999", "RJ Capital"),
            ("23800000", "26599999", "RJ Região Metropolitana do Rio de Janeiro"),
            ("26600000", "28999999", "RJ Interior"),
            ("29000000", "29099999", "Vitória"),
            ("29100000", "29199999", "ES Região Metropolitana de Vitória"),
            ("29200000", "29999999", "ES Interior")
        ],
        "3": [
            ("30000000", "31999999", "Belo Horizonte"),
            ("32000000", "34999999", "MG Região Metropolitana de Belo Horizonte"),
            ("35000000", "39999999", "MG Interior")
        ],
        "4": [
            ("40000000", "42599999", "Salvador"),
            ("42600000", "43999999", "BA Região Metropolitana de Salvador"),
            ("44000000", "48999999", "BA Interior"),
            ("49000000", "49099999", "Aracaju"),
            ("49100000", "49999999", "SE Interior")
        ],
        "5": [
            ("50000000", "52999999", "Recife"),
            ("53000000", "54999999", "PE Região Metropolitana do Recife"),
            ("55000000", "56999999", "PE Interior"),
            ("57000000", "57099999", "Maceió"),
            ("57100000", "57999999", "AL Interior"),
            ("58000000", "58099999", "João Pessoa"),
            ("58100000", "58999999", "PB Interior"),
            ("59000000", "59139999", "Natal"),
            ("59140000", "59999999", "RN Interior")
        ],
        "6": [
            ("60000000", "61599999", "Fortaleza"),
            ("61600000", "61999999", "CE Região Metropolitana de Fortaleza"),
            ("62000000", "63999999", "CE Interior"),
            ("64000000", "64099999", "Teresina"),
            ("64100000", "64999999", "PI Interior"),
            ("65000000", "65099999", "São Luís"),
            ("65100000", "65999999", "MA Interior"),
            ("66000000", "66999999", "Belém"),
            ("67000000", "67999999", "PA Região Metropolitana de Belém"),
            ("68000000", "68899999", "PA Interior"),
            ("68900000", "68914999", "Macapá"),
            ("68915000", "68999999", "AP Interior"),
            ("69000000", "69099999", "Manaus"),
            ("69100000", "69299999", "AM Interior"),
            ("69300000", "69339999", "Boa Vista"),
            ("69340000", "69399999", "RR Interior"),
            ("69900000", "69920999", "Rio Branco"),
            ("69921000", "69999999", "AC Interior")
        ],
        "7": [
            ("70000000", "70999999", "Brasília"),
            ("71000000", "72799999", "DF Cidades-Satélites"),
            ("73000000", "73699999", "DF Cidades-Satélites"),
            ("74000000", "74899999", "Goiânia"),
            ("74900000", "75199999", "GO Região Metropolitana de Goiânia"),
            ("72800000", "72999999", "GO Entorno de Brasília"),
            ("73700000", "73999999", "GO Interior"),
            ("75200000", "76799999", "GO Interior"),
            ("76800000", "76849999", "Porto Velho"),
            ("76850000", "76999999", "RO Interior"),
            ("77000000", "77299999", "Palmas"),
            ("77300000", "77999999", "TO Interior"),
            ("78000000", "78109999", "Cuiabá"),
            ("78110000", "78999999", "MT Interior"),
            ("79000000", "79129999", "Campo Grande"),
            ("79130000", "79999999", "MS Interior")
        ],
        "8": [
            ("80000000", "82999999", "Curitiba"),
            ("83000000", "83899999", "PR Região Metropolitana de Curitiba"),
            ("83900000", "87999999", "PR Interior"),
            ("88000000", "88099999", "Florianópolis"),
            ("88100000", "88179999", "SC Região Metropolitana de Florianópolis"),
            ("88180000", "89999999", "SC Interior")
        ],
        "9": [
            ("90000000", "91999999", "Porto Alegre"),
            ("92000000", "94999999", "RS Região Metropolitana de Porto Alegre"),
            ("95000000", "99999999", "RS Interior")
        ]
    }

    @staticmethod
    def listar_subregioes(primeiro_digito):
        """
        Retorna a lista de sub-regiões para um dado primeiro dígito.
        :param primeiro_digito: O primeiro dígito do CEP.
        :return: Lista de sub-regiões disponíveis.
        """
        subregioes = GeradorCEP.regioes.get(primeiro_digito)
        if not subregioes:
            return []
        return [sub[2] for sub in subregioes]

    @staticmethod
    def gerar_cep(primeiro_digito, subregiao):
        """
        Gera um CEP com base no primeiro dígito e na sub-região selecionada.
        :param primeiro_digito: O primeiro dígito do CEP.
        :param subregiao: A sub-região escolhida.
        :return: CEP gerado e a descrição da região.
        """
        regioes = GeradorCEP.regioes.get(primeiro_digito, [])
        subregiao_info = None

        # Busca a faixa de CEP correspondente à sub-região selecionada
        for sub in regioes:
            if sub[2] == subregiao:
                subregiao_info = sub
                break

        # Se não encontrar a sub-região, lança um erro
        if not subregiao_info:
            raise ValueError("Subregião inválida para o primeiro dígito fornecido.")

        cep_inicio, cep_fim, _ = subregiao_info

        # Gera um número de CEP dentro da faixa selecionada
        cep_num = random.randint(int(cep_inicio), int(cep_fim))
        cep = f"{str(cep_num)[:2]}.{str(cep_num)[2:5]}-{str(cep_num)[5:]}"

        return cep, subregiao

def simular_geracao_cep():
    """
    Função para simular a geração de um CEP com base na entrada do usuário.
    """
    try:
        # Solicita o primeiro dígito do CEP
        primeiro_digito = input("Digite o primeiro dígito do CEP (0 a 9): ")
        subregioes = GeradorCEP.listar_subregioes(primeiro_digito)
        
        # Se o primeiro dígito for inválido, exibe uma mensagem e encerra
        if not subregioes:
            print("Primeiro dígito inválido.")
            return

        # Lista as sub-regiões disponíveis
        print("Sub-regiões disponíveis:")
        for idx, sub in enumerate(subregioes, 1):
            print(f"{idx}. {sub}")

        # Solicita a escolha da sub-região
        subregiao_escolha = int(input("Escolha o número da sub-região desejada: "))
        
        # Se a escolha for inválida, exibe uma mensagem e encerra
        if subregiao_escolha < 1 or subregiao_escolha > len(subregioes):
            print("Escolha inválida.")
            return

        # Gera o CEP com base na escolha do usuário
        subregiao = subregioes[subregiao_escolha - 1]
        cep, regiao = GeradorCEP.gerar_cep(primeiro_digito, subregiao)
        print("CEP Gerado:", cep)
        print("Região:", regiao)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    simular_geracao_cep()
