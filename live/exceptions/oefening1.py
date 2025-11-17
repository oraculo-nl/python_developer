def safe_div(a,b):
    try:
        return a/b

    except TypeError:
        return None
    except ValueError:
        return None
    except ZeroDivisionError:
        return None

print(safe_div(1,2))
print(safe_div(1,0))
print(safe_div(1,"2"))
print(safe_div(-1,2))
print(safe_div(0,2))

