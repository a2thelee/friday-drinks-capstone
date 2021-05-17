import React, { useState, useEffect } from 'react';
import { getDrinksThunk } from "../../store/drinks"
import { useSelector, useDispatch } from 'react-redux'
import { useParams } from 'react-router-dom'

import "./SingleDrinkPage.css"

const SingleDrinkPage = () => {
  const dispatch = useDispatch()
  const { id } = useParams()
  const drinks = useSelector(state => state.drinks)


  useEffect(() => {
    dispatch(getDrinksThunk())
  }, [dispatch])

  if (!drinks[id]) return null;

  return (
    <div className="searched-drink-container">
      <div className="searched-drink-photo">
        <img
          src={drinks[id].photo_url}
          className="searched-drink-photo"
          alt="you got me" />
      </div>

      <div className="searched-drink-name">
        <p>Drink Name: <strong>{drinks[id].name}</strong></p>
      </div>

      <div className="searched-drink-alcoholic">
        <p>Alcoholic/Non-Alcoholic? <strong>{drinks[id].isAlcoholic}</strong></p>
      </div>

      <div className="searched-drink-instructions">
        <label><strong>Instructions</strong></label>
        <br></br>
        {drinks[id].instructions}
      </div>
    </div>
  )
}

export default SingleDrinkPage
