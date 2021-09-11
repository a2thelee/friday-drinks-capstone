// home page which essentially the container that maps through all drinks and renders a drinkcontainer tile for each drink.

import { getDrinksThunk } from "../../store/drinks"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from 'react'
import DrinkContainer from "../drinkContainer/DrinkContainer"

import './Home.css'

function Home() {
  const dispatch = useDispatch()
  const drinks = useSelector(state => state.drinks)
  const [loaded, setLoaded] = useState(true)


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
