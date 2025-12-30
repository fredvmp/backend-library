INSERT INTO users (username, email, birth_date)
VALUES
('david', 'david@example.com', '1992-11-03'),
('laura', 'laura@example.com', '1997-06-18'),
('marta', 'marta@example.com', '1989-02-25');

INSERT INTO ratings (user_id, book_id, score)
VALUES
(
    (SELECT id FROM users WHERE username = 'david'),
    (SELECT id FROM books WHERE title = '1984'),
    5
),
(
    (SELECT id FROM users WHERE username = 'laura'),
    (SELECT id FROM books WHERE title = 'Harry Potter and the Philosopher''s Stone'),
    4
),
(
    (SELECT id FROM users WHERE username = 'marta'),
    (SELECT id FROM books WHERE title = 'La sombra del viento'),
    5
);

INSERT INTO reviews (review_text, user_id, book_id)
VALUES
(
    'A disturbing but brilliant vision of the future.',
    (SELECT id FROM users WHERE username = 'david'),
    (SELECT id FROM books WHERE title = '1984')
),
(
    'Magical, immersive and perfect to start the saga.',
    (SELECT id FROM users WHERE username = 'laura'),
    (SELECT id FROM books WHERE title = 'Harry Potter and the Philosopher''s Stone')
),
(
    'An atmospheric and emotional story, beautifully written.',
    (SELECT id FROM users WHERE username = 'marta'),
    (SELECT id FROM books WHERE title = 'La sombra del viento')
);

INSERT INTO user_books (user_id, book_id)
VALUES
(
    (SELECT id FROM users WHERE username = 'david'),
    (SELECT id FROM books WHERE title = 'Animal Farm')
),
(
    (SELECT id FROM users WHERE username = 'laura'),
    (SELECT id FROM books WHERE title = 'Harry Potter and the Philosopher''s Stone')
),
(
    (SELECT id FROM users WHERE username = 'marta'),
    (SELECT id FROM books WHERE title = 'El juego del ángel')
);

INSERT INTO reading_status_history (status, user_id, book_id)
VALUES
(
    'READING',
    (SELECT id FROM users WHERE username = 'david'),
    (SELECT id FROM books WHERE title = '1984')
),
(
    'FINISHED',
    (SELECT id FROM users WHERE username = 'david'),
    (SELECT id FROM books WHERE title = '1984')
),
(
    'READING',
    (SELECT id FROM users WHERE username = 'marta'),
    (SELECT id FROM books WHERE title = 'La sombra del viento')
);

INSERT INTO loans (loan_date, return_date, user_id, book_edition_id)
VALUES
(
    '2024-01-10',
    '2024-01-25',
    (SELECT id FROM users WHERE username = 'laura'),
    (
        SELECT id
        FROM book_editions
        WHERE isbn = '9788432223451'
    )
),
(
    '2024-02-01',
    NULL,
    (SELECT id FROM users WHERE username = 'david'),
    (
        SELECT id
        FROM book_editions
        WHERE isbn = '9788432223452'
    )
);


