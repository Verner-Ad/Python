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
    ("Russia", "Moscow region", "Moscow", "Lavrushinsky Lane", 10),
    ("Russia", "Leningrad region", "St. Peterburg", "Inzhenernaya street", 4),
    ("Russia", "Moscow region", "Moscow", "Volkhonka Street", 15),
    ("Belarus", "Minsk region", "Minsk", "Lenin Street", 20);
    
INSERT INTO GALLERY (GAL_NAME, FOUND_DATE, ADRESS_ID)
VALUES
    ("Tretyakov Gallery", "1856", 1),
    ("State Russian Museum", "13-04-1895", 2),
    ("Cathedral of Christ the Savior", "31-12-1999", 3),
    ("National Museum of Art","5-11-1957", 4);

INSERT INTO AUTHOR (FIRST_NAME, SURNAME, SEX)
VALUES
    ("Vrubel", "Vrubel", "M"),
    ("Alexey", "Savrasov", "M"),
    ("Arkhip", "Kuindzhi", "M"),
    ("Ivan", "Kramsky", "M"),
    ("Andrey", "Rublev", "M"),
    ("Serebryakova", "Serebryakova", "F");

INSERT INTO PAINTING (PIC_NAME, CRE_DATE, GENRE, MATERIAL, HEIGHT, WIDTH, AUTHOR_ID, GALLERY_ID)
VALUES
    ("Demon Seated", "1890", "Mythological Scene", "Oil on Canvas", 114, 211, 1, 1),
    ("The Rooks Have Arrived", "1871", "Landscape", "Oil on Canvas", 62, 48, 2, 1),
    ("The Swan Princess", "1900", "Mythological scene", "Oil on canvas", 142, 93, 1, 1),
    ("Moonlit Night on the Dnieper", "1880", "Landscape", "Oil on Canvas", 105, 146, 3, 2),
    ("Unknown", "1883", "Portrait", "Oil on canvas", 75, 99, 4, 1),
    ("Trinity", "1420", "Icon", "Wood, tempera", 141, 114, 5, 3),
    ("Behind the toilet", "1909", "Self-portrait", "Oil on canvas on cardboard", 75, 65, 6, 1),
    ("Forgotten Village", "1874", "Landscape", "Oil on Canvas", 82, 165, 3, 1),
    ("Winter Road", "1870", "Landscape", "Oil on canvas", 41, 71, 2, 4)