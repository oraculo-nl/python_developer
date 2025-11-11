def titelcase(s):
    # simpele titelcase zonder externe libs
    return " ".join(w.capitalize() for w in s.split())
