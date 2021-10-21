import React from "react";
import { useEffect, useContext } from "react";
import { userContext } from "../context/userContext";
import { useState } from "react";
export default function User(props) {
  const { values } = useContext(userContext);
  return (
    <div>
      <div className="container mr-5 ml-2 mx-auto bg-white shadow-xl">
        <div className="w-11/12 mx-auto">
          <div className="bg-white my-6">
            <table className="text-left w-full border-collapse">
              <thead>
                <tr>
                  <th className="py-4 px-6 bg-purple-400 font-bold uppercase text-sm text-white border-b border-grey-light">
                    Entity
                  </th>
                  <th className="py-4 px-6 text-center bg-purple-400 font-bold uppercase text-sm text-white border-b border-grey-light">
                    Value
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr className="hover:bg-grey-lighter">
                  <td className="py-4 px-6 border-b border-grey-light">Name</td>
                  <td className="py-4 px-6 text-center border-b border-grey-light">
                    {values.name}
                  </td>
                </tr>
                <tr className="hover:bg-grey-lighter">
                  <td className="py-4 px-6 border-b border-grey-light">
                    Profession
                  </td>
                  <td className="py-4 px-6 text-center border-b border-grey-light">
                    {values.profession}
                  </td>
                </tr>
                <tr className="hover:bg-grey-lighter">
                  <td className="py-4 px-6 border-b border-grey-light">
                    Email
                  </td>
                  <td className="py-4 px-6 text-center border-b border-grey-light">
                    {values.email}
                  </td>
                </tr>
                <tr className="hover:bg-grey-lighter">
                  <td className="py-4 px-6 border-b border-grey-light">Age </td>
                  <td className="py-4 px-6 text-center border-b border-grey-light">
                    {values.age}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
