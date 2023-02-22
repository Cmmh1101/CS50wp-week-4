# Technologies/languages

This is a Django/Python project for the program CS50 Web Programming week 4

# To start this project:

- clone the repo
- Run in the project terminal (I added 3 because is the version I'm currently using): python3 manage.py runserver

# CS50 specifications:

- **Entry Page:** Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.

  - The view should get the content of the encyclopedia entry by calling the appropriate util function.
  - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
  - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

- **Index Page:** Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.

- **Search:** Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.

    - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.

    - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.

    - Clicking on any of the entry names on the search results page should take the user to that entry’s page.