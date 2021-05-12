import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from "react-router-dom"
import { getDrinksThunk, deleteDrinkThunk, showForm } from "../../store/drinks"

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

  const handleClick = async (id) => {
    // preventDefault()
    console.log(id, "--------------------------")
    await dispatch(deleteDrinkThunk(id))
    await dispatch(showForm({ showForm: false, key: id }))
    dispatch(getDrinksThunk())
  }

  const checkIfUserCreated = (drink) => {
    if (drink.authorId === userId) {
      return (
        <div>
          <button onClick={() => handleClick(drink.id)}>X</button>
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
