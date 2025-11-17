# 02_lambda_basics.py
# Onderwerp: Lambda's (anonieme functies)

verdubbel = lambda x: x * 2
som = lambda a, b: a + b

if __name__ == "__main__":
    print("verdubbel(5) ->", verdubbel(5))
    print("som(3, 4) ->", som(3, 4))
