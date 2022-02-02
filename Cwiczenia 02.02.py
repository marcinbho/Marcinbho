# class KlasaBazowa:
#     pass
#
# class KlasaPochodna(KlasaBazowa):
#     pass

# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         KontoBankowe.__init__(self, nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             KontoBankowe.wyplac(self, ilosc)

account = KontoDebetowe("Jan Nowak", 0, 1000)
account.info()
account.wplac(500)
account.info()