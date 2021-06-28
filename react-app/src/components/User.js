import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from "react-router-dom";
import { getDrinksThunk, getOneDrinkThunk } from "../store/drinks"
import DrinkContainer from "./drinkContainer/DrinkContainer"

//any css here would be done in Home.css or related drinkcontainer/drinkcard

function User() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(true)
  const [user, setUser] = useState({});
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId } = useParams();
  const drinks = Object.values(useSelector(state => state.drinks))
  const userCreatedDrinks = drinks.filter(drink => drink?.authorId === Number(userId))
  const favorites = Object.values(useSelector(state => state.session.user.favorites))
  const favoriteIds = favorites.map(favorite => favorite.drinkId)

  console.log(favoriteIds, "----------------------this should be favoriteIds")

  // console.log(dispatch(getOneDrinkThunk(1)), "this is the dispatch for getonedrink")

  const renderFavorites = async (id) => {
    await dispatch(getOneDrinkThunk(id))
  }

  useEffect(() => {
    if (!userId) {
      return
    }
    (async () => {
      const response = await fetch(`/api/users/${userId}`);
      const user = await response.json();
      setUser(user);
    })();
  }, [userId]);

  useEffect(() => {
    dispatch(getDrinksThunk()).then(() => {
      setLoaded(false)
    })
  }, [dispatch])

  if (loaded) {
    return <h4>Opening up the bar...</h4>
  }

  if (!user) {
    return null;
  }

  return (
    <div>
      <ul>
        <li>
          <strong>Username:</strong> {user.username}
        </li>
        <li>
          <strong>Email:</strong> {user.email}
        </li>
      </ul>

      <p className="user-label"><strong>Your Created Drinks</strong></p>
      <div className="drinks-container">
        {userCreatedDrinks.map(drink => {
          return (
            <DrinkContainer key={drink?.id} drink={drink} />
          )
        })}
      </div>

      <p className="user-label"><strong>Your Favorite Cocktails! (coming soon)</strong></p>
      <div className="favorites-container">
        {favoriteIds.map(favorite => {
          return (
            console.log(favorite)
          )
        })}
      </div>

    </div>
  );
}
export default User;
