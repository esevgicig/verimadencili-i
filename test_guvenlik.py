import pytest
from sifre_kontrol import sifre_kontrol_et
def test_dogru_sifre():
    assert sifre_kontrol_et("GucluSifre1@")==True

def test_eksik_sifre():
    assert sifre_kontrol_et("zayıf")==False

def test_hatali_sifre():
    assert sifre_kontrol_et("12345678")==False
