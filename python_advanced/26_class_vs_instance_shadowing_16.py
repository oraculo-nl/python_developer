# Doel: overschrijven van class attribuut met instance attribuut (schaduwen).

class Config:
    versie = "1.0"  # class attribuut

c1 = Config()
c2 = Config()
c1.versie = "1.1"   # maakt een instance attribuut met dezelfde naam
print("c1:", c1.versie)      # 1.1 (instance attribuut)
print("c2:", c2.versie)      # 1.0 (class attribuut)
print("Class:", Config.versie) # 1.0
