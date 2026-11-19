from pyngrok import ngrok

# يفتح رابط للعالم كله على بورت 5000
public_url = ngrok.connect(5000)
print("="*50)
print("ارسلي هذا الرابط لصديقتك:")
print(public_url)
print("="*50)
print("لا تسكرين هالتيرمنال! اذا سكرتيه الرابط بيطفي")

# يخليه شغال
import time
while True:
    time.sleep(10)