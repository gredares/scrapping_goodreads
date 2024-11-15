import requests
from module import (
    get_book_details,
    get_all_book_links,
    save_to_json
)

def main():
    all_books_data = [] 
    total_pages = 25

    # Get all book links
    all_book_links = get_all_book_links(total_pages)

    for i, book_link in enumerate(all_book_links, 1):
        print(f"Processing book {i}/{len(all_book_links)}: {book_link}")
        book_details = get_book_details(book_link)
        if book_details:
            all_books_data.append(book_details)

    # Save the data to a JSON file
    save_to_json(all_books_data, "goodreads_books.json")
    print(f"\nSaved data for {len(all_books_data)} books to goodreads_books.json")

if __name__ == "__main__":
    main() 
    
    