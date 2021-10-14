import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../assets/styles/landing.css';

const Landing = () => {
  // hooks
  const [loged, setLoged] = useState(0);

  const handleButton = () => {
    if (loged === 1) {
      setLoged(0);
    } else {
      setLoged(1);
    }
  };

  return (
    <>
      <Header isLoged={loged} />
      <h1 className='title-landing'> Hello vero 4!</h1>
      <button type='button' onClick={handleButton}> hacer click </button>
      {(loged === 1) ?
        (
          <p>
            El usuario esta logeado
          </p>
        ) :
        (
          <p>
            El usuario NO esta logeado.
          </p>
        )}
      <Footer />
    </>
  );
};

export default Landing;
