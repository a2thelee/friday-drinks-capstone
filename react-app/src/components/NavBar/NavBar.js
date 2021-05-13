import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux'
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { getDrinksThunk } from "../../store/drinks"

import "./NavBar.css"

const NavBar = () => {
  const history = useHistory()
  const user = useSelector(state => state.session.user)
  const [drink, setDrink] = useState("")

  const drinksList = Object.values(useSelector(state => state.drinks))

  const createRedirect = () => {
    history.push("/create_drinks")
  }

  const handleSubmit = (e) => {
    setDrink("")
  }

  let userId;

  if (user) {
    userId = user.id;
  }

  function isLoggedIn() {
    if (user) {
      return (
        <div className="logged-in-container">
          <li>
            <NavLink to={`/user/${userId}`} exact={true} className="profile-navlink">Profile</NavLink>
          </li>
          <li>
            <button className="create-drink-button" onClick={() => createRedirect()}>Create a Drink/</button>
          </li>
          <li>
            <LogoutButton />
          </li>
        </div>
      )
    }
  }

  function isLoggedOut() {
    if (!user) {
      return (
        <div className="logged-out-container">
          <li>
            <NavLink to="/login" exact={true} activeClassName="active">
              Login
          </NavLink>
          </li>
          <li>
            <NavLink to="/sign-up" exact={true} activeClassName="active">
              Sign Up
          </NavLink>
          </li>

        </div>
      )
    }
  }


  return (
    <nav>
      <div>
        <NavLink to="/">Friday Drinks</NavLink>
      </div>
      {isLoggedIn()}
      {isLoggedOut()}
      <div className="searchBarContainer">
        <form className="searchBar" onSubmit={(e) => handleSubmit(e)}>
          <input
            value={drink}
            type="text"
            placeholder="Look for a Drink"
            onChange={(e) => setDrink(e.target.value)}
          />
        </form>
      </div>
    </nav>
  );
}

export default NavBar;


{/* <div className="searchBarContainer">
          <li>
            <form className="searchBar" onSubmit={(e) => handleSubmit(e)}>
              <input
                value={location}
                type="text"
                placeholder="Search by State..."
                onChange={(e) => setLocation(e.target.value)}
              />
              {uniqueArray.length ?
                uniqueArray.map((val, key) => {
                  console.log('UArray', uniqueArray)
                  return (
                    <div className="searchedList" key={key}>
                      <NavLink to={{
                        pathname: "/searchResults",
                        state: {
                          val: val
                        },
                      }} onClick={e => handleSubmit(e)}>
                        {val}
                      </NavLink>
                    </div>
                  )
                })
                : null}
            </form>
          </li>
        </div>
        {hideLoginSignUp()}
        <div className="isLoggedIn">
          {isLoggedIn()}
        </div> */}


        // ingredientsList.filter((item) => {
        //     if (ingredient === "") {
        //       return item
        //     } else if (item.name.toLowerCase().includes(ingredient.toLowerCase())) {
        //       return item
        //     }
        //   }).map((ingredient) => {
        //     return (
        //       <div data-ingredient-id={ingredient.id}
        //         key={ingredient.id}
        //         className="ingredients-input-list"
        //         onClick={ingredientSubmit}>
        //         <p>{ingredient.name}</p>
        //       </div>
        //     )
        //   })}
        // </div>
