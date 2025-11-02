# Zoeken in dictionary met while-loop
landen = {"nl": "Nederland", "be": "België", "fr": "Frankrijk"}
while True:
    code = input("Landcode (of 'stop'): ").lower()
    if code == "stop":
        print("Klaar.")
        break
    if code in landen:
        print(f"{code.upper()} = {landen[code]}")
    else:
        print("Onbekende code.")
