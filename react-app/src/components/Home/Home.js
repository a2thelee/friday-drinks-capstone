import { getDrinksThunk } from "../../store/drinks"
// import { getFavoriteDrinksThunk } from "../../store/favorites"
// import { getIngredientsThunk } from "../../store/ingredients"
// import { getDrinkIngredientsThunk } from "../../store/drinkIngredients"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect } from 'react'

import './Home.css'

function Home() {
  const dispatch = useDispatch()
  const drinks = useSelector(state => state.drinks)
  // const favorites = useSelector(state => state.favorites)

  useEffect(() => {
    dispatch(getDrinksThunk())
    // dispatch(getFavoriteDrinksThunk())
    // dispatch(getIngredientsThunk())
    // dispatch(getDrinkIngredientsThunk())
  }, [dispatch])

  //is a drink alcoholic?
  const drinkAlcoholic = (drink) => {
    if (drink.isAlcoholic) {
      return "Alcoholic"
    } else {
      return "Non-Alcoholic"
    }
  }

  return (
    <div className="drinks-container">
      {Object.values(drinks).map(drink => {
        return (
          <div className="single-drink-container" key={drink.id}>
            <div className="drink-photo-container">
              <img src={drink.photo_url} className="drink-photo" alt="drink-pic" />
            </div>
            <div className="drink-text-div">
              <p>{drink.name}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}

export default Home
