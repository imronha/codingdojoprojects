USE twitter;

SELECT * FROM twitter.tweets;

-- INSERT INTO twitter.tweets (tweet, user_id, created_at, updated_at) VALUES ("yay a tweet", 2, NOW(), NOW());

DELETE FROM twitter.tweets WHERE id = 16;