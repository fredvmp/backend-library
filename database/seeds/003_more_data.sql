-- =========================
-- AUTORES NUEVOS
-- =========================
INSERT INTO authors (name, birth_date, country, biography) VALUES
('Haruki Murakami', '1949-01-12', 'Japan', 'Contemporary Japanese writer known for surreal narratives'),
('Patrick Rothfuss', '1973-06-06', 'USA', 'Fantasy writer, author of The Kingkiller Chronicle'),
('Osamu Dazai', '1909-06-19', 'Japan', 'Japanese novelist, known for deeply personal works'),
('Frank Herbert', '1920-10-08', 'USA', 'Science fiction writer, best known for Dune'),
('Oscar Wilde', '1854-10-16', 'Ireland', 'Poet and playwright, famous for wit and social criticism');

-- =========================
-- EDITORIALES NUEVAS
-- =========================
INSERT INTO publishers (name, country) VALUES
('Vintage', 'United Kingdom'),
('Penguin Random House', 'USA'),
('HarperCollins', 'USA'),
('Minotauro', 'Spain');

-- =========================
-- GÉNEROS NUEVOS (si no existen)
-- =========================
INSERT INTO genres (name)
VALUES
('Fantasy'),
('Science Fiction'),
('Classic'),
('Literary Fiction'),
('Adventure'),
('Magical Realism')
ON CONFLICT (name) DO NOTHING;

-- =========================
-- LIBROS (IDs RESUELTOS DINÁMICAMENTE)
-- =========================
INSERT INTO books (title, publication_year, author_id, publisher_id)
VALUES
(
  'Kafka on the Shore',
  2002,
  (SELECT id FROM authors WHERE name = 'Haruki Murakami'),
  (SELECT id FROM publishers WHERE name = 'Vintage')
),
(
  'The Name of the Wind',
  2007,
  (SELECT id FROM authors WHERE name = 'Patrick Rothfuss'),
  (SELECT id FROM publishers WHERE name = 'Penguin Random House')
),
(
  'No Longer Human',
  1948,
  (SELECT id FROM authors WHERE name = 'Osamu Dazai'),
  (SELECT id FROM publishers WHERE name = 'HarperCollins')
),
(
  'Dune',
  1965,
  (SELECT id FROM authors WHERE name = 'Frank Herbert'),
  (SELECT id FROM publishers WHERE name = 'Minotauro')
),
(
  'The Picture of Dorian Gray',
  1890,
  (SELECT id FROM authors WHERE name = 'Oscar Wilde'),
  (SELECT id FROM publishers WHERE name = 'Vintage')
);

-- =========================
-- RELACIÓN LIBROS - GÉNEROS
-- =========================
INSERT INTO book_genres (book_id, genre_id)
VALUES
(
  (SELECT id FROM books WHERE title = 'Kafka on the Shore'),
  (SELECT id FROM genres WHERE name = 'Magical Realism')
),
(
  (SELECT id FROM books WHERE title = 'Dune'),
  (SELECT id FROM genres WHERE name = 'Science Fiction')
),
(
  (SELECT id FROM books WHERE title = 'The Name of the Wind'),
  (SELECT id FROM genres WHERE name = 'Fantasy')
);
