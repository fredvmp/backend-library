-- 1. Crear 'Sci-Fi' y 'Fiction'
INSERT INTO genres (name) VALUES ('Sci-Fi'), ('Fiction') 
ON CONFLICT (name) DO NOTHING;

-- 2. Movemos libros de 'Science Fiction' a 'Sci-Fi'
UPDATE book_genres 
SET genre_id = (SELECT id FROM genres WHERE name = 'Sci-Fi')
WHERE genre_id = (SELECT id FROM genres WHERE name = 'Science Fiction');

-- 3. Movemos libros de 'Ficción' y 'Literary Fiction' a 'Fiction'
UPDATE book_genres 
SET genre_id = (SELECT id FROM genres WHERE name = 'Fiction')
WHERE genre_id IN (SELECT id FROM genres WHERE name IN ('Ficción', 'Literary Fiction'));

-- 4. Borramos los géneros antiguos que ya no tienen libros asociados
DELETE FROM genres WHERE name IN ('Science Fiction', 'Ficción', 'Literary Fiction');