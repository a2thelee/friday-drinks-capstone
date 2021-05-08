import React, {useEffect, useState} from 'react'
import {useSelector} from 'react-redux'
import {Redirect} from 'react-router-dom'
import {getFavoriteDrinksThunk} from "../../store/favorites"

const profile = () => {
  const userId = useSelector(state => state.session.user.id)
  const 
}
