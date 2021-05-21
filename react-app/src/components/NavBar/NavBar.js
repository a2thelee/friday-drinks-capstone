import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useHistory } from "react-router-dom"
import { getDrinksThunk } from "../../store/drinks"
import { login } from "../../store/session"

import "./NavBar.css"

const NavBar = () => {
  const history = useHistory()
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const drinksList = Object.values(useSelector((state => state.drinks)))
  const [drink, setDrink] = useState("")
  const [searchTerm, setSearchTerm] = useState("")
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    dispatch(getDrinksThunk())
  }, [dispatch])

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
            <div className="user-profile-div">
              <NavLink to={`/user/${userId}`} exact={true} className="navbar-navlink"
                id="profile-link">{user.username}'s Bar</NavLink>
            </div>
          </div>
          <div>
            <li>
              <button className="create-drink-button" onClick={createRedirect}>Create a Drink</button>
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
              <NavLink className="navbar-navlink" to="/login" exact={true} activeClassName="active">
                Login
          </NavLink>
            </li>
            <li>
              <NavLink className="navbar-navlink" to="/sign-up" exact={true} activeClassName="active">
                Sign Up
          </NavLink>
            </li>
            <li>
              <button
                className="demo-button"
                onClick={async (e) => {
                  setEmail("demo@aa.io")
                  setPassword("password")
                  dispatch(login("demo@aa.io", "password"))
                }}>Demo User</button>
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

        <NavLink
          className="logo"
          to="/">
          Friday Drinks
          </NavLink>

        <p className="navbar-text">It's Always Friday</p>

        <div className="searchbar-div">
          <input
            className="searchBar"
            type="text"
            placeholder="Search by Drink"
            value={drink}
            onChange={e => setDrink(e.target.value)} />

          {drinksList.filter((item) => {
            if (drink === "") {
              return ""
            } else if (item?.name?.toLowerCase().includes(drink?.toLowerCase())) {
              return item
            }
          }).map((drink) => {
            return (
              <div
                key={drink.id}
                className="searchList">
                <NavLink
                  key={drink.id}
                  to={`/drinks/${drink.id}`}
                  className="search-offer"
                  onClick={() => setDrink("")}
                >
                  {drink.name}
                </NavLink>
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
