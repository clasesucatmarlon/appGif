import React from 'react';
import { GifGridItems } from './GifGridItems';
import { useFetchGifs } from "../hooks/useFetchGifs";

export const GifGrid = ({ category }) => {
   const { data: images, loading } = useFetchGifs(category);
   return (
      <>
         { loading && <p className='animate__animated animate__flash animate__delay-3s'>Cargando información ...</p>}
         <div className='title'>
            <h3 className='animate__animated animate__fadeInDownBig'>{category}</h3>
         </div>

         <div className='card-grid'>
            {
               images.map(imag => (
                  <GifGridItems
                     key={imag.id}
                     {...imag}
                  />
               ))
            }
         </div>
      </>
   )
}
