-- =========================
-- AUTORES
-- =========================
INSERT INTO authors (name, birth_date, country)
VALUES
('Carlos Ruiz Zafón', '1964-09-25', 'España'),
('Isabel Allende', '1942-08-02', 'Chile');

-- =========================
-- EDITORIALES
-- =========================
INSERT INTO publishers (name, country)
VALUES
('Planeta', 'España'),
('Debolsillo', 'España');

-- =========================
-- GÉNEROS
-- =========================
INSERT INTO genres (name)
VALUES
('Ficción'),
('Misterio'),
('Novela histórica');

-- =========================
-- LIBROS
-- =========================
INSERT INTO books (title, publication_year, author_id, publisher_id)
VALUES
('La sombra del viento', 2001, 1, 1),
('El juego del ángel', 2008, 1, 1);

-- =========================
-- EDICIONES DE LIBROS
-- =========================
INSERT INTO book_editions (isbn, pages, format, publication_date, book_id)
VALUES
('9788432223451', 320, 'PHYSICAL',  '2018-03-10', 1),
('9788432223452', 320, 'DIGITAL',   '2019-01-05', 1),
('9788432223453', 320, 'AUDIOBOOK', '2020-06-20', 1),

('9788498389001', 410, 'PHYSICAL',  '2015-09-15', 2),
('9788498389002', 410, 'DIGITAL',   '2017-02-01', 2);

-- =========================
-- RELACIÓN LIBROS - GÉNEROS
-- =========================
INSERT INTO book_genres (book_id, genre_id)
VALUES
(1, 1), -- Ficción
(1, 2), -- Misterio
(2, 2), -- Misterio
(2, 3); -- Novela histórica
