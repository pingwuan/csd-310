


DROP DATABASE IF EXISTS whatabook;

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT SELECT, INSERT, UPDATE, DELETE ON whatabook.* TO 'whatabook_user'@'localhost';

CREATE DATABASE whatabook;

USE whatabook;


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale     VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name   VARCHAR(500) NOT NULL,
    author  VARCHAR(200)    NOT NULL,
    details VARCHAR(500),
    PRIMARY KEY (book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);
INSERT INTO store(locale)
    VALUES
        ('whatabook cetnral, totally not Lincoln, NE 68505');


INSERT INTO book (book_name, author, details) 
    VALUES
        ('Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 'First book in the Harry Potter series'),
        ('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 'Second book in the Harry Potter series'),
        ('Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 'Third book in the Harry Potter series'),
        ('Harry Potter and the Goblet of Fire', 'J.K. Rowling', 'Fourth book in the Harry Potter series'),
        ('Harry Potter and the Order of Phoenix', 'J.K. Rowling', 'Fifth book in the Harry Potter series'),
        ('Harry Potter and the Half-Blood Prince', 'J.K. Rowling', 'Sixth book in the Harry Potter series'),
        ('Harry Potter and the Deathly Hallows', 'J.K. Rowling', 'Seventh and final book in the Harry Potter series'),
        ('Percy Jackson and the Lightning Thief', 'Rick Riordan', 'First book in the Percy Jackson and the Olympians series'),
        ('Percy Jackson and the Sea of Monsters', 'Rick Riordan', 'Second book in the Percy Jackson and the Olympians series'),
        ('Percy Jackson and the Titan''s Curse', 'Rick Riordan', 'Third book in the Percy Jackson and the Olympians series'),
        ('Percy Jackson and the Battle of the Labyrinth', 'Rick Riordan', 'Fourth book in the Percy Jackson and the Olympians series'),
        ('Percy Jackson and the Last Olympian', 'Rick Riordan', 'Fifth and final book in the Percy Jackson and the Olympians series');
INSERT INTO user (first_name, last_name) 
    VALUES
        ('Alice', 'Johnson'), 
        ('Bob', 'Smith'), 
        ('Charlie', 'Brown'), 
        ('David', 'Lee'), 
        ('Emily', 'Davis'),
        ('John', 'Doe'),
        ('Jane', 'Doe');

