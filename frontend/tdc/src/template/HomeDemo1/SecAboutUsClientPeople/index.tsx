import React from 'react';
import SecWelcomeMeter from './SecWelcomeMeter';
import SecWhoWeContantPeople from './SecWhoWeContant';

type SecAboutUsClientPeopleProps = {
  img: string;
};

const SecAboutUsClientPeople: React.FC<SecAboutUsClientPeopleProps> = ({ img }) => {
  return (
    <section className="about-us-area section-padding-0-100 clearfix" id="about">
      <div className="container">
        <div className="row align-items-center">
          <SecWelcomeMeter img={img} />
          <SecWhoWeContantPeople />
        </div>
      </div>
    </section>
  );
};

export default SecAboutUsClientPeople;
