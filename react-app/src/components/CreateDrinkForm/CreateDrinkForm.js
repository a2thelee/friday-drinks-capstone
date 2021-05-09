import { getIngredientsThunk } from "../../store/ingredients"
import { useDispatch, useSelector } from "react-redux"
import React, { useEffect, useState } from "react"
import { NavLink } from "react-router-dom"

import "./CreateDrinkForm.css"

function CreateDrinkForm() {
  const dispatch = useDispatch()
  const authorId = useSelector(state => state.session.user.id)
  const ingredientsList = Object.values(useSelector(state => state.ingredients))

  const [name, setName] = useState('')
  const [alcoholic, setAlcoholic] = useState(false)
  const [photoUrl, setPhotoUrl] = useState('')
  const [instructions, setInstructions] = useState('')
  const [ingredient, setIngredient] = useState('')

  //an array to keep track of submitted ingredients since we are only using one input
  const [ingredients, setIngredients] = useState([])

  useEffect(() => {
    dispatch(getIngredientsThunk())
  }, [dispatch])

  // handles submit to dispatch create drink thunk NEEDS WORK

  const handleSubmit = (e) => {
    e.preventDefault()

  }
  // const handleSubmit = (e) => {
  //   e.preventDefault()
  //   createDrink(authorId, name, ISALCOHOLIC, instructions, photo_url, ingredients)
  //   history.push("/")
  // }

  //handles checkbox logic for alcoholic or non-alcoholic. NEEDS WORK
  const checkAlcoholic = (e) => {
    setAlcoholic(e.target.checked)
  }

  //handles the user adding an image
  const addPhotoUrl = (e) => {
    setPhotoUrl(e.target.files.item(0))
  }

  //ingredient submission handler. HOLY SHIT IT WORKS!
  console.log("ingredients array please fucking work", ingredients)
  console.log("these are instructions, the should work", instructions)
  const ingredientSubmit = (e) => {
    e.preventDefault();
    setIngredients([...ingredients, ingredient])
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
        {ingredientsList.filter((item) => {
          if (ingredient === "") {
            return item
          } else if (item.name.toLowerCase().includes(ingredient.toLowerCase())) {
            return item
          }
        }).map((ingredient) => {
          return (
            <div key={ingredient.id} className="ingredients-input-list">
              <p onClick={ingredientSubmit}>{ingredient.name}</p>
            </div>
          )
        })}

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
