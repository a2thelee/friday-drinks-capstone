import React, { useState } from "react"
import { Modal } from "../../context/Modal"
import DrinkCard from "../drinkCard/DrinkCard"

import "./DrinkContainer.css"

const DrinkContainer = ({ drink }) => {
  const [showModal, setShowModal] = useState(false)


  const modalClose = (event) => {
    event.stopPropagation()
    setShowModal(false)
  }

  const modalOpen = () => {
    setShowModal(true)
  }

  return (

    <div
      className="single-drink-container"
      key={drink.id}
      onClick={modalOpen}
    >{showModal && (
      <Modal onClose={modalClose}>
        <DrinkCard drink={drink} />
      </Modal>
    )}
      <div className="drink-photo-container">
        <img
          src={drink.photo_url}
          className="drink-photo"
          alt="drink-pic" />
      </div>
      <div className="drink-text-div">
        <p>{drink.name}</p>
      </div>
    </div>
  )
}

export default DrinkContainer
