//  ****************** ACTIONS ********************************/

const GET_DRINKS = "drinks/GET_DRINKS"

const getDrinks = (drinks) => ({
  type: GET_DRINKS,
  payload: drinks
})

//*************** THUNK ACTION CREATORS ************************ */

export const getDrinksThunk = () => async (dispatch) => {
  const response = await fetch('api/drinks')
  if (!response.ok) {
    throw response
  }

  const drinks = await response.json()
  dispatch(getDrinks(drinks))
}


// ******************* Reducer ********************************/

const initialState = {}

const drinksReducer = (drinks = initialState, action) => {
  switch (action.type) {
    case GET_DRINKS:
      const drinksPayload = action.payload
      const newDrinks = {}
      for (const drink of drinksPayload.drinks) {
        newDrinks[drink.id] = drink
      }
      return newDrinks;

    default:
      return drinks;
  }
}

export default drinksReducer;
