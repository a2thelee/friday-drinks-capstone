import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { useHistory } from "react-router-dom"

import "./logout.css"

const LogoutButton = () => {
  const dispatch = useDispatch();
  const history = useHistory()
  const onLogout = async (e) => {
    await history.push("/")
    dispatch(logout());
  };

  return <button className="logout-button" onClick={onLogout}>Logout</button>;
};

export default LogoutButton;
