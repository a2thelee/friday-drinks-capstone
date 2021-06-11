# Friday Drinks
Friday Drinks is a fun cocktail recipe site where users can find new and old concoctions to mix and even submit their own works!

See Friday Drinks live [here](https://friday-drinks.herokuapp.com/)

## Technologies

* Backend: Python / Flask / SQLAlchemy / PostgresSQL
* Frontend: React / Redux
* Secure User Authentication using JSON Web Tokens and Bcrypt hashing
* Boto3 in conjunction with AWS for image hosting 

## Main Features

1. Smooth user interface for login/sign up flow and coctail viewing using Modals
2. Share your favorite cocktail recipes and images with others 
3. Filtered search for drinks by name using Redux State Management
4. User created cocktails are saved on a profile page, making them easier to find later! (favorites coming soon!)

## Screen Views

### Home Page
![friday-drinks-landing](https://user-images.githubusercontent.com/74819177/121685568-174cad80-ca8e-11eb-986a-88c486c3f0d5.png)

### Cocktail Modal
![friday-drinks](https://user-images.githubusercontent.com/74819177/121685696-406d3e00-ca8e-11eb-9066-0cc43766da3f.png)

### Filtered Search
![friday-drinks-search](https://user-images.githubusercontent.com/74819177/121686105-bffb0d00-ca8e-11eb-9906-e58072bfb809.png)


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
