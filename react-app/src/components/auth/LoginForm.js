import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const errorPresence = (array) => {
    if (array.length) {
      return <div>The Email/Password Combination You Provided Was Incorrect!</div>
    }
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-form-container">
      <form className="login-form" onSubmit={onLogin}>
        <p className="login-text">Log in to Friday Drinks</p>
        <div>
          {errorPresence(errors)}
          {/* {errors.map((error) => (
            <div>The Email/Password Combination You Provided Was Incorrect!</div>
          ))} */}
        </div>
        <div>
          <label htmlFor="email">Email</label>
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
          />
          <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
