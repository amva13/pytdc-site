import Image from 'next/image';
import React from 'react';

type SingleCoolFactProps = {
  img: string;
  link: string;
  title: string;
};

const SingleCoolFact: React.FC<SingleCoolFactProps> = ({ img, link, title }) => {
  return (
    <div className="col-12 col-sm-6 col-md-3 col-lg-2" data-aos="fade-up">
      <div className="trust-item text-center" >
        <div className="ico-platform-logo" >
        <Image src={img} alt="X" layout="fill" />
        </div>
        <div className="dream-btn-group">
        <a data-aos="fade-up" href={link} className="btn dream-btn mt-30" style={{
          display: 'block',
          textAlign: 'center',
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: 'white',
          textDecoration: 'none',
          borderRadius: '5px',
          marginTop: '20px',
          maxWidth: '100%',
          boxSizing: 'border-box',
        }} >{title}</a>
        </div>
      </div>
    </div>
  );
};

export default SingleCoolFact;
