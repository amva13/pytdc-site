import React from 'react';
import SecWelcomeMeter from './SecWelcomeMeter';
import SecWhoWeContant from './SecWhoWeContant';

type SecAboutUsClientProps = {
  img: string;
};

const SecAboutUsClient: React.FC<SecAboutUsClientProps> = ({ img }) => {
  return (
    <section className="about-us-area section-padding-0-100 clearfix" id="about">
      <div className="container">
        <div className="row align-items-center">
          <SecWelcomeMeter img={img} />
          <SecWhoWeContant />
        </div>
      </div>
    </section>
  );
};

export default SecAboutUsClient;
