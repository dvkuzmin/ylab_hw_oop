from abc import ABC, abstractmethod


class Place(ABC):
    """Abstract class of the place, where antagonist can be"""
    name: str

    @abstractmethod
    def get_antagonist(self):
        ...


class Kostroma(Place):
    name = 'Kostroma city'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo city'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Crypton(Place):
    name = 'Planet Crypton'
    coordinates = [446416.12663, 5344524.45654]

    def get_antagonist(self):
        print("Doomsday is on the darkside of the planet")
