import Image from 'next/image';
import React from 'react';

type SecWelcomeMeterProps = {
  img: string;
};

const SecWelcomeMeter: React.FC<SecWelcomeMeterProps> = ({ img }) => {
  return (
    <div className="col-12 col-lg-6">
      <div className="welcome-meter" data-aos="fade-up">
        <Image src={img} className="center-block" alt="Welcome Meter" layout="fill" />
      </div>
    </div>
  );
};

export default SecWelcomeMeter;
