from abc import ABC, abstractmethod

from heroes import SuperHero
from places import Place


class NewsMaker(ABC):
    """Abstract class for making news"""
    def __init__(self, hero: SuperHero, place: Place):
        self.hero = hero
        self.place = place

    @abstractmethod
    def create_news(self):
        ...


class Newspaper(NewsMaker):
    def create_news(self):
        print(f"{self.hero.name} saved the {self.place.name}")


class TVNews(NewsMaker):
    def create_news(self):
        print(f"Fox News: today {self.hero.name} saved the {self.place.name}")
