import React from 'react';
import { useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import { useHistory } from "react-router-dom"

import "./NavBar.css"

const NavBar = () => {
  const history = useHistory()
  const user = useSelector(state => state.session.user)

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
        <div className="logged-in-container">
          <li>
            <NavLink to={`/user/${userId}`} exact={true} className="profile-navlink">Profile</NavLink>
          </li>
          <li>
            <button className="create-drink-button" onClick={createRedirect}>Create a Drink/</button>
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
      {isLoggedIn()}
      {isLoggedOut()}
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
