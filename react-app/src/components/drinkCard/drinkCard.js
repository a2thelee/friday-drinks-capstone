import { getDrinksThunk } from "../../store/drinks"
import { useDispatch, useSelector } from "./react-redux"
import React, { useEffect, useState } from 'react'

import "drinkCard.css"

const drinkCard = (props) => {
  const { userId } = useSelector(state => state.session.user.id)
}
