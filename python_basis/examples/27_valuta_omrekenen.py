# Euro naar dollar met opgegeven koers
euro = float(input("Bedrag in euro: "))
koers = float(input("Wisselkoers EUR->USD (bijv. 1.08): "))
usd = euro * koers
print(f"€{euro:.2f} is ${usd:.2f} bij koers {koers}")
