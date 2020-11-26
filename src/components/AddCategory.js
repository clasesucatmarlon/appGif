import React, { useState } from 'react';
import PropTypes from 'prop-types';

export const AddCategory = ({setCateg}) => {
   const [inputValue, setinputValue] = useState('');

   // Escribir dentro del la caja de texto.  Al llamar a esta función se actualiza de una vez el inputValue
   const handleInputChange = (e) => {
      setinputValue(e.target.value)
   }

   // Manejar el evento ENTER
   const handleSubmit = (e) => {
      e.preventDefault();  // Prevenir el comportamiento por defecto del formulario
      if (inputValue.trim().length > 2) {
         setCateg( cat => [inputValue, ...cat, ] );
         setinputValue('');
      }
   }

   return (
      <form onSubmit={handleSubmit}>
         <input
            type='text'
            value={inputValue}
            onChange={handleInputChange}
         />
      </form>
   )
}

AddCategory.propTypes = {
   setCateg: PropTypes.func.isRequired
}
