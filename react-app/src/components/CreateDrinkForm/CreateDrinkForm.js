import { getIngredientsThunk } from "../../store/ingredients"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"
import React, { useEffect, useState } from "react"
import { createDrinksThunk } from "../../store/drinks"

import "./CreateDrinkForm.css"

function CreateDrinkForm() {
  const dispatch = useDispatch()
  const history = useHistory()
  const authorId = useSelector(state => state.session.user.id)
  const ingredientsList = Object.values(useSelector(state => state.ingredients))
  const [name, setName] = useState('')
  const [photo, setPhoto] = useState('')
  const [instructions, setInstructions] = useState('')
  const [ingredient, setIngredient] = useState('')
  const [isAlcoholic, setAlcoholic] = useState(false)

  //an array to keep track of submitted ingredients since we are only using one input
  const [ingredients, setIngredients] = useState([])
  const [ingredientNames, setIngredientNames] = useState([])

  useEffect(() => {
    dispatch(getIngredientsThunk())
  }, [dispatch])

  // handles submit to dispatch create drink thunk

  const handleSubmit = async (e) => {
    e.preventDefault()
    // const response = dispatch(createDrinksThunk({ authorId, name, isAlcoholic, ingredients, instructions, photo }))
    await dispatch(createDrinksThunk({ authorId, name, isAlcoholic, ingredients, instructions, photo }))
    history.push(`/users/${authorId}`)

    // if (response.ok) {
    //   history.push(`/users/${authorId}`)
    // } else {
    //   window.alert("Pleae fill out the fields")
    // }
  }

  //handles checkbox logic for alcoholic or non-alcoholic
  const checkAlcoholic = (e) => {
    setAlcoholic(alcoholic => !alcoholic)
  }

  //handles the user adding an image
  const addPhoto = (e) => {
    setPhoto(e.target.files[0])
  }

  //ingredient submission handler. sends ingredient IDs to thunk to make querying easier on the back end. WORKS!
  const ingredientSubmit = (e, ingredient) => {
    if (!ingredients.includes(ingredient.id)) {
      ingredientNames.push(ingredient)
      setIngredients([...ingredients, +e.currentTarget.dataset.ingredientId])
      setIngredient("")
    } else {
      window.alert("Ingredient Already Added!")
    }
  }

  // const ingredientSubmit = (e, ingredient) => {
  //   ingredientNames.push(ingredient)
  //   setIngredients([...ingredients, +e.currentTarget.dataset.ingredientId])
  //   setIngredient("")
  // }

  // const displayIngredients = (e) => {
  //   setIngredientNames([...ingredient])
  // }

  return (
    <>
      <div className="user-ingredients-list">
        <p className="active-ingredients-label"><strong>Active Ingredients</strong></p>
        {ingredientNames.map(ingredient => {
          return (
            <p className="active-ingredients-list" key={ingredient.id}>{ingredient.name}</p>
          )
        })}
      </div>
      <div className="create-drink-div">
        <form onSubmit={handleSubmit} className="create-drink-form">
          <div className="drink-name-div">
            <label>Drink Name:</label>
            <input
              type="text"
              value={name}
              onChange={e => setName(e.target.value)}
            />
          </div>

          <div className="checkbox-div">
            <label> Contains Alcohol? </label>
            <input
              type="checkbox"
              checked={isAlcoholic}
              onChange={checkAlcoholic}
            />
          </div>

          <div className="drink-picture-div">
            <label>Drink Picture</label>
            <input
              type="file"
              onChange={addPhoto}
            />
          </div>

          <div className="ingredients-input-div">
            <label>Ingredients</label>
            <input
              type="text"
              placeholder="Gin"
              value={ingredient}
              onChange={e => setIngredient(e.target.value)}
            />

            {ingredientsList.filter((item) => {
              if (ingredient === "") {
                return ""
              } else if (item.name.toLowerCase().includes(ingredient.toLowerCase())) {
                return item
              }
            }).map((ingredient) => {
              return (
                <div data-ingredient-id={ingredient.id}
                  key={ingredient.id}
                  className="ingredients-input-list"
                  onClick={(e) => ingredientSubmit(e, ingredient)}>
                  <p>{ingredient.name}</p>
                </div>
              )
            })}
          </div>

          <div className="instructions-div">
            <label>Instructions</label>
            <textarea
              type="text"
              placeholder="measurements and directions"
              required
              value={instructions}
              onChange={e => setInstructions(e.target.value)} />
          </div>
        </form>
        <button type="submit" onClick={handleSubmit}>Submit</button>
      </div >
    </>
  )

}

export default CreateDrinkForm;
