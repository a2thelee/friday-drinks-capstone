// ************************* ACTIONS *******************************************

const GET_DRINK_INGREDIENTS = "ingredients/GET_DRINK_INGREDIENTS"

// ******************** Action Creators ***********************

const getDrinkIngredients = (drinkIngredients) => ({
  type: GET_DRINK_INGREDIENTS,
  payload: drinkIngredients
})


// ************************* THUNK ACTION CREATORS ********************************

export const getDrinkIngredientsThunk = () => async (dispatch) => {
  const response = await fetch('/api/drink_ingredients')
  if (!response.ok) {
    throw response
  }

  const drinkIngredients = await response.json()
  dispatch(getDrinkIngredients(drinkIngredients))
}


// ************************ REDUCER *********************************

const initialState = {}

const drinkIngredientsReducer = (drinkIngredients = initialState, action) => {
  switch (action.type) {
    case GET_DRINK_INGREDIENTS:

      const drinkIngredientsPayload = action.payload
      const newDrinkIngredients = {}
      for (const drinkIngredient of drinkIngredientsPayload.drinkIngredients) {
        newDrinkIngredients[drinkIngredient.id] = drinkIngredient
      }
      return newDrinkIngredients;

    default:
      return drinkIngredients
  }
}

export default drinkIngredientsReducer
