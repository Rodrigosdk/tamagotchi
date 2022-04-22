class Pet:
    __name = ''
    __age = 0
    __power = 100
    __life = 100
    __hungry = 100

    def __init__(self, name):
        self.__name = name
    def get_power(self):
        return self.__power

    def get_name(self):
        '''
        Retornar o nome do Tamagotchi
        '''
        return self.__name

    def get_age(self):
        '''
        Retornar a idade do Tamagotchi
        '''
        return self.__age
    
    def get_life(self):
        '''
        Retornar o valor da vida do Tamagotchi
        '''
        return self.__life

    def get_hungry(self):
        '''
        Retornar o valor da fome do Tamagotchi
        '''
        return self.__hungry

    def set_life(self, life_value):
        '''
        Modificar o valor da vida do Tamagotchi
        '''
        self.__life = life_value
        return self.__life
        
    def set_hungry(self, hungry_value):
        '''
        Modificar o valor da fome do Tamagotchi
        '''
        self.__hungry = hungry_value
        return self.__hungry

    def set_power(self, power_value):
        '''
        Modificar o valor da energia do Tamagotchi
        '''
        self.__power = power_value
        return self.__power
    
    def set_age(self, age_value):
        '''
        Modificar a idade do Tamagotchi
        '''
        self.__age = age_value
        return self.__age
    