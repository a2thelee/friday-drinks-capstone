//  ****************** ACTIONS ********************************/

const GET_DRINKS = "drinks/GET_DRINKS"
const GET_ONE_DRINK = "drinks/GET_ONE_DRINK"
const CREATE_DRINK = "drinks/CREATE_DRINK"
const DELETE_DRINK = "drinks/DELETE_DRINK"
const SHOW_FORM = "drinks/SHOW_FORM"

const getDrinks = (drinks) => ({
  type: GET_DRINKS,
  payload: drinks
})

const createDrink = (drink) => ({
  type: CREATE_DRINK,
  payload: drink
})

const deleteDrink = () => ({
  type: DELETE_DRINK
})

const getOneDrink = (drink) => ({
  type: GET_ONE_DRINK,
  payload: drink
})

export const showForm = (visibility) => ({
  type: SHOW_FORM,
  payload: visibility
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


// Makes 2 fetch calls. 1 to the back end to upload photo file to AWS bucket and receives back a photo url. second fetch takes that photo url and sends it to back end with the rest of the form data.
export const createDrinksThunk = (drinkData) => async (dispatch) => {
  const { authorId, name, isAlcoholic, instructions, photo, ingredients } = drinkData

  const body = new FormData();

  body.append("photo", photo)
  const imageRes = await fetch('/api/drinks/photo', {
    method: "POST",
    // headers: {
    //   'Content-Type': 'multipart/form-data'
    // },
    body
  });
  const { photo_url } = await imageRes.json()

  const response = await fetch('/api/drinks/create', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      authorId,
      name,
      isAlcoholic,
      instructions,
      photo_url,
      ingredients
    })
  })
  const newDrink = await response.json()
  dispatch(createDrink(newDrink))
  return newDrink
}

// delete drink thunk
export const deleteDrinkThunk = (id) => async (dispatch) => {
  const response = await fetch(`/api/drinks/${id}`, { method: "DELETE" })

  dispatch(deleteDrink())
  return null;
}

// get one drink thunk
export const getOneDrinkThunk = (id) => async (dispatch) => {
  const response = await fetch(`/api/drinks/${id}`)
  if (!response.ok) {
    throw response
  }

  const drink = await response.json()
  dispatch(getOneDrink(drink))
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

    case GET_ONE_DRINK:
      const drinkPayload = action.payload
      return drinkPayload

    case CREATE_DRINK:
      return { ...drinks, [action.payload.id]: action.payload }

    case DELETE_DRINK:
      return drinks;

    case SHOW_FORM:
      drinks[action.payload.key].show = action.payload.showForm
      return { ...drinks }

    default:
      return drinks
  }
}

export default drinksReducer;
