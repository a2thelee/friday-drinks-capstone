import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useHistory } from "react-router-dom"
import { getDrinksThunk } from "../../store/drinks"

import "./NavBar.css"

const NavBar = () => {
  const history = useHistory()
  const user = useSelector(state => state.session.user)
  const drinksList = Object.values(state => state.drinks)
  const dispatch = useDispatch()
  const [drink, setDrink] = useState("")

  useEffect(() => {
    dispatch(getDrinksThunk())
  }, [dispatch])

  console.log(drinksList, "drinkslist -----------------------")

  const createRedirect = () => {
    history.push("/create_drinks")
  }

  let userId;

  if (user) {
    userId = user.id;
  }

  function isLoggedIn() {
    if (user) {
      return (
        <>
          <div className="logged-in-container">
            <li>
              <NavLink to={`/user/${userId}`} exact={true} className="profile-navlink">Profile</NavLink>
            </li>
          </div>
          <div>
            <li>
              <button className="create-drink-button" onClick={createRedirect}>Create a Drink/</button>
            </li>
          </div>
          <div>
            <li>
              <LogoutButton />
            </li>
          </div>
        </>
      )
    }
  }

  function isLoggedOut() {
    if (!user) {
      return (
        <>
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
        </>
      )
    }
  }


  return (
    <nav>
      <div className="navbar-container">
        {isLoggedIn()}
        {isLoggedOut()}

        <NavLink to="/">Friday Drinks</NavLink>

        <div>
          <input
            type="text"
            placeholder="Search by Drink"
            value={drink}
            onChange={e => setDrink(e.target.value)} />

          {drinksList.filter((item) => {
            if (drink === "") {
              return ""
            } else if (item.name.toLowerCase().includes(drink.toLowerCase())) {
              return item
            }
          }).map((drink) => {
            return (
              <div
                key={drink.id}
                className="drinks-input-list">
                <p>{drink.name}</p>
              </div>
            )
          })}
        </div>

      </div>
    </nav>
  );
}

export default NavBar;


// <ul className="NavBar-div">
//   <li>
//     <NavLink to="/" exact={true} activeClassName="active">
//       Home
//           </NavLink>
//   </li>
//   <li>
//     <NavLink to="/login" exact={true} activeClassName="active">
//       Login
//           </NavLink>
//   </li>
//   <li>
//     <NavLink to="/sign-up" exact={true} activeClassName="active">
//       Sign Up
//           </NavLink>
//   </li>
//   <li>
//     <NavLink to="/users" exact={true} activeClassName="active">
//       Users
//           </NavLink>
//   </li>
//   <li>
//     <LogoutButton />
//   </li>
// </ul>
