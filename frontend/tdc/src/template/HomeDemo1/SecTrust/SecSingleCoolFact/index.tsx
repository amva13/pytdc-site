import React from 'react';
import { StaticImageData } from 'next/image';
import EmbeddedPage from '../../../../components/EmbeddedPage';

type CoolFactData = {
  img: StaticImageData;
  link: string;
  title: string;
};

type SecSingleCoolFactProps = {
  data: CoolFactData[];
}

const SecSingleCoolFact: React.FC<SecSingleCoolFactProps> = ({data}) => {
  return (
    <div
      style={{
        display: 'flex', 
        gap: '20px', 
        justifyContent: 'center', 
        flexWrap: 'wrap', 
        padding: '20px', 
      }}
    >
      {data &&
        data.map((item, key) => (
          <div
            key={key}
            style={{
              flex: '0 1 auto', 
              width: '300px', 
            }}
          >
            <EmbeddedPage src={item.link} title={item.title} />
          </div>
        ))}
    </div>
  );
};

export default SecSingleCoolFact;
