from credit.models import Client, Account, Credit

client_1 = Client.objects.create(name="Бердиев Н.Д", citizenship="гражданин КР", birth_year="1994-05-06", work_place="работает в Codify")
client_1.clients.create(number="12345678910", account_type="10")
client_1.clients.create(number="12345678911", account_type="11")
client_1.accounts.create(sum=5000)
client_1.clients.all()
client_1.accounts.all()

client_2 = Client.objects.create(name="Усманов С.Ч", citizenship="гражданин КР", birth_year="1987-05-06", work_place="работает в HostKey")
client_2.clients.create(number="12345678910", account_type="10")
client_2.clients.create(number="12345678911", account_type="11")
client_2.accounts.create(sum=5000)
client_2.clients.all()
client_2.accounts.all()