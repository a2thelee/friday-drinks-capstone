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

  return (
    <div className="create-drink-div">
      <form onSubmit={handleSubmit} className="create-drink-form">
        <label>Drink Name:
          <input type="text" value={name} onChange={e => setName(e.target.value)} />
        </label>

        <label>Alcoholic or Non-Alcoholic?
          <input type="checkbox">Alcoholic</input>
          <input type="checkbox">Non-Alcoholic</input>
        </label>

        <label>Drink Picture
          <input type="file" onChange={addPhotoUrl} />
        </label>

      </form>
    </div>
  )

}
