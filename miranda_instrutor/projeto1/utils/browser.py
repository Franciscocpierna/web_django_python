import os
import undetected_chromedriver as uc
from time import sleep
import logging

# Silencia logs internos do uc que podem poluir o terminal
logging.getLogger('uc').setLevel(logging.CRITICAL)

def make_chrome_browser(headless=False):
    """
    Configura o Chrome com undetected-chromedriver.
    Aplica correções específicas para o WinError 6 (Identificador Inválido).
    """
    options = uc.ChromeOptions()
    
    if headless or os.environ.get('SELENIUM_HEADLESS') == '1':
        options.add_argument('--headless')
    
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3') 

    try:
        # use_subprocess=True é essencial para evitar o fechamento inesperado
        driver = uc.Chrome(options=options, use_subprocess=True)
        return driver
    except Exception as e:
        print(f"Erro ao iniciar o navegador: {e}")
        return None

if __name__ == '__main__':
    browser = make_chrome_browser(headless=False)
    
    if browser:
        try:
            print("Acedendo ao site...")
            browser.get('https://www.google.com') 
            sleep(3) 
            
            print(f"Título da página: {browser.title}")
            print("Sucesso! Operação concluída.")
                
        except Exception as e:
            print(f"Ocorreu um erro durante a execução: {e}")
        finally:
             print("A fechar navegador com segurança...")
        #     
        # para teste navegador aberto mantido    
        #try:
        #        browser.quit = lambda: None
        #        print("Conexão com o script finalizada. Navegador preservado.")
        #except:
        #        pass
        #
        #
        try:
                # 1. Fechar todas as janelas primeiro
                browser.close()
                # 2. Encerrar o processo do driver
                browser.quit()
        except Exception:
                # Ignora erros de encerramento já conhecidos no Windows
                pass
            
            # SOLUÇÃO PARA O WINERROR 6:
            # Forçamos o atributo quit para uma função vazia.
            # Assim, quando o destrutor (__del__) tentar rodar o quit() novamente,
            # ele não fará nada e não gerará a exceção de Identificador Inválido.
        try:
                browser.quit = lambda: None
        except:
                pass

        print("Processo finalizado.")