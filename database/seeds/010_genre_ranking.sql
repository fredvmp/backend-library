INSERT INTO genres (name) VALUES ('Fantasía') 
ON CONFLICT DO NOTHING;

INSERT INTO authors (name) VALUES ('J.R.R. Tolkien') 
ON CONFLICT DO NOTHING;

INSERT INTO books (title, author_id, genre_id) VALUES 
('El Hobbit', (SELECT id FROM authors WHERE name='J.R.R. Tolkien' LIMIT 1), 
              (SELECT id FROM genres WHERE name='Fantasía' LIMIT 1)),
('El Silmarillion', (SELECT id FROM authors WHERE name='J.R.R. Tolkien' LIMIT 1), 
                    (SELECT id FROM genres WHERE name='Fantasía' LIMIT 1))
ON CONFLICT DO NOTHING;

INSERT INTO users (username, email) VALUES ('elena', 'elena@example.com') 
ON CONFLICT DO NOTHING;

INSERT INTO ratings (user_id, book_id, score) VALUES 
((SELECT id FROM users WHERE username='elena' LIMIT 1), 
 (SELECT title_id FROM (SELECT id as title_id, title FROM books) as b WHERE title='El Hobbit' LIMIT 1), 5),
((SELECT id FROM users WHERE username='elena' LIMIT 1), 
 (SELECT title_id FROM (SELECT id as title_id, title FROM books) as b WHERE title='El Silmarillion' LIMIT 1), 4)
ON CONFLICT DO NOTHING;

INSERT INTO books (title, author_id, genre_id) VALUES 
('El retorno del Rey', (SELECT id FROM authors WHERE name='J.R.R. Tolkien' LIMIT 1), 
                       (SELECT id FROM genres WHERE name='Fantasía' LIMIT 1)),
('Las dos torres', (SELECT id FROM authors WHERE name='J.R.R. Tolkien' LIMIT 1), 
                    (SELECT id FROM genres WHERE name='Fantasía' LIMIT 1))
ON CONFLICT DO NOTHING;

INSERT INTO users (username, email) VALUES 
('ivan', 'ivan@example.com'),
('marta', 'marta@example.com')
ON CONFLICT DO NOTHING;

INSERT INTO ratings (user_id, book_id, score) VALUES 
((SELECT id FROM users WHERE username='ivan' LIMIT 1), (SELECT id FROM books WHERE title='El Hobbit' LIMIT 1), 4),
((SELECT id FROM users WHERE username='ivan' LIMIT 1), (SELECT id FROM books WHERE title='El Silmarillion' LIMIT 1), 4),
((SELECT id FROM users WHERE username='ivan' LIMIT 1), (SELECT id FROM books WHERE title='El retorno del Rey' LIMIT 1), 4)
ON CONFLICT DO NOTHING;

INSERT INTO ratings (user_id, book_id, score) VALUES 
((SELECT id FROM users WHERE username='marta' LIMIT 1), (SELECT id FROM books WHERE title='El Hobbit' LIMIT 1), 5),
((SELECT id FROM users WHERE username='marta' LIMIT 1), (SELECT id FROM books WHERE title='El Silmarillion' LIMIT 1), 5),
((SELECT id FROM users WHERE username='marta' LIMIT 1), (SELECT id FROM books WHERE title='El retorno del Rey' LIMIT 1), 5),
((SELECT id FROM users WHERE username='marta' LIMIT 1), (SELECT id FROM books WHERE title='Las dos torres' LIMIT 1), 4)
ON CONFLICT DO NOTHING;