from testen import check_leeftijd

def test_testen():
    assert check_leeftijd(18) == "Je mag stemmen"
    assert check_leeftijd(12) == "Je bent een tiener"
    assert check_leeftijd(10) == "Je bent een kind"
    assert check_leeftijd(30) == "Je mag stemmen"