// ***************************** ACTIONS ***********************************

const GET_INGREDIENTS = "ingredients/GET_INGREDIENTS"

// ******************** Action Creators ***********************

const getIngredients = (ingredients) => ({
  type: GET_INGREDIENTS,
  payload: ingredients
})


// ************************** THUNK ACTION CREATORS **************************

export const getIngredientsThunk = () => async (dispatch) => {
  const response = await fetch('/api/ingredients/')
  if (!response.ok) {
    throw response
  }

  const ingredients = await response.json()
  dispatch(getIngredients(ingredients))
}


// ********************* REDUCER ************************************

const initialState = {}

const ingredientsReducer = (ingredients = initialState, action) => {
  switch (action.type) {
    case GET_INGREDIENTS:

      const ingredientsPayload = action.payload
      const newIngredients = {}
      for (const ingredient of ingredientsPayload.ingredients) {
        newIngredients[ingredient.id] = ingredient
      }
      return newIngredients;

    default:
      return ingredients
  }
}

export default ingredientsReducer;
