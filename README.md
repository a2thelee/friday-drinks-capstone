# Friday Drinks
Friday Drinks is a fun cocktail recipe site where users can find new and old concoctions to mix and even submit their own works!

See Friday Drinks live [here](https://friday-drinks.herokuapp.com/)

## Technologies

* Backend: Python / Flask / SQLAlchemy / PostgresSQL
* Frontend: JavaScript / React / Redux / CSS3 / HTML5
* Boto3 in conjunction with AWS for image hosting 

## Main Features

1. Smooth user interface for login/sign up flow and coctail viewing using Modals
2. Cocktail creation featuring a list of over 500 ingredients and user image uploads using AWS!
3. Users can "favorite" cocktails in order to save them for easier lookup!
4. Filtered search for drinks by name using Redux Library!
5. User profile page to store user-created and favorite cocktails!

## Recent Additions/ Currently Implementing

1. Favorites (Added June 30 2021)
2. Modal Design (Redesigned July 5, 2021)
3. Currently focusing on making page more responsive every day!

## Screen Views

### Home Page
![friday-drinks-landing](https://user-images.githubusercontent.com/74819177/126399358-cda89c5f-ed2b-4bf0-aed7-0f93965adfba.png)

### Cocktail Modal
![friday-drinks](https://user-images.githubusercontent.com/74819177/126399245-fead4852-9a3e-4ed9-9473-4a9f6d2e24e1.png)

### Profile
![friday-drinks-profile](https://user-images.githubusercontent.com/74819177/126399406-1d11b2a5-5302-4b76-a226-02b575f64118.png)

### Filtered Search/Search Result
![friday-drinks-search](https://user-images.githubusercontent.com/74819177/126399816-75c2ceea-a0b0-448d-9373-72a2c55ce226.png)

## Special Thanks to [TheCocktailDB.com](https://www.thecocktaildb.com/) for helping make this happen!

# Flask React Project

This is the backend for the Flask React project.

## Getting started

1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/appacademy-starters/python-project-starter.git
   ```

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

***
*IMPORTANT!*
   If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
   You can do this by running:

   ```bash
   pipenv lock -r > requirements.txt
   ```

*ALSO IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on apline-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***
