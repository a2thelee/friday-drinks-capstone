import { getIngredientsThunk } from "../../store/ingredients"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from "react"

import "./CreateDrinkForm.css"

function CreateDrinkForm() {
  const dispatch = useDispatch()
  const userId = useSelector(state => state.session.user.id)
  const ingredientsList = Object.values(useSelector(state => state.ingredients))

  const [name, setName] = useState('')
  const [alcoholic, setAlcoholic] = useState(false)
  const [photoUrl, setPhotoUrl] = useState('')
  const [instructions, setInstructions] = useState('')
  const [ingredient, setIngredient] = useState('')

  useEffect(() => {
    dispatch(getIngredientsThunk())
  }, [dispatch])

  const handleSubmit = (e) => {
    e.preventDefault()
    //createDrinkThunk
  }

  //handles checkbox logic for alcoholic or non-alcoholic
  const checkAlcoholic = (e) => {
    setAlcoholic(e.target.checked)
  }

  //handles the user adding an image
  const addPhotoUrl = (e) => {
    const file = e.target.file;
    setPhotoUrl(file)
  }

  /*
  userId
  name (of drink)
  isAlcoholic?
  photoUrl
  instructions
  authorId

  Ingredient input fields
  */


  // Alcoholic</input>
  // Non-Alcoholic</input>

  return (
    <div className="create-drink-div">
      <form onSubmit={handleSubmit} className="create-drink-form">
        <label>Drink Name:</label>
        <input type="text" value={name} onChange={e => setName(e.target.value)} />


        <label> Contains Alcohol? </label>
        <input type="checkbox" />

        <label>Drink Picture</label>
        <input type="file" onChange={addPhotoUrl} />


      </form>
    </div>
  )

}

export default CreateDrinkForm;
