-- Data to seed the database
INSERT INTO user VALUES
    (1, 'Super User', 'super@user.com', '$2b$12$rABZ8UJM5tmzjKaYH0QFg.1vQ1tMRv5mdINUAT9nlWvup5G2jH7C2', 1, 1, 'en'),
    (2, 'Aleix Llusà', 'aleix.llusa@upc.edu', '$2b$12$rABZ8UJM5tmzjKaYH0QFg.1vQ1tMRv5mdINUAT9nlWvup5G2jH7C2', 1, 0, 'ca'),
    (3, 'Deactivated User', 'foo@bar.com', '$2b$12$rABZ8UJM5tmzjKaYH0QFg.1vQ1tMRv5mdINUAT9nlWvup5G2jH7C2', 0, 0, 'ca')
;

INSERT INTO server VALUES
    (1, 'Minecraft', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft server.', 'start_cmd', 'stop_cmd', 'status_cmd'),
    (2, 'No Icon', 'https://theme.zdassets.com/this/icon/doesnt/exist.png', 'This is a server without icon, to test everything.', 'start_cmd', 'stop_cmd', 'status_cmd'),
    (3, 'Overleaf', 'https://cdn.overleaf.com/img/ol-brand/overleaf_og_logo.png', 'This is our nice and beautiful Overleaf server.', 'start_cmd', 'stop_cmd', 'status_cmd'),
    (4, 'Minecraft 2', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft 2 server.', 'start_cmd', 'stop_cmd', 'status_cmd'),
    (5, 'Ubuntu Server', 'https://cdn-icons-png.flaticon.com/512/5969/5969282.png', 'This is our nice and beautiful Ubuntu server.', 'start_cmd', 'stop_cmd', 'status_cmd')
;
