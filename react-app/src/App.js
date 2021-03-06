import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import User from "./components/User";
import CreateDrinkForm from "./components/CreateDrinkForm/CreateDrinkForm.js"
import SingleDrinkPage from "./components/NavBar/SingleDrinkPage"

import Home from "./components/Home/Home"
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>

        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>

        <Route path="/" exact={true}>
          <Home />
        </Route>

        <Route path="/create_drinks" exact={true}>
          <CreateDrinkForm />
        </Route>

        <Route path="/drinks/:id" exact={true}>
          <SingleDrinkPage />
        </Route>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
