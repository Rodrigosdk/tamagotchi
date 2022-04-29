class Pet:
    __name = ''
    __age = 0
    __power = 100
    __life = 100
    __hungry = 100

    def __init__(self, name):
        self.__name = name
    
    @property
    def power(self):
        '''
        Retorna o valor da energia
        '''
        return self.__power
    
    @property
    def name(self):
        '''
        Retornar o nome do Tamagotchi
        '''
        return self.__name
    
    @property
    def age(self):
        '''
        Retornar a idade do Tamagotchi
        '''
        return self.__age
    
    @property
    def life(self):
        '''
        Retornar o valor da vida do Tamagotchi
        '''
        return self.__life
    
    @property
    def hungry(self):
        '''
        Retornar o valor da fome do Tamagotchi
        '''
        return self.__hungry

    @life.setter
    def life(self, life_value):
        '''
        Modificar o valor da vida do Tamagotchi
        '''
        self.__life = life_value
        return self.__life
    
    @hungry.setter
    def hungry(self, hungry_value):
        '''
        Modificar o valor da fome do Tamagotchi
        '''
        self.__hungry = hungry_value
        return self.__hungry

    @power.setter
    def power(self, power_value):
        '''
        Modificar o valor da energia do Tamagotchi
        '''
        self.__power = power_value
        return self.__power
    
    @age.setter
    def age(self, age_value):
        '''
        Modificar a idade do Tamagotchi
        '''
        self.__age = age_value
        return self.__age
    