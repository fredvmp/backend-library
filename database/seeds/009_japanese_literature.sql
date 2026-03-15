-- 1. Añadimos a Natsume Soseki si no está
INSERT INTO authors (name, birth_date, country, biography)
SELECT 'Natsume Soseki', '1867-02-09', 'Japan', 'The foremost Japanese novelist of the Meiji era.'
WHERE NOT EXISTS (SELECT 1 FROM authors WHERE name = 'Natsume Soseki');

-- 2. Añadimos los libros faltantes
INSERT INTO books (title, publication_year, author_id, publisher_id) VALUES
('South of the Border, West of the Sun', 1992, (SELECT id FROM authors WHERE name = 'Haruki Murakami'), (SELECT id FROM publishers WHERE name = 'Vintage')),
('Norwegian Wood', 1987, (SELECT id FROM authors WHERE name = 'Haruki Murakami'), (SELECT id FROM publishers WHERE name = 'Vintage')),
('Kokoro', 1914, (SELECT id FROM authors WHERE name = 'Natsume Soseki'), (SELECT id FROM publishers WHERE name = 'Vintage')),
('The Miner', 1908, (SELECT id FROM authors WHERE name = 'Natsume Soseki'), (SELECT id FROM publishers WHERE name = 'Vintage'))
ON CONFLICT DO NOTHING; -- Por si acaso ejecutas el script dos veces

-- 3. Ediciones (Datos cruciales para tus análisis de páginas)
INSERT INTO book_editions (isbn, pages, format, publication_date, book_id) VALUES
('9780679767398', 192, 'PHYSICAL', '1999-01-01', (SELECT id FROM books WHERE title = 'South of the Border, West of the Sun')),
('9780099448822', 400, 'PHYSICAL', '2000-06-01', (SELECT id FROM books WHERE title = 'Norwegian Wood')),
('9781846556203', 248, 'PHYSICAL', '2010-01-01', (SELECT id FROM books WHERE title = 'Kokoro')),
('9781411438965', 256, 'DIGITAL',  '2015-05-12', (SELECT id FROM books WHERE title = 'The Miner')),
('9780099458326', 505, 'PHYSICAL', '2005-01-01', (SELECT id FROM books WHERE title = 'Kafka on the Shore'))
ON CONFLICT (isbn) DO NOTHING;

-- 4. Géneros (Usando tus nombres limpios)
INSERT INTO book_genres (book_id, genre_id)
SELECT b.id, g.id FROM books b, genres g 
WHERE b.title IN ('Kokoro', 'The Miner', 'Norwegian Wood', 'South of the Border, West of the Sun') 
AND g.name = 'Fiction'
ON CONFLICT DO NOTHING;


-- =============================================
-- HISTORIAL DE LECTURA
-- =============================================
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
-- David lee a Soseki (Rápido)
('READING',  '2024-03-01 08:00:00', (SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = 'Kokoro')),
('FINISHED', '2024-03-03 20:00:00', (SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = 'Kokoro')),
-- Laura lee Murakami (Ritmo medio)
('READING',  '2024-02-10 10:00:00', (SELECT id FROM users WHERE username = 'laura'), (SELECT id FROM books WHERE title = 'Norwegian Wood')),
('FINISHED', '2024-02-20 18:30:00', (SELECT id FROM users WHERE username = 'laura'), (SELECT id FROM books WHERE title = 'Norwegian Wood')),
-- Valeria lee varios (Efecto volumen)
('READING',  '2024-01-05 09:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'South of the Border, West of the Sun')),
('FINISHED', '2024-01-12 21:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'South of the Border, West of the Sun')),
('READING',  '2024-02-01 12:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'Kafka on the Shore')),
('FINISHED', '2024-02-28 15:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'Kafka on the Shore')),
-- Martin lee The Miner
('READING',  '2024-03-05 11:00:00', (SELECT id FROM users WHERE username = 'martin'), (SELECT id FROM books WHERE title = 'The Miner')),
('FINISHED', '2024-03-12 22:00:00', (SELECT id FROM users WHERE username = 'martin'), (SELECT id FROM books WHERE title = 'The Miner'));

-- =============================================
-- RATINGS
-- =============================================
INSERT INTO ratings (user_id, book_id, score) VALUES
((SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = 'Kokoro'), 5),
((SELECT id FROM users WHERE username = 'laura'), (SELECT id FROM books WHERE title = 'Norwegian Wood'), 5),
((SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'Kafka on the Shore'), 4),
((SELECT id FROM users WHERE username = 'martin'), (SELECT id FROM books WHERE title = 'The Miner'), 3),
((SELECT id FROM users WHERE username = 'alice'), (SELECT id FROM books WHERE title = 'South of the Border, West of the Sun'), 4)
ON CONFLICT DO NOTHING;

-- =============================================
-- PRÉSTAMOS
-- =============================================
INSERT INTO loans (loan_date, return_date, user_id, book_edition_id) VALUES
('2024-01-15', '2024-02-01', (SELECT id FROM users WHERE username = 'marta'), (SELECT id FROM book_editions WHERE isbn = '9780099448822')),
('2024-02-05', '2024-02-25', (SELECT id FROM users WHERE username = 'paula'), (SELECT id FROM book_editions WHERE isbn = '9780679767398')),
('2024-03-01', NULL, (SELECT id FROM users WHERE username = 'alvaro'), (SELECT id FROM book_editions WHERE isbn = '9781846556203')); -- Libro aún prestado

-- =============================================
-- REVIEWS
-- =============================================
INSERT INTO reviews (review_text, user_id, book_id) VALUES
('A hauntingly beautiful story about loneliness.', (SELECT id FROM users WHERE username = 'laura'), (SELECT id FROM books WHERE title = 'Norwegian Wood')),
('Classic Soseki. The psychological depth is amazing.', (SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = 'Kokoro')),
('Murakami at his most melancholic. Loved it.', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'South of the Border, West of the Sun'));