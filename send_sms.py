from twilio.rest import Client

client = Client("AC60eff66308de9fd57e9aa831709166dc", "d7949e2dc9e684d0b6fa1efcdb79894a")
message = client.messages.create(
    to="+919056253201", 
    from_="+19205261323",
    body="iam working kkiikikm0kom")
print(message.status)

