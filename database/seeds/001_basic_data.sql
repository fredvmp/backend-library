-- =========================
-- AUTHORS
-- =========================
INSERT INTO authors (name, birth_date, country, biography) VALUES
('George Orwell', '1903-06-25', 'United Kingdom', 'English novelist and essayist'),
('J.K. Rowling', '1965-07-31', 'United Kingdom', 'British author, best known for Harry Potter');

-- =========================
-- PUBLISHERS
-- =========================
INSERT INTO publishers (name, country) VALUES
('Penguin Books', 'United Kingdom'),
('Bloomsbury', 'United Kingdom');

-- =========================
-- BOOKS
-- =========================
INSERT INTO books (title, publication_year, author_id, publisher_id) VALUES
('1984', 1949, 1, 1),
('Animal Farm', 1945, 1, 1),
('Harry Potter and the Philosopher''s Stone', 1997, 2, 2);

-- =========================
-- USERS
-- =========================
INSERT INTO users (username, email, birth_date) VALUES
('alice', 'alice@example.com', '1998-05-12'),
('bob', 'bob@example.com', '1995-09-30');
