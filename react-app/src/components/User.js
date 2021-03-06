import React, { useState, useEffect } from "react";
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from "react-router-dom";
import { getDrinksThunk } from "../store/drinks"
import DrinkContainer from "./drinkContainer/DrinkContainer"

//any css here would be done in Home.css or related drinkcontainer/drinkcard

function User() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(true)
  const [user, setUser] = useState({});
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId } = useParams();
  const drinks = useSelector(state => state.drinks)
  const userCreatedDrinks = Object.values(drinks).filter(drink => drink?.authorId === Number(userId))
  const favorites = Object.values(useSelector(state => state.session.user.favorites))


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

      <p className="user-label"><strong>Your Created Drinks</strong></p>
      <div className="drinks-container">
        {userCreatedDrinks.map(drink => {
          return (
            <DrinkContainer key={drink?.id} drink={drink} />
          )
        })}
      </div>

      <p className="user-label"><strong>Your Favorite Cocktails</strong></p>
      <div className="drinks-container">
        {favorites.map(favorite => {
          return (
            <DrinkContainer key={favorite.drinkId} drink={drinks[favorite.drinkId]} />
          )
        })}
      </div>

    </div>
  );
}
export default User;
