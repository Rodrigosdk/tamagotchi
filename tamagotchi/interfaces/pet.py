from abc import ABC, abstractmethod

class PetInterface(ABC):
    @abstractmethod
    def power(self) -> float:
        raise NotImplementedError
    
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def age(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def life(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def hungry(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def life(self, life_value)-> float:
        raise NotImplementedError
    
    @abstractmethod
    def hungry(self, hungry_value)-> float:
        raise NotImplementedError

    @abstractmethod
    def power(self, power_value)-> float:
        raise NotImplementedError
    
    @abstractmethod
    def age(self, age_value)-> int:
        raise NotImplementedError
    