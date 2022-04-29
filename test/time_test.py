import tamagotchi
from tamagotchi.pet import Pet
from tamagotchi.time import Time

tamagotchi = Pet('teste')
tamagotchi_time = Time(tamagotchi)

def test_must_denigrate_power():
    '''
    Vai testar se  tamagotchi_time.denigrate_power()
    subitraiu  0.5 de energia do tamagotchi
    '''
    tamagotchi_time.denigrate_power()
    assert tamagotchi.power == 99.5

def test_must_denigrate_hungry():
    '''
    Vai testar se  tamagotchi_time.denigrate_hungry()
    subitraiu 1 da fome do tamagotchi
    '''
    tamagotchi_time.denigrate_hungry()
    assert tamagotchi.hungry == 99

def test_must_not_denigrate_power():
    '''
    Vai testar se tamagotchi_time.denigrate_power
    não vai subitraiu 0.5 da energia do tamagotchi
    se ela já estiver zerada.
    '''
    tamagotchi.power = 0
    
    tamagotchi_time.denigrate_power()
    assert tamagotchi.power == 0

def test_must_not_denigrate_hungry():
    '''
    Vai testar se tamagotchi_time.denigrate_hungry
    não vai subitrair 1 da fome do tamagotchi
    se ela já estiver zerada.
    '''
    tamagotchi.hungry = 0
    
    tamagotchi_time.denigrate_hungry()
    assert tamagotchi.hungry == 0

def test_must_denigrate_life_when_the_power_goes_out():
    '''
    Vai testar se tamagotchi_time.denigrate_attribut
    vai subitrair 10 da vida do tamagotchi se a energia
    já estiver zerada.
    '''
    tamagotchi.life = 100

    tamagotchi_time.denigrate_attribut()
    
    assert tamagotchi.life == 89

def test_must_denigrate_life_when_the_hungry_goes_out():
    '''
    Vai testar se tamagotchi_time.denigrate_hungry
    vai subitrair 1 da vida do tamagotchi se a fome
    já estiver zerada.
    '''
    tamagotchi.life = 100

    tamagotchi_time.denigrate_hungry()
    
    assert tamagotchi.life == 99