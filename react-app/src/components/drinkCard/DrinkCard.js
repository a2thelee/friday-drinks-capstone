//this is modal component

import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from "react-router-dom"
import { getDrinksThunk, deleteDrinkThunk, showForm } from "../../store/drinks"
import { makeFavoriteThunk, unFavoriteThunk } from "../../store/session"



import "./DrinkCard.css"

const DrinkCard = (props) => {
  const userId = useSelector(state => state.session.user?.id)
  const dispatch = useDispatch()
  const history = useHistory()
  const isFavorite = useSelector(state => state?.session?.user?.favorites[props.drink.id]) //destructure props on line 10 to make easier keeying to
  const drinkId = props.drink.id

  const ingredients = props.drink.ingredients


  const siftedIngredients = ingredients.map((ingredient) => {
    return ingredient.name
  })

  const drinkAlcoholic = (drink) => {
    if (drink.isAlcoholic) {
      return "Alcoholic"
    } else {
      return "Non-Alcoholic"
    }
  }

  const handleClick = async (id) => {
    // preventDefault()
    await dispatch(deleteDrinkThunk(id))
    await dispatch(showForm({ showForm: false, key: id }))
    dispatch(getDrinksThunk())
  }

  const checkIfUserCreated = (drink) => {
    if (drink.authorId === userId) {
      return (
        <div>
          <button class="drink-delete-button" onClick={() => handleClick(drink.id)}>X</button>
        </div>
      )
    }
  }

  const isFavorited = () => {
    if (userId) {
      if (!isFavorite) {
        return (
          <i class="far fa-heart" onClick={() => dispatch(makeFavoriteThunk(drinkId))} />
        )
      } else {
        return (
          <i class="fas fa-heart" onClick={() => dispatch(unFavoriteThunk(isFavorite.id, drinkId))} />
        )
      }
    }
  }

  return (

    <div
      className="drinkcard-container"
    >
      <div className="div1">
        <div className="drinkcard-photo-container" >
          <img
            src={props.drink.photo_url}
            className="drinkcard-photo"
            alt="drink-pic"
          />
        </div >
      </div>

      <div className="div2">
        <div className="drinkcard-name-div">
          <p>Drink Name: <strong>{props.drink.name}</strong></p>
          <p># of Favorites: <strong>{props.drink.number_of_favorites}</strong> </p>
        </div>

        <div className="drinkcard-contains-alcohol">
          <p>Alcoholic/Non-Alcoholic? <strong>{drinkAlcoholic(props.drink)}</strong></p>
        </div>

        <div className="drinkcard-ingredients">
          <p>Ingredients: <strong>{siftedIngredients.join(", ")}</strong></p>
        </div>

        <div className="drinkcard-instructions">
          <label><strong>Instructions</strong></label>
          <br></br>
          {props.drink.instructions}
        </div>


        {/* this is the heart, styling rules are the same as text in css <i class="fas fa-heart"> is filled heart*/}
        {isFavorited()}

        {checkIfUserCreated(props.drink)}
      </div>
    </div >

  )
}

export default DrinkCard
