import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import SecVideoArea from './SecVideoArea';


const SecDemoVideo: React.FC = () => {
  return (
    <section className="demo-video section-before section-padding-100">
      <div className="container">
        <SectionHeading
          title="Watch the TDC Intro Video"
          text="A presentation by members of the TDC team introducing Therapeutics Data Commons (TDC-1)"
        />
        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            margin: 0,
            }}
      >
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ZuCOhEZtaOw?si=Kh5DiaUNdkvznYSh" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen></iframe>
        </div>
        <p></p>
        <SecVideoArea />
      </div>
    </section>
  );
};

export default SecDemoVideo;
