import { getDrinksThunk } from "../../store/drinks"
// import { getFavoriteDrinksThunk } from "../../store/favorites"
// import { getIngredientsThunk } from "../../store/ingredients"
// import { getDrinkIngredientsThunk } from "../../store/drinkIngredients"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from 'react'
// import { Modal } from "../../context/Modal"
// import DrinkCard from "../drinkCard/DrinkCard"
import DrinkContainer from "../drinkContainer/DrinkContainer"

import './Home.css'

function Home() {
  const dispatch = useDispatch()
  const drinks = useSelector(state => state.drinks)
  const [loaded, setLoaded] = useState(true)
  const [drink, setDrink] = useState()
  let item;


  useEffect(() => {
    dispatch(getDrinksThunk()).then(() => {
      setLoaded(false)
    })
  }, [dispatch])

  if (loaded) {
    return <h4>Opening up the bar...</h4>
  }


  return (
    <>
      <div className="drinks-container">
        {Object.values(drinks).map(drink => {
          return (
            <DrinkContainer key={drink?.id} drink={drink} />
          )
        })}
      </div>
    </>
  )
}

export default Home
