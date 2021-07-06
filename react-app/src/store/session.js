import { favoriteDrink } from "./drinks"

// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const MAKE_FAVORITE = "session/MAKE_FAVORITE";
const UN_FAVORITE = "session/UN_FAVORITE";

const setUser = (user) => ({
    type: SET_USER,
    payload: user
})

const removeUser = () => ({
    type: REMOVE_USER
})

const makeFavorite = (favorite) => ({
    type: MAKE_FAVORITE,
    payload: favorite
})

const unFavorite = (favorite) => ({
    type: UN_FAVORITE,
    payload: favorite
})

// thunks
export const makeFavoriteThunk = (drinkId) => async (dispatch) => {
    const response = await fetch(`/api/users/favorites`, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({ drinkId })
    })
    if (response.ok) {
        const data = await response.json();
        dispatch(makeFavorite(data.favoriteDrink))
        dispatch(favoriteDrink(data.numFavorites, data.favoriteDrink.drinkId))
    } //for the love of God learn error handling
}

export const unFavoriteThunk = (favoriteId, drinkId) => async (dispatch) => {
    const response = await fetch(`/api/users/favorites`, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'DELETE',
        body: JSON.stringify({ favoriteId, drinkId })
    })
    if (response.ok) {
        const data = await response.json();
        dispatch(unFavorite({ drinkId }))
        dispatch(favoriteDrink(data.numFavorites, data.drinkId))
    }
}

export const authenticate = () => async (dispatch) => {
    const response = await fetch('/api/auth/', {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    if (data.errors) {
        return;
    }
    dispatch(setUser(data))

}

export const login = (email, password) => async (dispatch) => {
    const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email,
            password
        })
    });
    const data = await response.json();
    if (data.errors) {
        return data;
    }
    dispatch(setUser(data));
    return {};
}

export const logout = () => async (dispatch) => {
    const response = await fetch("/api/auth/logout", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(removeUser());
};


export const signUp = (username, email, password) => async (dispatch) => {
    const response = await fetch("/api/auth/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username,
            email,
            password,
        }),
    });
    const data = await response.json();
    dispatch(setUser(data));
}

// reducer

const initialState = { user: null };

// useSelector(state => state.session.user)

export default function reducer(state = initialState, action) {
    let newState;

    switch (action.type) {
        case SET_USER:
            return { user: action.payload };
        case REMOVE_USER:
            return { user: null };
        case MAKE_FAVORITE:
            newState = Object.assign({}, state)
            newState.user.favorites[action.payload.drinkId] = action.payload
            return newState
        case UN_FAVORITE:
            newState = Object.assign({}, state)
            delete newState.user.favorites[action.payload.drinkId]
            return newState
        default:
            return state;
    }
}
