# Рефакторинг кода с использованием принципов SOLID

Добавлен абстрактный класс PLace с абстрактным методом get_antagonist.
Добавлен абстрактный класс SuperHero с абстрактными методами attack и find. Метод ultimate 
будет переопределяться только для героев со сверхспособностями. Добавлены 
классы-миксины для разных возможностей аттак. При создании класса супергоероя
внедрена инъекция класса AntagonistFinder для низкой связанности и отсутствия хардкодинга 
в виде создания этого объекта прямо внутри класса. На основе созданного абстрактного класса
NewsMaker созданы различные классы, оповещающие о новостях через различные источники,
исправлена проблема single responsibility.
