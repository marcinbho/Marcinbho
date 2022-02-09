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
#

# account = KontoDebetowe("Jan Nowak", 0, 1000)
# account.info()
# account.wplac(500)
# account.info()
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             super().wyplac(ilosc)
#             account = KontoDebetowe("Jan Nowak", 0, 1000)
#             account.info()
#             account.wplac(500)
#             account.wyplac(1000)
#
# class A:
#     """Rodzic pierwszy"""
#
#     def __init__(self):
#         super().__init__()
#         self.a = "A"
#
#     def fa(self):
#         print("a:", self.a)
#
#
# class B:
#     """Rodzic drugi"""
#
#     def __init__(self):
#         super().__init__()
#         self.b = "B"
#
#     def fb(self):
#         print("b:", self.b)
#
#
# class Pochodna(B, A):
#     """Dziecko"""
#
#     def __init__(self):
#         super().__init__()
#         print(A.__doc__)
#         print(B.__doc__)
#         print(Pochodna.__doc__)
# import math
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError

    #     # print(math.pi)
    # class kolo(Figura):
    #     def __init__(self, r):
    #         self.r = r
    #         def obwod(self):
    #         return self.r*2 * math.pi
    #
    #         def pole(self):
    #         return self.r ** 2 * math.pi
    # k=kolo ( 5 )
    # print(k.pole())






# class trujkat(Figura):
#     def __init__(self, a):
#         self.a = a
#     def obwod(self):
#         return self.a * 3
#
#     def pole(self):
#         return self.a ** 2 * 3 ** (1/2)/4
# f2 = trujkat (5)
# print(a.obwod())
# print(a.pole())


# class prostokat(Figura):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return 2 * (self.a + self.b)
#
#     def pole(self):
#         return self.a * self.b
# f3 = prostokat(2.4)
# print(f3 . pole)
# print(f3 . obwod)

#Kwadrat

# class kwadrat(Figura):
#     def __init__(self,a):
#         self.a = a
#
#     def obwod(self):
#         return 4 * self.a
#
#     def pole(self):
#         return self.a ** 2
# f3 = kwadrat(4)
# print(f3 . pole)
# print(f3 . obwod)