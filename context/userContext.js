import { createContext, useContext, useState } from "react";
const userContext = createContext();

const userProvider = ({ children }) => {
  const [values, setValues] = useState({
    name: "",
    profession: "",
    email: "",
    age: "",
  });

  const set = (name) => {
    return ({ target: { value } }) => {
      setValues((oldValues) => ({ ...oldValues, [name]: value }));
    };
  };

  return (
    <userContext.Provider
      value={{
        values,
        set,
      }}
    >
      {children}
    </userContext.Provider>
  );
};

export { userProvider, userContext };
