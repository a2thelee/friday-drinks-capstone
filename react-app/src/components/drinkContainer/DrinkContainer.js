import React, { useState } from "react"
import { Modal } from "../../context/Modal"
import DrinkCard from "../drinkCard/DrinkCard"
import { showForm } from "../../store/drinks"
import { useDispatch } from "react-redux"

const DrinkContainer = ({ drink }) => {
  const dispatch = useDispatch()
  const [showModal, setShowModal] = useState(drink?.show)

  const modalClose = async (event) => {
    event.stopPropagation()
    await dispatch(showForm({ showForm: false, key: drink.id }))
    setShowModal(drink.show)
    // dispatch(showForm())
  }

  const modalOpen = async () => {
    await dispatch(showForm({ showForm: true, key: drink.id }))
    setShowModal(drink.show)
  }

  return (

    <div
      className="single-drink-container"
      key={drink?.id}
      onClick={modalOpen}
    >{showModal && drink.show && (
      <Modal onClose={modalClose}>
        <DrinkCard drink={drink} />
      </Modal>
    )}
      <div className="drink-photo-container">
        <img
          src={drink?.photo_url}
          className="drink-photo"
          alt="drink-pic" />
      </div>
      <div className="drink-text-div">
        <p className="drink-container-name">{drink?.name}</p>
      </div>
    </div>
  )
}

export default DrinkContainer
