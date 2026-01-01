Task 2: Using Python requests library to interact with an API

1. Installed the requests library:
   pip install requests

2. Wrote fetch_and_print_posts():
   - Sends a GET request to JSONPlaceholder
   - Prints status code
   - If successful, prints the title of each post

3. Wrote fetch_and_save_posts():
   - Sends the same GET request
   - Creates a list of dictionaries with id, title, and body
   - Saves this data into a CSV file using csv.DictWriter

4. Ran the main script:
   - Printed the titles of all posts
   - Created posts.csv with post data 

Example Output:
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
eum et est occaecati
nesciunt quas odio
dolorem eum magni eos aperiam quia
...
A posts.csv file is also created containing columns:
id, title, body
and each row represents a post from the API.

