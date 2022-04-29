from tamagotchi.pet import Pet

tamagotchi = Pet('teste')

def test_must_return_age_0():
    '''
    verifica se a idade está zerada
    '''
    value_age = tamagotchi.age
    
    assert value_age == 0

def test_must_not_return_age_0():
    '''
    Vai testar  se a idade está 
    conseguio ser alterada
    '''
    tamagotchi.age = 10

    value_age = tamagotchi.age

    assert value_age != 0

def test_must_return_life_100():
    '''
    vai testa se tamagotchi.life retorna
    o valor da vida
    '''
    value_life = tamagotchi.life
    
    assert value_life == 100

def test_must_not_return_life_100():
    '''
    vai testa se tamagotchi.life consegue
    modificar o valor da vida
    '''
    tamagotchi.life = 10

    value_life = tamagotchi.life

    assert value_life != 100

def test_must_return_hungry_100():
    '''
    vai testa se tamagotchi.hungry retorna
    o valor da fome
    '''
    value_hungry = tamagotchi.hungry
    
    assert value_hungry == 100

def test_must_not_return_hungry_100():
    '''
    vai testa se tamagotchi.hungry consegue 
    retorna modificar o valor da fome
    '''
    tamagotchi.hungry = 10

    value_hungry = tamagotchi.hungry

    assert value_hungry != 100

def test_must_return_power_100():
    '''
    vai testa se tamagotchi.power retorna
    o valor da energia 
    '''
    value_power = tamagotchi.power
    
    assert value_power == 100

def test_must_not_return_power_100():
    '''
    vai testa se tamagotchi.power modficar 
    o valor da energia 
    '''

    tamagotchi.power = 10

    value_power = tamagotchi.power

    assert value_power != 0