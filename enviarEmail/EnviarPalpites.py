
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

import os 
import smtplib
from email.message import EmailMessage
from enviarEmail.MeuEmail.Gmail import GMAIL, SENHA
from datetime import datetime
from API.GerarPalpites import SolicitarPalpites,ReceberOsPalpites
from email.message import EmailMessage
import smtplib
from datetime import datetime
import os
import schedule
import time




def EmailPalpites():
    try:
        # 1. Gerar os palpites
        SolicitarPalpites()        
        ReceberOsPalpites()  
       
        # 2. Configurações do e-mail
        Email = GMAIL
        Senha = SENHA  
        
        msg = EmailMessage()
        data_hoje = datetime.now().strftime("%d/%m/%Y")
        
        msg['Subject'] = f"Palpites do dia {data_hoje}"
        msg['From'] = Email
        msg['To'] = "arturdiniz06@gmail.com"
        msg.set_content("Segue em anexo os palpites do dia.")

        # 3. Anexar arquivo de palpites
        pasta_Palpites = "Palpites"
        
        # Verifica se a pasta existe
        if not os.path.exists(pasta_Palpites):
            raise FileNotFoundError(f"Pasta '{pasta_Palpites}' não encontrada")
            
        # Lista arquivos de palpites (modifique o padrão conforme seus arquivos)
        arquivos_palpites = [
            f for f in os.listdir(pasta_Palpites) 
            if f.startswith("Palpites") and f.endswith(".txt")  # Ajuste este filtro
        ]
        
        if not arquivos_palpites:
            raise FileNotFoundError("Nenhum arquivo de palpites encontrado")
            
        # Pega o arquivo mais recente
        arquivo = max(
            [os.path.join(pasta_Palpites, f) for f in arquivos_palpites],
            key=os.path.getctime
        )
        
        with open(arquivo, "rb") as f:
            dados_anexo = f.read()
            nome_anexo = os.path.basename(arquivo)
            
        msg.add_attachment(
            dados_anexo,
            maintype="text",
            subtype="plain",
            filename=nome_anexo
        )

        # 4. Enviar e-mail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(Email, Senha)
            smtp.send_message(msg)
            
        print(f"✅ E-mail enviado com anexo: {nome_anexo}")

    except FileNotFoundError as e:
        print(f"❌ Erro ao encontrar arquivo: {e}")
    except smtplib.SMTPException as e:
        print(f"❌ Erro no envio do e-mail: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
    
EmailPalpites()