from wordcloud import STOPWORDS
start = '2021-01-01T00:00:00Z'
end = '2021-08-31T23:59:59Z'
path = "./results/"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAARjOQEAAAAAAOHOH0bomcK5DtKssC42ATS2SQQ%3Drg2Q619LihIqClg9dKQxnQlJSoxtmLXoNZwEsBYU8cwwfTH3Eu' #os.environ.get("BEARER_TOKEN")
search_url = "https://api.twitter.com/2/tweets/search/all"
query = 'lang:pt -is:retweet ("Unidade de conservação" OR "Area protegida" OR "Parque Nacional" OR "Parque estadual" OR "Parque natural municipal" OR "Parque municipal" OR "Estação ecológica" OR "Reserva biológica" OR "Monumento natural" OR "Refúgio da vida silvestre" OR "Reserva extrativista" OR "Área de proteção ambiental" OR "Floresta nacional" OR "Floresta estadual" OR "Floresta municipal" OR "Reserva de desenvolvimento sustentável" OR "Área de relevante interesse" OR "Reserva Particular do Patrimônio Natural")'
tweet_fields = 'author_id,created_at,geo,id,in_reply_to_user_id,public_metrics'
user_fields = 'name,username,verified'
expansions = 'geo.place_id,entities.mentions.username,author_id'
place_fields = 'country,country_code,place_type'
max_results = '500'
stopwords = set(STOPWORDS)
stopwords.update(["https", "Unidade de conservação", "Area protegida",
                  "Parque Nacional", "Estação ecológica", "Reserva biológica",
                  "Monumento natural", "Refúgio da vida silvestre",
                  "Reserva extrativista", "Área de proteção ambiental",
                  "Floresta nacional", "Reserva de desenvolvimento sustentável",
                  "Área de relevante interesse", "Reserva Particular do Patrimônio Natural",
                  "do", "de", "da", "para", "e", "t", "co", "uma", "o", "a", "pra",
                  "para", "um", "dos", "das", "é"])