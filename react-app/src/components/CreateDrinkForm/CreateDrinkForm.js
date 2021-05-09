import { getIngredientsThunk } from "../../store/ingredients"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from "react"
import { NavLink } from "react-router-dom"

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

  console.log(ingredientsList)

  useEffect(() => {
    dispatch(getIngredientsThunk())
  }, [dispatch])

  // handles submit to dispatch create drink thunk NEEDS WORK
  const handleSubmit = (e) => {
    e.preventDefault()
    //createDrinkThunk
  }

  //handles checkbox logic for alcoholic or non-alcoholic. NEEDS WORK
  const checkAlcoholic = (e) => {
    setAlcoholic(e.target.checked)
  }

  //handles the user adding an image
  const addPhotoUrl = (e) => {
    const file = e.target.file;
    setPhotoUrl(file)
  }

  //ingredient submission handler
  let ingredientsArray = [];
  console.log("ingredients Array=================", ingredientsArray)

  const ingredientSubmit = (e) => {
    e.preventDefault();
    ingredientsArray.push(e.target.value)
    setIngredient("")
  }

  return (
    <div className="create-drink-div">
      <form onSubmit={handleSubmit} className="create-drink-form">
        <label>Drink Name:</label>
        <input type="text" value={name} onChange={e => setName(e.target.value)} />


        <label> Contains Alcohol? </label>
        <input type="checkbox" />

        <label>Drink Picture</label>
        <input type="file" onChange={addPhotoUrl} />

        <label>Ingredients</label>
        <input
          type="text"
          placeholder="Gin"
          value={ingredient}
          onChange={e => setIngredient(e.target.value)}
        />
        {ingredientsList.length ?
          ingredientsList.filter((item) => {
            if (ingredient === "") {
              return item
            } else if (item.name.toLowerCase().includes(ingredient.toLowerCase())) {
              return item
            }
          }).map((ingredient) => {
            return (
              <div key={ingredient.id} className="ingredients-input-list">
                <p onClick={e => ingredientSubmit(e)}>{ingredient.name}</p>
              </div>
            )
          }) : null}

        <label>Instructions</label>
        <textarea
          type="text"
          placeholder="measurements and directions"
          required
          value={instructions}
          onChange={e => setInstructions(e.target.value)} />
      </form>
    </div >
  )

}

export default CreateDrinkForm;
