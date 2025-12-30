-- ============================================
-- 1. NUEVOS AUTORES
--   (nombres no usados previamente)
-- ============================================

INSERT INTO authors (name, birth_date, country, biography) VALUES
('N. K. Jemisin',     '1972-09-19', 'USA',          'American science fiction and fantasy writer, known for complex worlds and social themes.'),
('China Miéville',    '1972-09-06', 'United Kingdom','British speculative fiction writer, mixing fantasy, horror and politics.'),
('Elena Ferrante',    '1943-01-01', 'Italy',        'Pseudonymous Italian novelist, famous for the Neapolitan Novels.'),
('Stephen King',      '1947-09-21', 'USA',          'Prolific author of horror, supernatural fiction, suspense and fantasy.'),
('Jo Nesbø',          '1960-03-29', 'Norway',       'Norwegian writer of crime and thriller novels.'),
('Sally Rooney',      '1991-02-20', 'Ireland',      'Irish author known for contemporary relationship-focused novels.'),
('Neal Stephenson',   '1959-10-31', 'USA',          'American writer of speculative fiction, known for cyberpunk and historical themes.'),
('Donna Tartt',       '1963-12-23', 'USA',          'American author, known for dense and character-driven novels.'),
('Colleen Hoover',    '1979-12-11', 'USA',          'American author of romance and contemporary fiction.'),
('Andrzej Sapkowski', '1948-06-21', 'Poland',       'Polish fantasy writer, creator of The Witcher saga.');


-- ============================================
-- 2. NUEVAS EDITORIALES
--   (nombres distintos a los ya existentes:
--    Penguin Books, Bloomsbury, Planeta,
--    Debolsillo, Vintage, Penguin Random House,
--    HarperCollins, Minotauro)
-- ============================================

INSERT INTO publishers (name, country) VALUES
('Orbit Books', 'United Kingdom'),
('Anagrama',    'Spain'),
('Tor UK',      'United Kingdom'),
('Scribner',    'USA'),
('Alfaguara',   'Spain'),
('Knopf',       'USA'),
('Faber & Faber','United Kingdom'),
('Gollancz',    'United Kingdom');


-- ============================================
-- 3. (SIN NUEVOS GÉNEROS)
--   Usamos solo los géneros que YA tienes:
--   'Ficción', 'Misterio', 'Novela histórica',
--   'Fantasy', 'Science Fiction', 'Classic',
--   'Literary Fiction', 'Adventure', 'Magical Realism'
--   → así evitamos cualquier problema de género_id NULL
-- ============================================


-- ============================================
-- 4. NUEVOS LIBROS
--   - Títulos no repetidos respecto a tus scripts 001–004
--   - Algunos de autores nuevos, otros de autores ya existentes
--     (Murakami, Rothfuss, Zafón), pero con títulos nuevos.
-- ============================================

INSERT INTO books (title, publication_year, author_id, publisher_id) VALUES
-- N. K. Jemisin
('The Fifth Season', 2015,
 (SELECT id FROM authors WHERE name = 'N. K. Jemisin'),
 (SELECT id FROM publishers WHERE name = 'Orbit Books')),
('The Obelisk Gate', 2016,
 (SELECT id FROM authors WHERE name = 'N. K. Jemisin'),
 (SELECT id FROM publishers WHERE name = 'Orbit Books')),

-- China Miéville
('Perdido Street Station', 2000,
 (SELECT id FROM authors WHERE name = 'China Miéville'),
 (SELECT id FROM publishers WHERE name = 'Tor UK')),
('The City & the City', 2009,
 (SELECT id FROM authors WHERE name = 'China Miéville'),
 (SELECT id FROM publishers WHERE name = 'Tor UK')),

-- Elena Ferrante
('My Brilliant Friend', 2011,
 (SELECT id FROM authors WHERE name = 'Elena Ferrante'),
 (SELECT id FROM publishers WHERE name = 'Scribner')),
('The Story of a New Name', 2012,
 (SELECT id FROM authors WHERE name = 'Elena Ferrante'),
 (SELECT id FROM publishers WHERE name = 'Scribner')),

-- Stephen King
('The Shining', 1977,
 (SELECT id FROM authors WHERE name = 'Stephen King'),
 (SELECT id FROM publishers WHERE name = 'Knopf')),
('It', 1986,
 (SELECT id FROM authors WHERE name = 'Stephen King'),
 (SELECT id FROM publishers WHERE name = 'Knopf')),

-- Jo Nesbø
('The Snowman', 2007,
 (SELECT id FROM authors WHERE name = 'Jo Nesbø'),
 (SELECT id FROM publishers WHERE name = 'Alfaguara')),
('The Bat', 1997,
 (SELECT id FROM authors WHERE name = 'Jo Nesbø'),
 (SELECT id FROM publishers WHERE name = 'Alfaguara')),

-- Sally Rooney
('Normal People', 2018,
 (SELECT id FROM authors WHERE name = 'Sally Rooney'),
 (SELECT id FROM publishers WHERE name = 'Faber & Faber')),
('Conversations with Friends', 2017,
 (SELECT id FROM authors WHERE name = 'Sally Rooney'),
 (SELECT id FROM publishers WHERE name = 'Faber & Faber')),

-- Neal Stephenson
('Snow Crash', 1992,
 (SELECT id FROM authors WHERE name = 'Neal Stephenson'),
 (SELECT id FROM publishers WHERE name = 'Gollancz')),
('Cryptonomicon', 1999,
 (SELECT id FROM authors WHERE name = 'Neal Stephenson'),
 (SELECT id FROM publishers WHERE name = 'Gollancz')),

-- Donna Tartt
('The Secret History', 1992,
 (SELECT id FROM authors WHERE name = 'Donna Tartt'),
 (SELECT id FROM publishers WHERE name = 'Knopf')),
('The Goldfinch', 2013,
 (SELECT id FROM authors WHERE name = 'Donna Tartt'),
 (SELECT id FROM publishers WHERE name = 'Knopf')),

-- Colleen Hoover
('It Ends with Us', 2016,
 (SELECT id FROM authors WHERE name = 'Colleen Hoover'),
 (SELECT id FROM publishers WHERE name = 'Scribner')),
('Ugly Love', 2014,
 (SELECT id FROM authors WHERE name = 'Colleen Hoover'),
 (SELECT id FROM publishers WHERE name = 'Scribner')),

-- Andrzej Sapkowski
('The Last Wish', 1993,
 (SELECT id FROM authors WHERE name = 'Andrzej Sapkowski'),
 (SELECT id FROM publishers WHERE name = 'Gollancz')),
('Blood of Elves', 1994,
 (SELECT id FROM authors WHERE name = 'Andrzej Sapkowski'),
 (SELECT id FROM publishers WHERE name = 'Gollancz')),

-- Más libros de autores ya existentes en tu BD (sin repetir títulos)
-- Haruki Murakami (ya existía)
('The Wind-Up Bird Chronicle', 1994,
 (SELECT id FROM authors WHERE name = 'Haruki Murakami'),
 (SELECT id FROM publishers WHERE name = 'Vintage')),

-- Patrick Rothfuss (ya existía)
('The Slow Regard of Silent Things', 2014,
 (SELECT id FROM authors WHERE name = 'Patrick Rothfuss'),
 (SELECT id FROM publishers WHERE name = 'Penguin Random House')),

-- Carlos Ruiz Zafón (ya existía)
('El prisionero del cielo', 2011,
 (SELECT id FROM authors WHERE name = 'Carlos Ruiz Zafón'),
 (SELECT id FROM publishers WHERE name = 'Planeta'));


-- ============================================
-- 5. RELACIONES LIBRO–GÉNERO (book_genres)
--   Se usan solo géneros que ya existen:
--   'Ficción', 'Misterio', 'Novela histórica',
--   'Fantasy', 'Science Fiction', 'Classic',
--   'Literary Fiction', 'Adventure', 'Magical Realism'
-- ============================================

INSERT INTO book_genres (book_id, genre_id) VALUES
-- The Fifth Season: Fantasy + Science Fiction
((SELECT id FROM books WHERE title = 'The Fifth Season'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),
((SELECT id FROM books WHERE title = 'The Fifth Season'),
 (SELECT id FROM genres WHERE name = 'Science Fiction')),

-- The Obelisk Gate: Fantasy
((SELECT id FROM books WHERE title = 'The Obelisk Gate'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),

-- Perdido Street Station: Fantasy + Adventure
((SELECT id FROM books WHERE title = 'Perdido Street Station'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),
((SELECT id FROM books WHERE title = 'Perdido Street Station'),
 (SELECT id FROM genres WHERE name = 'Adventure')),

-- The City & the City: Ficción + Misterio
((SELECT id FROM books WHERE title = 'The City & the City'),
 (SELECT id FROM genres WHERE name = 'Ficción')),
((SELECT id FROM books WHERE title = 'The City & the City'),
 (SELECT id FROM genres WHERE name = 'Misterio')),

-- My Brilliant Friend: Literary Fiction
((SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- The Story of a New Name: Literary Fiction
((SELECT id FROM books WHERE title = 'The Story of a New Name'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- The Shining: Ficción
((SELECT id FROM books WHERE title = 'The Shining'),
 (SELECT id FROM genres WHERE name = 'Ficción')),

-- It: Ficción
((SELECT id FROM books WHERE title = 'It'),
 (SELECT id FROM genres WHERE name = 'Ficción')),

-- The Snowman: Misterio
((SELECT id FROM books WHERE title = 'The Snowman'),
 (SELECT id FROM genres WHERE name = 'Misterio')),

-- The Bat: Misterio
((SELECT id FROM books WHERE title = 'The Bat'),
 (SELECT id FROM genres WHERE name = 'Misterio')),

-- Normal People: Literary Fiction
((SELECT id FROM books WHERE title = 'Normal People'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- Conversations with Friends: Literary Fiction
((SELECT id FROM books WHERE title = 'Conversations with Friends'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- Snow Crash: Science Fiction
((SELECT id FROM books WHERE title = 'Snow Crash'),
 (SELECT id FROM genres WHERE name = 'Science Fiction')),

-- Cryptonomicon: Science Fiction + Classic
((SELECT id FROM books WHERE title = 'Cryptonomicon'),
 (SELECT id FROM genres WHERE name = 'Science Fiction')),
((SELECT id FROM books WHERE title = 'Cryptonomicon'),
 (SELECT id FROM genres WHERE name = 'Classic')),

-- The Secret History: Literary Fiction
((SELECT id FROM books WHERE title = 'The Secret History'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- The Goldfinch: Literary Fiction
((SELECT id FROM books WHERE title = 'The Goldfinch'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- It Ends with Us: Ficción
((SELECT id FROM books WHERE title = 'It Ends with Us'),
 (SELECT id FROM genres WHERE name = 'Ficción')),

-- Ugly Love: Ficción
((SELECT id FROM books WHERE title = 'Ugly Love'),
 (SELECT id FROM genres WHERE name = 'Ficción')),

-- The Last Wish: Fantasy + Adventure
((SELECT id FROM books WHERE title = 'The Last Wish'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),
((SELECT id FROM books WHERE title = 'The Last Wish'),
 (SELECT id FROM genres WHERE name = 'Adventure')),

-- Blood of Elves: Fantasy
((SELECT id FROM books WHERE title = 'Blood of Elves'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),

-- The Wind-Up Bird Chronicle: Literary Fiction
((SELECT id FROM books WHERE title = 'The Wind-Up Bird Chronicle'),
 (SELECT id FROM genres WHERE name = 'Literary Fiction')),

-- The Slow Regard of Silent Things: Fantasy
((SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things'),
 (SELECT id FROM genres WHERE name = 'Fantasy')),

-- El prisionero del cielo: Novela histórica + Misterio
((SELECT id FROM books WHERE title = 'El prisionero del cielo'),
 (SELECT id FROM genres WHERE name = 'Novela histórica')),
((SELECT id FROM books WHERE title = 'El prisionero del cielo'),
 (SELECT id FROM genres WHERE name = 'Misterio'));


-- ============================================
-- 6. NUEVAS EDICIONES (book_editions)
--   - ISBN únicos (no usados en tus scripts)
-- ============================================

INSERT INTO book_editions (isbn, pages, format, publication_date, book_id) VALUES
-- The Fifth Season
('9780316229296', 512, 'PHYSICAL',  '2015-08-04',
 (SELECT id FROM books WHERE title = 'The Fifth Season')),
('9780316229302', 512, 'DIGITAL',   '2016-01-15',
 (SELECT id FROM books WHERE title = 'The Fifth Season')),

-- The Shining
('9780307743657', 447, 'PHYSICAL',  '2012-01-01',
 (SELECT id FROM books WHERE title = 'The Shining')),
('9780385121675', 447, 'DIGITAL',   '2013-10-01',
 (SELECT id FROM books WHERE title = 'The Shining')),

-- My Brilliant Friend
('9781609450786', 336, 'PHYSICAL',  '2012-09-25',
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),
('9781609451479', 336, 'DIGITAL',   '2014-05-10',
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),

-- Normal People
('9780571334650', 304, 'PHYSICAL',  '2018-08-28',
 (SELECT id FROM books WHERE title = 'Normal People')),
('9780571347292', 304, 'DIGITAL',   '2019-01-10',
 (SELECT id FROM books WHERE title = 'Normal People')),

-- Snow Crash
('9780553380958', 480, 'PHYSICAL',  '2000-06-01',
 (SELECT id FROM books WHERE title = 'Snow Crash')),
('9780140232929', 480, 'DIGITAL',   '2003-03-15',
 (SELECT id FROM books WHERE title = 'Snow Crash')),

-- The Last Wish
('9780316029186', 360, 'PHYSICAL',  '2008-12-14',
 (SELECT id FROM books WHERE title = 'The Last Wish')),
('9780316073059', 360, 'DIGITAL',   '2011-05-01',
 (SELECT id FROM books WHERE title = 'The Last Wish')),

-- El prisionero del cielo
('9788408105829', 384, 'PHYSICAL',  '2011-11-17',
 (SELECT id FROM books WHERE title = 'El prisionero del cielo')),
('9788408130647', 384, 'DIGITAL',   '2013-03-01',
 (SELECT id FROM books WHERE title = 'El prisionero del cielo'));


-- ============================================
-- 7. NUEVOS USUARIOS
--   (sin repetir usernames/emails de 001–004)
-- ============================================

INSERT INTO users (username, email, birth_date) VALUES
('sofia',   'sofia@example.com',   '1996-04-12'),
('raul',    'raul@example.com',    '1990-11-03'),
('diego',   'diego@example.com',   '1988-07-22'),
('clara',   'clara@example.com',   '1995-02-18'),
('sergio',  'sergio@example.com',  '1989-09-09'),
('lucia',   'lucia@example.com',   '1997-12-30'),
('pablo',   'pablo@example.com',   '1993-03-05'),
('andrea',  'andrea@example.com',  '1998-08-21'),
('monica',  'monica@example.com',  '1992-01-11'),
('jorge',   'jorge@example.com',   '1987-05-27'),
('camila',  'camila@example.com',  '1999-06-16'),
('felix',   'felix@example.com',   '1985-10-02'),
('gema',    'gema@example.com',    '1994-09-19'),
('roberto', 'roberto@example.com', '1986-02-23'),
('ines',    'ines@example.com',    '1991-03-14');


-- ============================================
-- 8. USER_BOOKS
--   (cada usuario nuevo con varios libros)
-- ============================================

-- sofia: fantasía y contemporáneo
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season'),
 '2023-01-10'),
((SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'Normal People'),
 '2023-01-20'),
((SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 '2023-02-01');

-- raul: terror y sci-fi
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining'),
 '2023-01-15'),
((SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'It'),
 '2023-02-01'),
((SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'Snow Crash'),
 '2023-02-10');

-- diego: thriller y crímenes
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman'),
 '2023-01-18'),
((SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The City & the City'),
 '2023-02-05');

-- clara: romance y contemporáneo
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us'),
 '2023-01-22'),
((SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'Ugly Love'),
 '2023-02-12'),
((SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'Conversations with Friends'),
 '2023-02-20');

-- sergio: Witcher + Jemisin
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish'),
 '2023-02-01'),
((SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'),
 '2023-02-18'),
((SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Obelisk Gate'),
 '2023-03-01');

-- lucia: Ferrante + Zafón
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'lucia'),
 (SELECT id FROM books WHERE title = 'The Story of a New Name'),
 '2023-02-05'),
((SELECT id FROM users WHERE username = 'lucia'),
 (SELECT id FROM books WHERE title = 'El prisionero del cielo'),
 '2023-02-25');

-- pablo: Tartt + Stephenson
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History'),
 '2023-02-10'),
((SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'Cryptonomicon'),
 '2023-03-05');

-- andrea: Murakami + Hoover
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'andrea'),
 (SELECT id FROM books WHERE title = 'The Wind-Up Bird Chronicle'),
 '2023-03-01'),
((SELECT id FROM users WHERE username = 'andrea'),
 (SELECT id FROM books WHERE title = 'It Ends with Us'),
 '2023-03-15');

-- monica: terror de King
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It'),
 '2023-03-02'),
((SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'The Shining'),
 '2023-03-20');

-- jorge: fantasía oscura
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'jorge'),
 (SELECT id FROM books WHERE title = 'The Last Wish'),
 '2023-03-05'),
((SELECT id FROM users WHERE username = 'jorge'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'),
 '2023-03-25'),
((SELECT id FROM users WHERE username = 'jorge'),
 (SELECT id FROM books WHERE title = 'The Fifth Season'),
 '2023-04-01');

-- camila: contemporáneo y relaciones
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People'),
 '2023-03-10'),
((SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 '2023-03-18');

-- felix: sci-fi dura
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash'),
 '2023-03-12'),
((SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Cryptonomicon'),
 '2023-03-28');

-- gema: Donna Tartt
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'gema'),
 (SELECT id FROM books WHERE title = 'The Secret History'),
 '2023-03-15'),
((SELECT id FROM users WHERE username = 'gema'),
 (SELECT id FROM books WHERE title = 'The Goldfinch'),
 '2023-04-02');

-- roberto: Witcher + Rothfuss corto
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'),
 '2023-03-20'),
((SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things'),
 '2023-04-05');

-- ines: Zafón y Ferrante
INSERT INTO user_books (user_id, book_id, added_at) VALUES
((SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'El prisionero del cielo'),
 '2023-03-25'),
((SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'The Story of a New Name'),
 '2023-04-08');


-- ============================================
-- 9. HISTÓRICO DE ESTADOS (reading_status_history)
--   (status, status_date, user_id, book_id)
-- ============================================

-- sofia: The Fifth Season (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-01-10',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season')),
('READING',  '2023-01-15',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season')),
('FINISHED', '2023-01-30',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season'));

-- sofia: Normal People (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2023-01-20',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'Normal People')),
('READING', '2023-02-02',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'Normal People'));

-- raul: The Shining (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-01-15',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining')),
('READING',  '2023-01-20',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining')),
('FINISHED', '2023-02-05',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining'));

-- raul: It (abandonado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',   '2023-02-01',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'It')),
('READING',   '2023-02-10',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'It')),
('ABANDONED', '2023-02-25',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'It'));

-- diego: The Snowman (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-01-18',
 (SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman')),
('READING',  '2023-01-25',
 (SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman')),
('FINISHED', '2023-02-03',
 (SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman'));

-- clara: It Ends with Us (terminado + relectura)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',    '2023-01-22',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us')),
('READING',    '2023-01-25',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us')),
('FINISHED',   '2023-02-02',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us')),
('RE_READING', '2023-03-01',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us')),
('READING',    '2023-03-02',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us'));

-- sergio: The Last Wish (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-02-01',
 (SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),
('READING',  '2023-02-05',
 (SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),
('FINISHED', '2023-02-20',
 (SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish'));

-- lucia: El prisionero del cielo (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2023-02-25',
 (SELECT id FROM users WHERE username = 'lucia'),
 (SELECT id FROM books WHERE title = 'El prisionero del cielo')),
('READING', '2023-03-05',
 (SELECT id FROM users WHERE username = 'lucia'),
 (SELECT id FROM books WHERE title = 'El prisionero del cielo'));

-- pablo: The Secret History (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-02-10',
 (SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History')),
('READING',  '2023-02-18',
 (SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History')),
('FINISHED', '2023-03-05',
 (SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History'));

-- andrea: The Wind-Up Bird Chronicle (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2023-03-01',
 (SELECT id FROM users WHERE username = 'andrea'),
 (SELECT id FROM books WHERE title = 'The Wind-Up Bird Chronicle')),
('READING', '2023-03-20',
 (SELECT id FROM users WHERE username = 'andrea'),
 (SELECT id FROM books WHERE title = 'The Wind-Up Bird Chronicle'));

-- monica: It (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-03-02',
 (SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It')),
('READING',  '2023-03-10',
 (SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It')),
('FINISHED', '2023-03-30',
 (SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It'));

-- jorge: Blood of Elves (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2023-03-25',
 (SELECT id FROM users WHERE username = 'jorge'),
 (SELECT id FROM books WHERE title = 'Blood of Elves')),
('READING', '2023-04-05',
 (SELECT id FROM users WHERE username = 'jorge'),
 (SELECT id FROM books WHERE title = 'Blood of Elves'));

-- camila: Normal People (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-03-10',
 (SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People')),
('READING',  '2023-03-15',
 (SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People')),
('FINISHED', '2023-03-28',
 (SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People'));

-- felix: Snow Crash (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-03-12',
 (SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),
('READING',  '2023-03-18',
 (SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),
('FINISHED', '2023-03-29',
 (SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash'));

-- gema: The Goldfinch (leyendo)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ', '2023-04-02',
 (SELECT id FROM users WHERE username = 'gema'),
 (SELECT id FROM books WHERE title = 'The Goldfinch')),
('READING', '2023-04-12',
 (SELECT id FROM users WHERE username = 'gema'),
 (SELECT id FROM books WHERE title = 'The Goldfinch'));

-- roberto: The Slow Regard of Silent Things (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-04-05',
 (SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things')),
('READING',  '2023-04-07',
 (SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things')),
('FINISHED', '2023-04-12',
 (SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things'));

-- ines: My Brilliant Friend (terminado)
INSERT INTO reading_status_history (status, status_date, user_id, book_id) VALUES
('TO_READ',  '2023-03-25',
 (SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),
('READING',  '2023-03-30',
 (SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend')),
('FINISHED', '2023-04-10',
 (SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'));


-- ============================================
-- 10. REVIEWS
--   reviews(review_text, created_at, user_id, book_id)
--   (solo para FINISHED)
-- ============================================

INSERT INTO reviews (review_text, created_at, user_id, book_id) VALUES
('Brutal, original and emotionally devastating. A masterclass in worldbuilding.',
 '2023-01-31',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season')),

('Creepy, atmospheric and surprisingly human. King at his best.',
 '2023-02-06',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining')),

('Tense and bleak Nordic crime with a chilling atmosphere.',
 '2023-02-04',
 (SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman')),

('Intense, emotional and hard to put down. A powerful romance with heavy themes.',
 '2023-02-03',
 (SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us')),

('Dark, witty and full of sharp character moments. A great entry into the Witcher world.',
 '2023-02-21',
 (SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish')),

('Dense, intellectual and strangely addictive. A campus novel that lingers for days.',
 '2023-03-06',
 (SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History')),

('Deeply unsettling and unexpectedly moving. King stretches horror into something more tragic.',
 '2023-03-31',
 (SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It')),

('Sharp, intimate and painfully real portrait of modern relationships.',
 '2023-03-29',
 (SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People')),

('Wild, inventive and visionary sci-fi with a hacker soul.',
 '2023-03-30',
 (SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash')),

('Quiet, strange and beautifully written. A small story that feels huge emotionally.',
 '2023-04-13',
 (SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things')),

('Intimate, complex and full of small, unforgettable details about friendship and growth.',
 '2023-04-11',
 (SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'));


-- ============================================
-- 11. RATINGS
--   ratings(user_id, book_id, score, created_at)
-- ============================================

INSERT INTO ratings (user_id, book_id, score, created_at) VALUES
((SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM books WHERE title = 'The Fifth Season'),
 5, '2023-01-31'),

((SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM books WHERE title = 'The Shining'),
 5, '2023-02-06'),

((SELECT id FROM users WHERE username = 'diego'),
 (SELECT id FROM books WHERE title = 'The Snowman'),
 4, '2023-02-04'),

((SELECT id FROM users WHERE username = 'clara'),
 (SELECT id FROM books WHERE title = 'It Ends with Us'),
 5, '2023-02-03'),

((SELECT id FROM users WHERE username = 'sergio'),
 (SELECT id FROM books WHERE title = 'The Last Wish'),
 5, '2023-02-21'),

((SELECT id FROM users WHERE username = 'pablo'),
 (SELECT id FROM books WHERE title = 'The Secret History'),
 5, '2023-03-06'),

((SELECT id FROM users WHERE username = 'monica'),
 (SELECT id FROM books WHERE title = 'It'),
 4, '2023-03-31'),

((SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM books WHERE title = 'Normal People'),
 5, '2023-03-29'),

((SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM books WHERE title = 'Snow Crash'),
 5, '2023-03-30'),

((SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM books WHERE title = 'The Slow Regard of Silent Things'),
 4, '2023-04-13'),

((SELECT id FROM users WHERE username = 'ines'),
 (SELECT id FROM books WHERE title = 'My Brilliant Friend'),
 5, '2023-04-11');


-- ============================================
-- 12. LOANS (PRÉSTAMOS)
--   loans(loan_date, return_date, user_id, book_edition_id)
-- ============================================

INSERT INTO loans (loan_date, return_date, user_id, book_edition_id) VALUES
-- sofia: The Fifth Season físico
('2023-01-10', '2023-01-28',
 (SELECT id FROM users WHERE username = 'sofia'),
 (SELECT id FROM book_editions WHERE isbn = '9780316229296')),

-- raul: The Shining físico
('2023-01-15', '2023-02-10',
 (SELECT id FROM users WHERE username = 'raul'),
 (SELECT id FROM book_editions WHERE isbn = '9780307743657')),

-- felix: Snow Crash físico
('2023-03-12', '2023-03-27',
 (SELECT id FROM users WHERE username = 'felix'),
 (SELECT id FROM book_editions WHERE isbn = '9780553380958')),

-- lucia: El prisionero del cielo físico
('2023-02-25', '2023-03-15',
 (SELECT id FROM users WHERE username = 'lucia'),
 (SELECT id FROM book_editions WHERE isbn = '9788408105829')),

-- camila: Normal People físico
('2023-03-10', '2023-03-30',
 (SELECT id FROM users WHERE username = 'camila'),
 (SELECT id FROM book_editions WHERE isbn = '9780571334650')),

-- roberto: The Last Wish físico (aún sin devolver)
('2023-03-20', NULL,
 (SELECT id FROM users WHERE username = 'roberto'),
 (SELECT id FROM book_editions WHERE isbn = '9780316029186'));
