import sys
from pathlib import Path
import os 
import smtplib
import time
from email.message import EmailMessage
from datetime import datetime
from enviarEmail.MeuEmail.Gmail import GMAIL, SENHA
from API.EnviarBackLog import ReceberLogs

def limpar_logs_antigos(pasta_log, dias=29):
    agora = time.time()
    for arquivo in os.listdir(pasta_log):
        caminho = os.path.join(pasta_log, arquivo)
        if os.path.isfile(caminho):
            criado_em = os.path.getctime(caminho)
            if (agora - criado_em) > (dias * 86400):
                os.remove(caminho)
                print(f"🗑️ Arquivo antigo removido: {arquivo}")

def EmailBackLog():
    try:
        pasta_log = "LOG"
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        arquivo_log = os.path.join(pasta_log, f"erros_{data_hoje}.txt")
        
        if not os.path.exists(arquivo_log):
            ReceberLogs()
            print(f"✅ Novo arquivo de log criado: {arquivo_log}")
        else:            
            print(f"⚠️ Arquivo já existe: {arquivo_log}")
            return
        
        msg = EmailMessage()
        msg['Subject'] = f"Erros do dia {datetime.now().strftime('%d/%m/%Y')}"
        msg['From'] = GMAIL
        msg['To'] = "arturdiniz06@gmail.com"
        msg.set_content("Segue em anexo o arquivo de logs do dia.")

        with open(arquivo_log, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="plain",
                filename=f"erros_{data_hoje}.txt"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL, SENHA)
            smtp.send_message(msg)
        
        print("✅ E-mail enviado com sucesso!")
        limpar_logs_antigos(pasta_log)

    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    EmailBackLog()