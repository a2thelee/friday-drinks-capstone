import React, { useState, useEffect } from 'react';
import { getOneDrinkThunk } from "../../store/drinks"
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from 'react-router-dom'

import "./SingleDrinkPage.css"

const SingleDrinkPage = () => {
  const dispatch = useDispatch()
  const { id } = useParams()
  const drink = useSelector(state => state.drinks)
  console.log(drink, "heloooooooooooooooooooo")

  useEffect(() => {
    dispatch(getOneDrinkThunk(id))
  }, [dispatch])

  return (
    <div className="searched-drink-container">
      <div className="searched-drink-photo">
        <img
          src={drink.photo_url}
          className="searched-drink-photo"
          alt="you got me" />
      </div>

      <div className="searched-drink-name">
        <p>Drink Name: <strong>{drink.name}</strong></p>
      </div>

      <div className="searched-drink-alcoholic">
        <p>Alcoholic/Non-Alcoholic? <strong>{drink.isAlcoholic}</strong></p>
      </div>

      <div className="searched-drink-instructions">
        <label><strong>Instructions</strong></label>
        <br></br>
        {drink.instructions}
      </div>
    </div>
  )
}

export default SingleDrinkPage
