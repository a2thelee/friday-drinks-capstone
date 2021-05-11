import React, { useState, useEffect } from 'react'
import { useSelector } from 'react-redux'

const DrinkCard = (props) => {

  const drinkAlcoholic = (drink) => {
    if (drink.isAlcoholic) {
      return "Alcoholic"
    } else {
      return "Non-Alcoholic"
    }
  }
  return (
    <div className="drinkcard-container">
      <div className="drinkcard-photo-container">
        <img
          src={props.drink.photo_url}
          className="drinkcard-photo"
          alt="drink-pic"
        />
      </div>

      <div className="drinkcard-name-div">
        <p>{props.drink.name}</p>
        <p># of Favorites: {props.drink.favorites}</p>
      </div>

      <div className="drinkcard-contains-alcohol">
        <p>{drinkAlcoholic(props.drink)}</p>
      </div>

      <div className="drinkcard-ingredients">
        {props.drink.ingredients}
      </div>

      <div className="drinkcard-instructions">
        {props.drink.instructions}
      </div>
    </div>
  )
}

export default DrinkCard
