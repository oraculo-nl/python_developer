# Doel: duck typing - geen expliciete erfenis nodig als de interface overeenkomt.

class Logger:
    def log(self, msg):
        print("LOG:", msg)

class Printer:
    def log(self, msg):
        print("PRINT:", msg)

def verwerk(logger_like, tekst):
    logger_like.log(tekst)

verwerk(Logger(), "Hallo")
verwerk(Printer(), "Wereld")
