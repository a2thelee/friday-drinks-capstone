// ************************ ACTIONS *******************************

const GET_FAVORITES = "favorites/GET_FAVORITES"

const getFavorites = (favorites) => ({
  type: GET_FAVORITES,
  payload: favorites
})

// ********************** THUNK ACTION CREATORS *******************

export const getFavoriteDrinksThunk = () => async (dispatch) => {
  const response = await fetch('/api/favorite_drinks')
  if (!response.ok) {
    throw response
  }

  const favorites = await response.json()
  dispatch(getFavorites(favorites))
}


// ***************** REDUCER *************************************

const initialState = {}

const favoritesReducer = (favorites = initialState, action) => {
  switch (action.type) {
    case GET_FAVORITES:

      const favoritesPayload = action.payload
      const newFavorites = {}
      for (const favorite of favoritesPayload.favorites) {
        newFavorites[favorite.id] = favorite
      }
      return newFavorites;

    default:
      return favorites
  }
}

export default favoritesReducer;
