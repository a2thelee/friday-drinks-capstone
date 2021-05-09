//  ****************** ACTIONS ********************************/

const GET_DRINKS = "drinks/GET_DRINKS"
const CREATE_DRINK = "drinks/CREATE_DRINK"

const getDrinks = (drinks) => ({
  type: GET_DRINKS,
  payload: drinks
})

const createDrink = (drink) => ({
  type: CREATE_DRINK,
  payload: drink
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

// export const createDrinksThunk = (drinkData) => async (dispatch) => {
//   const { }
// }


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
