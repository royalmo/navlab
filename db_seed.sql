-- Max mostres trigger creation.
CREATE TRIGGER max_mostres before insert on mostres when(select count(sensor_name) from mostres)>=5000
begin
delete from mostres where date=(select min(date) from mostres);
end;

-- Data to seed the database
INSERT INTO user VALUES
    (1, 'Super User', 'super@user.com', '{0}', 1, 1, 'en'),
    (2, 'Aleix Llusà', 'aleix.llusa@upc.edu', '{0}', 1, 0, 'ca'),
    (3, 'Deactivated User', 'foo@bar.com', '{0}', 0, 0, 'ca')
;

INSERT INTO server VALUES
    (1, 'Minecraft', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft server.', 'start_cmd', 'stop_cmd', NULL),
    (2, 'No Icon', 'https://theme.zdassets.com/this/icon/doesnt/exist.png', 'This is a server without icon, to test everything.', 'start_cmd', 'stop_cmd', 1),
    (3, 'Overleaf', 'https://cdn.overleaf.com/img/ol-brand/overleaf_og_logo.png', 'This is our nice and beautiful Overleaf server.', 'start_cmd', 'stop_cmd', 0),
    (4, 'Minecraft 2', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft 2 server.', 'start_cmd', 'stop_cmd', 1),
    (5, 'Ubuntu Server', 'https://cdn-icons-png.flaticon.com/512/5969/5969282.png', 'This is our nice and beautiful Ubuntu server.', 'start_cmd', 'stop_cmd', 0)
;
