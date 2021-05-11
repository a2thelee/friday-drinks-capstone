import React, { useState, useEffect } from 'react'
import { useSelector } from 'react-redux'
import { useHistory } from "react-router-dom"

const DrinkCard = (props) => {
  const authorId = useSelector(state => state.session.user.id)
  const history = useHistory()

  const drinkAlcoholic = (drink) => {
    if (drink.isAlcoholic) {
      return "Alcoholic"
    } else {
      return "Non-Alcoholic"
    }
  }

  // const modalExit = async (e) => {
  //   e.preventDefault()
  //   history.push('/')
  //   window.close.click()
  // }


  return (
    <div
      className="drinkcard-container"
    // onClick={modalExit}
    >
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
    </div >
  )
}

export default DrinkCard
