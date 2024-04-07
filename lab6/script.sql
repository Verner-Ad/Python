CREATE TABLE PAINTING (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PIC_NAME TEXT,
    CRE_DATE TEXT,
    GENRE TEXT,
    MATERIAL TEXT,
    HEIGHT INTEGER,
    WIDTH INTEGER,
    AUTHOR_ID INTEGER,
    GALLERY_ID INTEGER,
    FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHOR (ID),
    FOREIGN KEY (GALLERY_ID) REFERENCES GALLERY (ID)
);

CREATE TABLE AUTHOR (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FIRST_NAME TEXT,
    SURNAME TEXT,
    SEX TEXT
);

CREATE TABLE GALLERY (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    GAL_NAME TEXT,
    FOUND_DATE TEXT,
    ADRESS_ID INTEGER,
    FOREIGN KEY (ADRESS_ID) REFERENCES ADRESS (ID)
);

CREATE TABLE ADRESS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COUNTRY TEXT,
    REGION TEXT,
    CITY TEXT,
    STREET TEXT,
    HOUSE_NUMBER INTEGER
);

INSERT INTO ADRESS (COUNTRY, REGION, CITY, STREET, HOUSE_NUMBER)
VALUES
    ("Россия", "Москвоская область", "Москва", "Лаврушинский переулок", 10),
    ("Россия", "Ленинградская область", "Санкт-Петербург", "улица Инженерная", 4),
    ("Россия", "Москвоская область", "Москва", "Улица Волхонка", 15),
    ("Беларусь", "Минская область", "Минск", "Улица Ленина", 20);
    
INSERT INTO GALLERY (GAL_NAME, FOUND_DATE, ADRESS_ID)
VALUES
    ("Третьяковская галерея", "1856", 1),
    ("Государственный Русский музей", "13-04-1895", 2),
    ("Храм Христа Спасителя", "31-12-1999", 3),
    ("Национальный художественный музей","5-11-1957", 4);

INSERT INTO AUTHOR (FIRST_NAME, SURNAME, SEX)
VALUES
    ("Врубель", "Врубель", "М"),
    ("Алексей", "Саврасов", "М"),
    ("Архип", "Куинджи", "М"),
    ("Иван", "Крамский", "М"),
    ("Андрей", "Рублев", "М"),
    ("Серебрякова", "Серебрякова", "Ж");

INSERT INTO PAINTING (PIC_NAME, CRE_DATE, GENRE, MATERIAL, HEIGHT, WIDTH, AUTHOR_ID, GALLERY_ID)
VALUES
    ("Демон сидящий", "1890", "Мифологическая сцена", "Холст, масло", 114, 211, 1, 1),
    ("Грачи прилетели", "1871", "Пейзаж", "Холст, масло", 62, 48, 2, 1),
    ("Царевна-Лебедь", "1900", "Мифологическая сцена", "Холст, масло", 142, 93, 1, 1),
    ("Лунная ночь на Днепре", "1880", "Пейзаж", "Холст, масло", 105, 146, 3, 2),
    ("Неизвестная", "1883", "Портрет", "Холст, масло", 75, 99, 4, 1),
    ("Троица", "1420", "Икона", "Дерево, темпера", 141, 114, 5, 3),
    ("За туалетом", "1909", "Автопортрет", "Холст на картоне, масло", 75, 65, 6, 1),
    ("Забытая деревня", "1874", "Пейзаж", "Холст, масло", 82, 165, 3, 1),
    ("Зимняя дорога", "1870", "Пейзаж", "Холст, масло", 41, 71, 2, 4);