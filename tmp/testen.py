

def check_leeftijd(leeftijd):


    if leeftijd >= 18:
        return ("Je mag stemmen")
    elif 10 < leeftijd < 18:
        return ("Je bent een tiener")
    else:
        return ("Je bent een kind")



if __name__ == "__main__":
    leeftijd = int(input("wat is je leeftijd? "))
    check_leeftijd(leeftijd)
