import React from 'react';

const Header = ({ isLoged }) => {

  return (
    <header className='header-container'>
      <div className='header-container-logo'>
        <p>VERO</p>
      </div>
      <div className='header-container-menu'>
        {!isLoged ?
          (
            <ul>
              <li>About us</li>
              <li>Log In</li>
              <li>Register</li>
            </ul>
          ) :
          (
            <ul>
              <li>About us</li>
              <li>Profile</li>
              <li>Notifications</li>
              <li>Log out</li>
            </ul>
          )}

      </div>
    </header>
  );
};

export default Header;
