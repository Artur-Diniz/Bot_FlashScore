
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Sobe 2 níveis (API → pasta_base)

import os 
import smtplib
from email.message import EmailMessage
from Email.Gmail import AcessoGmail,AcessoSenha
from datetime import datetime
from API.EnviarBackLog import ReceberLogs
from email.message import EmailMessage
import smtplib
from datetime import datetime
import os

def EmailBackLog():
    try:
        #Verifica se o arquivo de log do dia já existe
        pasta_log = "LOG"
        data_hoje = datetime.now().strftime("%Y-%m-%d") 
        arquivo_log = os.path.join(pasta_log, f"erros_{data_hoje}.txt")
        
        if not os.path.exists(arquivo_log):
            ReceberLogs()  # Sua função que gera o arquivo LOG/erros_XXXX-XX-XX.txt
            print(f"✅ Novo arquivo de log criado: {arquivo_log}")
        else:            
            print(f"⚠️ Arquivo de log já existe: {arquivo_log}")
            print("⚠️ arquivo ja enviado ")
            return
        

        Email = AcessoGmail()  
        Senha = AcessoSenha()  
        
        msg = EmailMessage()
        data_hoje = datetime.now().strftime("%d/%m/%Y")
        
        msg['Subject'] = f"Erros do dia {data_hoje}"
        msg['From'] = Email
        msg['To'] = "arturdiniz06@gmail.com"
        msg.set_content("Segue em anexo o arquivo de logs do dia.")

        pasta_log = "LOG"
        arquivo_log = max(
            [os.path.join(pasta_log, f) for f in os.listdir(pasta_log) if f.startswith("erros_")],
            key=os.path.getctime
        )

        with open(arquivo_log, "rb") as f:
            dados_anexo = f.read()
            nome_anexo = os.path.basename(arquivo_log)
            
        msg.add_attachment(
            dados_anexo,
            maintype="text",
            subtype="plain",
            filename=nome_anexo
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(Email, Senha)
            smtp.send_message(msg)
            
        print(f"✅ E-mail enviado com anexo: {nome_anexo}")

    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

        
        
# EmailBackLog()