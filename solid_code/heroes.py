from __future__ import annotations
from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
from places import Place


class SuperHero(ABC):
    """Abstract class of superhero"""
    def __init__(self, name: str, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    @abstractmethod
    def attack(self):
        ...

    @abstractmethod
    def find(self, place: Place):
        ...

    def ultimate(self):
        ...


class LasersMixin:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class KickMixin:
    @staticmethod
    def roundhouse_kick():
        print('Bump')


class GunMixin:
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Superman(SuperHero, LasersMixin, KickMixin):
    def __init__(self, finder: AntagonistFinder):
        super(Superman, self).__init__('Clark Kent', True)
        self.finder = finder

    def find(self, place: Place):
        self.finder.find_antagonist(place)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, KickMixin, GunMixin):
    def __init__(self, finder: AntagonistFinder):
        super(ChuckNorris, self).__init__('Chuck Norris', False)
        self.finder = finder

    def find(self, place: Place):
        self.finder.find_antagonist(place)

    def attack(self):
        self.roundhouse_kick()
        self.fire_a_gun()
