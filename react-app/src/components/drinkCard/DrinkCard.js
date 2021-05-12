import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from "react-router-dom"
import { deleteDrinkThunk } from "../../store/drinks"

import "./DrinkCard.css"

const DrinkCard = (props) => {
  const userId = useSelector(state => state.session.user.id)
  const dispatch = useDispatch()
  const history = useHistory()

  const drinkAlcoholic = (drink) => {
    if (drink.isAlcoholic) {
      return "Alcoholic"
    } else {
      return "Non-Alcoholic"
    }
  }

  const deleteDrink = (e) => {
    e.preventDefault()
    history.push("/")
    dispatch(deleteDrinkThunk(e.target.id))
  }

  const checkIfUserCreated = (drink) => {
    if (drink.authorId === userId) {
      return (
        <div>
          <button onClick={deleteDrink}>X</button>
        </div>
      )
    }
  }

  return (

    <div
      className="drinkcard-container"
    >
      < div className="drinkcard-photo-container" >
        <img
          src={props.drink.photo_url}
          className="drinkcard-photo"
          alt="drink-pic"
        />
      </div >

      <div className="drinkcard-name-div">
        <p>{props.drink.name}</p>
        <p># of Favorites: {props.drink.favorites}</p>
      </div>

      <div className="drinkcard-contains-alcohol">
        <p>{drinkAlcoholic(props.drink)}</p>
      </div>

      <div className="drinkcard-ingredients">
        {console.log(props.drink.ingredient)}
        {props.drink.ingredients}
      </div>

      <div className="drinkcard-instructions">
        {props.drink.instructions}
      </div>

      {checkIfUserCreated(props.drink)}
    </div >

  )
}

export default DrinkCard
