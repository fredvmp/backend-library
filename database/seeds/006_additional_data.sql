-- ============================================
-- 1. NUEVOS USUARIOS (solo para generar variedad)
-- ============================================

INSERT INTO users (username, email, birth_date) VALUES
('valeria', 'valeria@example.com', '1994-07-11'),
('martin',  'martin@example.com',  '1986-03-22'),
('alvaro',  'alvaro@example.com',  '1992-10-05'),
('paula',   'paula@example.com',   '1998-12-14'),
('noa',     'noa@example.com',     '1999-01-30'),
('dario',   'dario@example.com',   '1985-06-09'),
('helena',  'helena@example.com',  '1993-09-17'),
('ruben',   'ruben@example.com',   '1990-11-28');

-- ============================================
-- 2. USER_BOOKS (asociamos estos usuarios a libros ya existentes)
-- ============================================

-- valeria: Ferrante + King
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 '2024-01-10'),
((SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'The Shining'),
 '2024-01-15');

-- martin: Snow Crash + The Fifth Season
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash'),
 '2024-01-12'),
((SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'The Fifth Season'),
 '2024-01-20');

-- alvaro: The Secret History + It Ends with Us
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'The Secret History'),
 '2024-02-01'),
((SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'It Ends with Us'),
 '2024-02-10');

-- paula: The Last Wish + Normal People
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish'),
 '2024-02-05'),
((SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'Normal People'),
 '2024-02-15');

-- noa: Blood of Elves + The Goldfinch
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'),
 '2024-02-12'),
((SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'The Goldfinch'),
 '2024-02-20');

-- dario: The City & the City + The Snowman
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'dario'),
 (SELECT id FROM books WHERE title = 'The City & the City'),
 '2024-02-18'),
((SELECT id FROM users WHERE username = 'dario'),
 (SELECT id FROM books WHERE title = 'The Snowman'),
 '2024-02-25');

-- helena: The Wind-Up Bird Chronicle + Ugly Love
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'helena'),
 (SELECT id FROM books WHERE title = 'The Wind-Up Bird Chronicle'),
 '2024-03-01'),
((SELECT id FROM users WHERE username = 'helena'),
 (SELECT id FROM books WHERE title = 'Ugly Love'),
 '2024-03-10');

-- ruben: The Slow Regard of Silent Things + El prisionero del cielo
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'ruben'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things'),
 '2024-03-05'),
((SELECT id FROM users WHERE username = 'ruben'),
 (SELECT id FROM books WHERE title = 'El prisionero del cielo'),
 '2024-03-12');

-- ============================================
-- 3. READING_STATUS_HISTORY
--   (variedad de estados para agregaciones)
-- ============================================

-- valeria: My Brilliant Friend (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2024-01-10',
 (SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),
('READING',  '2024-01-12',
 (SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),
('FINISHED', '2024-01-20',
 (SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'));

-- martin: Snow Crash (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2024-01-12',
 (SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),
('READING',  '2024-01-18',
 (SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),
('FINISHED', '2024-01-28',
 (SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash'));

-- alvaro: The Secret History (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2024-02-01',
 (SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'The Secret History')),
('READING', '2024-02-10',
 (SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'The Secret History'));

-- paula: The Last Wish (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2024-02-05',
 (SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),
('READING',  '2024-02-08',
 (SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),
('FINISHED', '2024-02-20',
 (SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish'));

-- noa: Blood of Elves (abandonado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',   '2024-02-12',
 (SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves')),
('READING',   '2024-02-18',
 (SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves')),
('ABANDONED', '2024-02-28',
 (SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'));

-- ============================================
-- 4. REVIEWS (nuevas opiniones para agregaciones)
-- ============================================

INSERT INTO reviews (review_text, created_at, user_id, book_id) VALUES
('A beautifully written and emotionally rich novel.', '2024-01-21',
 (SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),

('Fast-paced, chaotic and incredibly imaginative.', '2024-01-29',
 (SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),

('Dark, elegant and full of tension.', '2024-02-15',
 (SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'The Secret History')),

('A fantastic entry into the Witcher universe.', '2024-02-22',
 (SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),

('A dense but rewarding fantasy novel.', '2024-02-28',
 (SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'));

-- ============================================
-- 5. RATINGS (más puntuaciones para AVG, COUNT, etc.)
-- ============================================

INSERT INTO ratings (user_id, book_id, score, created_at) VALUES
((SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 4, '2024-01-21'),

((SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM books WHERE title = 'Snow Crash'),
 5, '2024-01-29'),

((SELECT id FROM users WHERE username = 'alvaro'),
 (SELECT id FROM books WHERE title = 'The Secret History'),
 4, '2024-02-15'),

((SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM books WHERE title = 'The Last Wish'),
 5, '2024-02-22'),

((SELECT id FROM users WHERE username = 'noa'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'),
 3, '2024-02-28');

-- ============================================
-- 6. LOANS (préstamos adicionales)
-- ============================================

INSERT INTO loans (loan_date, return_date, user_id, book_edition_id) VALUES
('2024-01-10', '2024-01-25',
 (SELECT id FROM users WHERE username = 'valeria'),
 (SELECT id FROM book_editions WHERE isbn = '9781609450786')),

('2024-01-12', '2024-01-30',
 (SELECT id FROM users WHERE username = 'martin'),
 (SELECT id FROM book_editions WHERE isbn = '9780553380958')),

('2024-02-05', NULL,
 (SELECT id FROM users WHERE username = 'paula'),
 (SELECT id FROM book_editions WHERE isbn = '9780316029186'));
