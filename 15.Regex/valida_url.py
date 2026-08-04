import re

# Usar expresiones regulares para validar url

url = re.compile(r"^(https?://)?([da-z.-]+).([a-z.]{2,6})([/w .-]*)*/?$")

if url.search("http://pythondiario.com.pe"): # Comprobemos que esta url es válida
    print("URL Valida")
else:
    print("URL No Valida")
    