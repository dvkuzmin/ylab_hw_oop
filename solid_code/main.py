from heroes import SuperHero, Superman, ChuckNorris
from places import Place, Kostroma, Tokyo
from news import NewsMaker, Newspaper, TVNews
from antagonistfinder import AntagonistFinder


def save_the_place(hero: SuperHero, place: Place, newsmaker: NewsMaker):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    newsmaker.create_news()


if __name__ == '__main__':
    finder = AntagonistFinder()
    superman = Superman(finder=finder)
    kostroma = Kostroma()
    newspaper = Newspaper(hero=superman, place=kostroma)
    save_the_place(hero=superman, place=kostroma, newsmaker=newspaper)

    print('-' * 20)

    chuck_norris = ChuckNorris(finder=finder)
    tokyo = Tokyo()
    tv_news = TVNews(hero=chuck_norris, place=tokyo)
    save_the_place(hero=chuck_norris, place=tokyo, newsmaker=tv_news)
