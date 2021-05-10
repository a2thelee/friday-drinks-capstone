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

  useEffect(() => {
    dispatch(getIngredientsThunk())
  }, [dispatch])

  // handles submit to dispatch create drink thunk NEEDS WORK

  const handleSubmit = (e) => {
    e.preventDefault()
    dispatch(createDrinksThunk({ authorId, name, isAlcoholic, ingredients, instructions, photo }))
    history.push("/")
  }

  //handles checkbox logic for alcoholic or non-alcoholic. NEEDS WORK
  const checkAlcoholic = (e) => {
    setAlcoholic(alcoholic => !alcoholic)
  }

  //handles the user adding an image
  const addPhoto = (e) => {
    setPhoto(e.target.files[0])
  }

  //ingredient submission handler. HOLY SHIT IT WORKS!
  const ingredientSubmit = (e) => {
    e.preventDefault();
    // console.log(e.currentTarget, "current target ---------------")
    // console.log(e.currentTarget.ingredientId, "ingredientId ------------------")
    setIngredients([...ingredients, +e.currentTarget.dataset.ingredientId])
    // console.log(ingredients, "ingredients array +++++++")
    setIngredient("")
  }

  return (
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
              return item
            } else if (item.name.toLowerCase().includes(ingredient.toLowerCase())) {
              return item
            }
          }).map((ingredient) => {
            return (
              <div data-ingredient-id={ingredient.id}
                key={ingredient.id}
                className="ingredients-input-list"
                onClick={ingredientSubmit}>
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
  )

}

export default CreateDrinkForm;
