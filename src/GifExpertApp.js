import React, { useState } from 'react';
import { AddCategory } from './components/AddCategory';
import { GifGrid } from './components/GifGrid';

const GifExpertApp = () => {

    const [categories, setCategories] = useState(['dogs'])

    /*     //AGREGAR NUEVO ELEMENTO AL ARRAY
        const handleAdd = () => {
            setCategories([...categories, 'Hola'])
        } */



    return (
        <>
            <h2>GifExpertApp</h2>
            <AddCategory setCateg={setCategories} />
            <hr />

            {/* <button onClick={handleAdd}>Agregar</button> */}

            {
                categories.map((category) => (
                    <GifGrid
                        key={category}
                        category={category} />
                ))
            }

        </>
    )
}

export default GifExpertApp;
