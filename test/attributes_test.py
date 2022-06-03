from tamagotchi.attributes import Attributes
from tamagotchi.pet import Pet

tamagotchi = Pet('teste')
attributes = Attributes(tamagotchi)


def test_must_add_10_to_age():
    '''
    Vai testar se attributes.older adicionou 
    mais 10 anos a idade
    '''
    assert tamagotchi.age == 0
    
    attributes.older(10) 
    assert tamagotchi.age == 10

def test_must_not_some_age():
    '''
    Vai testar se attributes.older não 
    adicionou 10 anos a idade
    '''
    assert tamagotchi.age == 10
    attributes.older(0)
    assert tamagotchi.age == 10

def test_must_restore_power():
    '''
    Vai testar se attributes.sleep
    restaurou o valor so sono
    '''

    tamagotchi.power = 50
    attributes.sleep()
    assert tamagotchi.power == 100

def test_must_not_restore_power():
    '''
    Vai testar se attributes.sleep
    não restaurou o valor so sono
    '''

    tamagotchi.power = 50
    assert tamagotchi.power != 100

def test_must_restore_hungry():
    '''
    Vai testar se attributes.eat
    restaurou o valor da fome
    '''
    tamagotchi.hungry = 50
    attributes.eat()
    assert tamagotchi.hungry == 100

def test_must_not_restore_hungry():
    '''
    Vai testar se attributes.eat
    não restaurou o valor da fome
    '''
    tamagotchi.hungry = 50
    assert tamagotchi.hungry != 100

def test_must_return_status_from_tamagotchi():
    '''
    Vai testar se attributes.status
    retornou o status do tamagotchi
    '''
    tamagotchi = Pet('teste')
    attributes = Attributes(tamagotchi)
    expected = '''
    Nome: teste
    vida: 100
    Fome: 100
    Idade: 0
    Energia: 100
    '''
    
    assert attributes.status() == expected
