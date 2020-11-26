import { useState, useEffect } from 'react';
import { getGifs } from '../helpers/GetGifs';

export const useFetchGifs = (category) => {
   const [state, setState] = useState({
      data: [],
      loading: true
   });

   // Ejecutar la petición Fetch solo una vez
   useEffect(() => {
      getGifs(category).then(imgs => {
         setTimeout(() => {
            setState({
               data: imgs,
               loading: false
            });
         }, 3000);
      });
   }, [category])

   return state; // { data: [], loading: true}



}