-- Caso 1: Varios usuarios leyendo el mismo libro ('1984') con distintos ritmos
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
-- David: Lector promedio (8 días)
('READING',  '2024-01-10 09:00:00', (SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = '1984')),
('FINISHED', '2024-01-18 21:00:00', (SELECT id FROM users WHERE username = 'david'), (SELECT id FROM books WHERE title = '1984')),
-- Alice: Lectora ultra-rápida (2 días)
('READING',  '2024-02-01 10:00:00', (SELECT id FROM users WHERE username = 'alice'), (SELECT id FROM books WHERE title = '1984')),
('FINISHED', '2024-02-03 15:00:00', (SELECT id FROM users WHERE username = 'alice'), (SELECT id FROM books WHERE title = '1984')),
-- Bob: Lector lento (25 días)
('READING',  '2024-01-05 12:00:00', (SELECT id FROM users WHERE username = 'bob'), (SELECT id FROM books WHERE title = '1984')),
('FINISHED', '2024-01-30 23:00:00', (SELECT id FROM users WHERE username = 'bob'), (SELECT id FROM books WHERE title = '1984'));

-- Caso 2: Martin (del script 006) lee 'Snow Crash' (Sci-Fi / ahora Sci-Fi)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('READING',  '2024-03-01 08:30:00', (SELECT id FROM users WHERE username = 'martin'), (SELECT id FROM books WHERE title = 'Snow Crash')),
('FINISHED', '2024-03-05 19:45:00', (SELECT id FROM users WHERE username = 'martin'), (SELECT id FROM books WHERE title = 'Snow Crash'));

-- Caso 3: Paula (del script 006) lee Fantasía
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('READING',  '2024-02-15 10:00:00', (SELECT id FROM users WHERE username = 'paula'), (SELECT id FROM books WHERE title = 'The Last Wish')),
('FINISHED', '2024-02-17 12:00:00', (SELECT id FROM users WHERE username = 'paula'), (SELECT id FROM books WHERE title = 'The Last Wish'));

-- Caso 4: Registro de 'Día 0' (empezado y terminado mismo día) para probar tu .clip(lower=1)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('READING',  '2024-03-10 09:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'Animal Farm')),
('FINISHED', '2024-03-10 22:00:00', (SELECT id FROM users WHERE username = 'valeria'), (SELECT id FROM books WHERE title = 'Animal Farm'));