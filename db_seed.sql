-- Data to seed the database

INSERT INTO user VALUES
    (1, 'Super User', 'super@user.com', '{0}', 1, 1, 'en'),
    (2, 'Aleix Llusà', 'aleix.llusa@upc.edu', '{0}', 1, 0, 'ca'),
    (3, 'Deactivated User', 'foo@bar.com', '{0}', 0, 0, 'ca')
;

INSERT INTO server VALUES
    --(1, 'Minecraft', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft server.', 'start_cmd', 'stop_cmd', NULL),
    --(2, 'No Icon', 'https://theme.zdassets.com/this/icon/doesnt/exist.png', 'This is a server without icon, to test everything.', 'start_cmd', 'stop_cmd', 1),
    --(3, 'Overleaf', 'https://cdn.overleaf.com/img/ol-brand/overleaf_og_logo.png', 'This is our nice and beautiful Overleaf server.', 'start_cmd', 'stop_cmd', 0),
    --(4, 'Minecraft 2', 'https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370.png', 'This is our nice and beautiful Minecraft 2 server.', 'start_cmd', 'stop_cmd', 1),
    --(5, 'Ubuntu Server', 'https://cdn-icons-png.flaticon.com/512/5969/5969282.png', 'This is our nice and beautiful Ubuntu server.', 'start_cmd', 'stop_cmd', 0)
    (1, "Navarcles' Arduino: LED", "https://navlab.ericroy.net/static/media/led.png", "This is the LED that can be found in Isaac's Arduino.", '', '', 0)
;

INSERT INTO monitor (key, title, label, min_value, max_value) VALUES
    ('led', "Navarcles' Arduino: LED", "Status", -0.5, 1.5),
    ('potenciometre', "Navarcles' Arduino: Potentiometer", "Value", 0, 255)--,
    -- ('navlab_temp', "Navarcles' Raspberry: Temperature", "Temperature (C)", NULL, NULL)
;

-- Inserting sample led values
INSERT INTO sample (monitor_key, date, value) VALUES
  ('led', DATETIME('2023-05-20 00:00:00'), 0),
  ('led', DATETIME('2023-05-20 00:00:05'), 1),
  ('led', DATETIME('2023-05-20 00:00:10'), 0),
  ('led', DATETIME('2023-05-20 00:00:15'), 1),
  ('led', DATETIME('2023-05-20 00:00:20'), 0),
  ('led', DATETIME('2023-05-20 00:00:25'), 1),
  ('led', DATETIME('2023-05-20 00:00:30'), 0),
  ('led', DATETIME('2023-05-20 00:00:35'), 1),
  ('led', DATETIME('2023-05-20 00:00:40'), 0),
  ('led', DATETIME('2023-05-20 00:00:45'), 1),
  ('led', DATETIME('2023-05-20 00:00:50'), 0),
  ('led', DATETIME('2023-05-20 00:00:55'), 1),
  ('led', DATETIME('2023-05-20 00:01:00'), 0),
  ('led', DATETIME('2023-05-20 00:01:05'), 1),
  ('led', DATETIME('2023-05-20 00:01:10'), 0),
  ('led', DATETIME('2023-05-20 00:01:15'), 1),
  ('led', DATETIME('2023-05-20 00:01:20'), 0),
  ('led', DATETIME('2023-05-20 00:01:25'), 1),
  ('led', DATETIME('2023-05-20 00:01:30'), 0),
  ('led', DATETIME('2023-05-20 00:01:35'), 0),
  ('led', DATETIME('2023-05-20 00:01:40'), 0),
  ('led', DATETIME('2023-05-20 00:01:45'), 0),
  ('led', DATETIME('2023-05-20 00:01:50'), 0),
  ('led', DATETIME('2023-05-20 00:01:55'), 0),
  ('led', DATETIME('2023-05-20 00:02:00'), 0),
  ('led', DATETIME('2023-05-20 00:02:05'), 0),
  ('led', DATETIME('2023-05-20 00:02:10'), 0),
  ('led', DATETIME('2023-05-20 00:02:15'), 0),
  ('led', DATETIME('2023-05-20 00:02:20'), 0),
  ('led', DATETIME('2023-05-20 00:02:25'), 0),
  ('led', DATETIME('2023-05-20 00:02:30'), 0),
  ('led', DATETIME('2023-05-20 00:02:35'), 0),
  ('led', DATETIME('2023-05-20 00:02:40'), 0),
  ('led', DATETIME('2023-05-20 00:02:45'), 1),
  ('led', DATETIME('2023-05-20 00:02:50'), 1),
  ('led', DATETIME('2023-05-20 00:02:55'), 1),
  ('led', DATETIME('2023-05-20 00:03:00'), 1),
  ('led', DATETIME('2023-05-20 00:03:05'), 1),
  ('led', DATETIME('2023-05-20 00:03:10'), 1),
  ('led', DATETIME('2023-05-20 00:03:15'), 1),
  ('led', DATETIME('2023-05-20 00:03:20'), 1),
  ('led', DATETIME('2023-05-20 00:03:25'), 1),
  ('led', DATETIME('2023-05-20 00:03:30'), 1),
  ('led', DATETIME('2023-05-20 00:03:35'), 1)
;

-- Inserting sample potentiometer values
INSERT INTO Sample (monitor_key, date, value) VALUES
  ('potenciometre', DATETIME('2023-05-20 00:00:00'), 100),
  ('potenciometre', DATETIME('2023-05-20 00:00:05'), 105),
  ('potenciometre', DATETIME('2023-05-20 00:00:10'), 110),
  ('potenciometre', DATETIME('2023-05-20 00:00:15'), 115),
  ('potenciometre', DATETIME('2023-05-20 00:00:20'), 120),
  ('potenciometre', DATETIME('2023-05-20 00:00:25'), 125),
  ('potenciometre', DATETIME('2023-05-20 00:00:30'), 130),
  ('potenciometre', DATETIME('2023-05-20 00:00:35'), 135),
  ('potenciometre', DATETIME('2023-05-20 00:00:40'), 140),
  ('potenciometre', DATETIME('2023-05-20 00:00:45'), 145),
  ('potenciometre', DATETIME('2023-05-20 00:00:50'), 150),
  ('potenciometre', DATETIME('2023-05-20 00:00:55'), 155),
  ('potenciometre', DATETIME('2023-05-20 00:01:00'), 160),
  ('potenciometre', DATETIME('2023-05-20 00:01:05'), 165),
  ('potenciometre', DATETIME('2023-05-20 00:01:10'), 170),
  ('potenciometre', DATETIME('2023-05-20 00:01:15'), 175),
  ('potenciometre', DATETIME('2023-05-20 00:01:20'), 180),
  ('potenciometre', DATETIME('2023-05-20 00:01:25'), 185),
  ('potenciometre', DATETIME('2023-05-20 00:01:30'), 190),
  ('potenciometre', DATETIME('2023-05-20 00:01:35'), 195),
  ('potenciometre', DATETIME('2023-05-20 00:01:40'), 200),
  ('potenciometre', DATETIME('2023-05-20 00:01:45'), 205),
  ('potenciometre', DATETIME('2023-05-20 00:01:50'), 210),
  ('potenciometre', DATETIME('2023-05-20 00:01:55'), 215),
  ('potenciometre', DATETIME('2023-05-20 00:02:00'), 220),
  ('potenciometre', DATETIME('2023-05-20 00:02:05'), 225),
  ('potenciometre', DATETIME('2023-05-20 00:02:10'), 230),
  ('potenciometre', DATETIME('2023-05-20 00:02:15'), 235),
  ('potenciometre', DATETIME('2023-05-20 00:02:20'), 240),
  ('potenciometre', DATETIME('2023-05-20 00:02:25'), 245),
  ('potenciometre', DATETIME('2023-05-20 00:02:30'), 250),
  ('potenciometre', DATETIME('2023-05-20 00:02:35'), 255),
  ('potenciometre', DATETIME('2023-05-20 00:02:40'), 250),
  ('potenciometre', DATETIME('2023-05-20 00:02:45'), 245),
  ('potenciometre', DATETIME('2023-05-20 00:02:50'), 240),
  ('potenciometre', DATETIME('2023-05-20 00:02:55'), 235),
  ('potenciometre', DATETIME('2023-05-20 00:03:00'), 230),
  ('potenciometre', DATETIME('2023-05-20 00:03:05'), 225),
  ('potenciometre', DATETIME('2023-05-20 00:03:10'), 220),
  ('potenciometre', DATETIME('2023-05-20 00:03:15'), 215),
  ('potenciometre', DATETIME('2023-05-20 00:03:20'), 210),
  ('potenciometre', DATETIME('2023-05-20 00:03:25'), 205),
  ('potenciometre', DATETIME('2023-05-20 00:03:30'), 200),
  ('potenciometre', DATETIME('2023-05-20 00:03:35'), 195)
;

-- Safety trigger to prevent more than 5000 samples of one single monitor
CREATE TRIGGER max_samples AFTER INSERT ON sample
FOR EACH ROW
WHEN (SELECT COUNT(*) FROM sample WHERE monitor_key = new.monitor_key) >= 5000
BEGIN
    DELETE FROM sample WHERE id = (SELECT id FROM sample WHERE monitor_key = new.monitor_key ORDER BY date ASC LIMIT 1);
END;
