from abc import ABC, abstractmethod

class PetInterface(ABC):
    @abstractmethod
    def hygiene(self):
        raise NotImplementedError
        
    @abstractmethod
    def force(self):
        raise NotImplementedError

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