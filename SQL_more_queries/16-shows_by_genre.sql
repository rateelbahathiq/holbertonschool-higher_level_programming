-- Lists all TV shows and all genres linked to each show, including NULL if no genre exists
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
