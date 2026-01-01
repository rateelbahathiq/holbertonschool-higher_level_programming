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
Status Code: 200 <br>
sunt aut facere repellat provident occaecati excepturi optio reprehenderit <br>
qui est esse <br>
ea molestias quasi exercitationem repellat qui ipsa sit aut<br>
eum et est occaecati<br>
nesciunt quas odio<br>
dolorem eum magni eos aperiam quia<br>
... <br>
A posts.csv file is also created containing columns:<br>
id, title, body

 
Task 3: Building a simple web API using Python http.server

1. Created a basic HTTP server using the http.server module.

2. Wrote a request handler class:
   - Subclassed BaseHTTPRequestHandler
   - Implemented the do_GET() method to handle GET requests

3. Handled multiple endpoints:
   - `/` returns plain text: "Hello, this is a simple API!"
   - `/data` returns JSON data: {"name": "John", "age": 30, "city": "New York"}
   - `/status` returns JSON: {"status": "OK"}
   - `/info` returns JSON with version and description
   - Any other path returns a 404 error with message: {"error": "Endpoint not found"}

4. Ran the server:
   - Server started at http://localhost:8000
   - Tested all endpoints using curl from a second terminal


Example Output:
curl http://localhost:8000/
Hello, this is a simple API!

curl http://localhost:8000/data
{"name": "John", "age": 30, "city": "New York"}

curl http://localhost:8000/status
{"status": "OK"}

curl http://localhost:8000/info
{"version": "1.0", "description": "A simple API built with http.server"}

curl http://localhost:8000/unknown
{"error": "Endpoint not found"}

