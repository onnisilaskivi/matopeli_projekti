#Käytetään Pytestiä yksikkötestauksiin
#Testit ajetaan komennolla pytest
from main import *

#Mato setup
def mato():
        return Mato()
#Kalja setup
def kalja():
        return Kalja()

#Varmistetaan että pisteet pelin jälkeen nollaantuvat
def test_game_over():
        assert pisteet == 0

#Miniminopeus madolle 200 ja maksiminopeus 50, jotta peli pelattava.
def test_minimi_maksimi_nopeus():
        assert NOPEUS >= 50 and NOPEUS <= 200

#Varmistetaan, että kalja pysyy pelikentällä
def test_onko_kalja_pelikentällä():
        assert x >= 0 and x <= PELI_LEVEYS
        assert y >= 0 and y <= PELI_KORKEUS

#Varmistetaan, että madon pituus (mato_ovaalit lista) on yli 2
def test_testi():
        assert len(mato_ovaalit_testi) >= 2

#Varmistetaan, että pelaajan asettama uusi_suunta(nuolen painallus) päivittyy pelin suunnaksi
def test_vaihda_suunta():
        assert uusi_suunta_test == suunta