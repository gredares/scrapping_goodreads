# Scrapping Goodreads
## Le site Goodreads en quelques mots


Goodreads est la référence mondiale en matière de recommandations littéraires.

- Des millions de livres référencés, notés et commentés par les lecteurs
- Recommandations personnalisées basées sur les goûts de lecture
- Citations littéraires populaires et inspirantes
- Un réseau social pour suivre les avis et découvertes littéraires de la communauté

## Le but du projet

- Récupérer les données de chaque livre de la catégoerie "Classics" dans un fichier json (voir ci-après) :

```py
 book_details = {
        "book_title": None,
        "book_rating": None,
        "book_ratings_number": None,
        "book_reviews_number": None,
        "book_pages_number": None,
        "book_publishing_date": None,
        "author": {
            "author_name": None,
            "author_written_books_number": None,
            "author_followers_number": None
        }
```


## Les fonctions utilisées

Afin de récupérer toutes les données souhaitées, nous avons utilisé plusieurs fonctions :

- "get_all_book_links" - Pour récupérer tous les liens des livres dans une liste
- "get_book_details" - Pour récupérer toutes les informations pour chaque livre
- "date_to_epoch" - Pour convertir une date dans le format EPOCH (en secondes)
- "normalize_date" - Pour gérer les dates avec un format erroné (moins de 4 digits)
- "save_to_json" - Pour sauvegarder les données dans un fichier json
- "main" - Pour éxécuter le programme en appellant toutes les autres fonctions


## Librairies utilisées

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Librairie | Code |
| ------ | ------ |
| Requests | import requests |
| BeautifulSoup | from BS4 import BeautifulSoup |
| Datetime | import datetime |
| Typing | from typing import Dict, List, Any |

## Remerciements

Merci à Matthieu pour son aide, ses conseils, sa patience et de nous avoir enseigné le langage python pour nous permettre de réaliser ce projet. 
