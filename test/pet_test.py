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
    Vai testar verifica se a idade está 
    conseguio ser alterada
    '''
    tamagotchi.age = 10

    value_age = tamagotchi.age

    assert value_age != 0

def test_must_return_life_100():
    value_life = tamagotchi.life
    
    assert value_life == 100

def test_must_not_return_life_100():
    tamagotchi.life = 10

    value_life = tamagotchi.life

    assert value_life != 100

def test_must_return_hungry_100():    
    value_hungry = tamagotchi.hungry
    
    assert value_hungry == 100

def test_must_not_return_hungry_100():
    tamagotchi.hungry = 10

    value_hungry = tamagotchi.hungry

    assert value_hungry != 100

def test_must_return_power_100():    
    value_power = tamagotchi.power
    
    assert value_power == 100

def test_must_not_return_power_100():
    tamagotchi.power = 10

    value_power = tamagotchi.power

    assert value_power != 0