import { getDrinksThunk } from "../../store/drinks"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from 'react'

import './Home.css'

function Home() {
  const dispatch = useDispatch()
  const drinks = useSelector(state => state.drinks)

  useEffect(() => {
    dispatch(getDrinksThunk())
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
              <img src={drink.photo_url} className="drink-photo" />
            </div>
            <div className="drink-text-div">
              <p>{drink.name}</p>
              <p>{drinkAlcoholic(drink)}</p>
              <p>{drink.instructions}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}

export default Home
