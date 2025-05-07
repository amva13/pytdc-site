import {useEffect} from 'react'

import Image from 'next/image';
import {Logo} from '../../data/data-layout/data-Header';

import {Addshrink , addActiveClass , OpenMenu , moveSmooth} from "../../utils/index"

const Header = () => {

  useEffect(() => {
      Addshrink()
  },[])

  useEffect(() => {
      OpenMenu()
  },[])

  useEffect(() => {
      moveSmooth()
  },[])

  return (
    <>
      <header className="header-area wow fadeInDown" data-wow-delay="0.2s">
        <div className="classy-nav-container breakpoint-off">
          <div className="container">
            <nav className="classy-navbar justify-content-between" id="dreamNav">
            <Image src={Logo.src} alt="logo" layout="fill" />
              <div className="classy-navbar-toggler">
                <span className="navbarToggler" onClick={addActiveClass}>
                    <span />
                    <span />
                    <span />
                </span>
              </div>
              <div className="classy-menu">
                <div className="classycloseIcon">
                  <div className="cross-wrap" onClick={addActiveClass}>
                      <span className="top" />
                      <span className="bottom" />
                  </div>
                </div>
                <div className="classynav">
                  <ul id="nav">
                    <li><a onClick={moveSmooth} href="#home" className="login-btn" style={{borderColor:'#FFEFC2', textAlign:'center', alignItems:'center'}}>Home</a></li>
                    <li><a onClick={moveSmooth} href="#about" className="login-btn" style={{borderColor:'#FFEFC2', textAlign:'center', alignItems:'center'}}>About</a></li>
                    <li><a onClick={moveSmooth} href="#services" className="login-btn" style={{borderColor:'#FFEFC2', textAlign:'center', alignItems:'center'}}>Features</a></li>
                    <li><a onClick={moveSmooth} href="#team" className="login-btn" style={{borderColor:'#FFEFC2', textAlign:'center', alignItems:'center'}}>Team</a></li>
                    {/* <li><a onClick={moveSmooth} href="#contact" className="login-btn" style={{borderColor:'#FFEFC2', textAlign:'center', alignItems:'center'}}>Contact</a></li> */}
                  </ul>
                  <a href="/home" className="btn login-btn ml-50" style={{borderColor:'#FFDF00'}}>Homepage</a>
                </div>
              </div>
            </nav>
          </div>
        </div>
      </header>
    </>
  );
}

export default Header;