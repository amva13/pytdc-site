import React from 'react';


const SecVideoArea: React.FC = () => {
  return (
    <div
      className="col-lg-8 offset-lg-2 col-md-10 offset-md-1 col-sm-12"
      data-aos="fade-up"
    >
      <div className="welcome-video-area">
        <div className="welcome-thumb">
        </div>
        <div className="video-icon">
          <a
            href="https://youtu.be/ZuCOhEZtaOw?si=Kh5DiaUNdkvznYSh"
            className="btn dream-btn video-btn"
            id="videobtn"
          >
            <i className="fa fa-play"></i>
          </a>
        </div>
      </div>
    </div>
  );
};

export default SecVideoArea;
