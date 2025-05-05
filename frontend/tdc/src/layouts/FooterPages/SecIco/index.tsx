import Image from 'next/image';
import React from 'react';

type SecIcoProps = {
  logo: string;
};

const SecIco: React.FC<SecIcoProps> = ({ logo }) => {
  const styles = {
    baseText: {
      fontWeight: 'bold',
    },
    innerText: {
      color: 'white',
    },
  };

  return (
    <div className="col-sm-12">
      <div className="footer-copywrite-info">
        <div className="copywrite_text wow fadeInUp" data-wow-delay="0.2s">
          <div className="footer-logo">
            <a href="#"><Image src={logo} alt="logo" layout="fill" /></a>
          </div>
          <p style={styles.innerText}>Copyright &copy; Apliko Inc. 2022. All rights reserved.</p>
        </div>
        <div className="footer-social-info wow fadeInUp" data-wow-delay="0.4s">
          <a href="https://www.instagram.com/apliko_io/"><i className="fa fa-instagram" aria-hidden="true" /></a>
          <a href="https://twitter.com/Alphunt_"> <i className="fa fa-twitter" aria-hidden="true" /></a>
          <a href="https://www.linkedin.com/company/apliko-io"><i className="fa fa-linkedin" aria-hidden="true" /></a>
          <a href="https://discord.gg/ZJ67MtXag4"><i className="fa fa-server" aria-hidden="true" /></a>
          <a href="https://www.crunchbase.com/organization/apliko-io"><i className="fa fa-hacker-news" aria-hidden="true" /></a>
        </div>
      </div>
    </div>
  );
};

export default SecIco;