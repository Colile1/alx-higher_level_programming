# 0x14. JavaScript - Web scraping

This project introduces web scraping and file operations in JavaScript using Node.js. You will learn how to read and write files, make HTTP requests, and process API responses using the `request` module.

## Project Structure

- **0-readme.js**: Reads and prints the content of a file.
- **1-writeme.js**: Writes a string to a file.
- **2-statuscode.js**: Displays the status code of a GET request to a URL.
- **3-starwars_title.js**: Prints the title of a Star Wars movie by episode number.
- **4-starwars_count.js**: Prints the number of movies where the character “Wedge Antilles” is present.
- **5-request_store.js**: Gets the contents of a webpage and stores it in a file.
- **6-completed_tasks.js**: Computes the number of completed tasks by user ID from an API.
- **100-starwars_characters.js**: Prints all characters of a Star Wars movie.
- **101-starwars_characters.js**: Prints all characters of a Star Wars movie in the order they appear in the API.
- **README.md**: This file.

## Usage

1. **Install Node.js 14.x and required modules:**
   ```sh
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
   sudo npm install semistandard request --global
   export NODE_PATH=/usr/lib/node_modules
   ```

2. **Make scripts executable:**
   ```sh
   chmod +x *.js
   ```

3. **Run scripts:**
   Each script takes arguments as described in its comments or the project instructions. For example:
   ```sh
   ./0-readme.js <file_path>
   ./1-writeme.js <file_path> <string>
   ./2-statuscode.js <URL>
   ./3-starwars_title.js <movie_id>
   ./4-starwars_count.js <API_URL>
   ./5-request_store.js <URL> <file_path>
   ./6-completed_tasks.js <API_URL>
   ./100-starwars_characters.js <movie_id>
   ./101-starwars_characters.js <movie_id>
   ```

## Notes

- All scripts are semistandard compliant.
- All scripts use `request` for HTTP requests.
- All scripts are executable and should be run with Node.js 14.x.
- See each script for specific usage and argument requirements.
