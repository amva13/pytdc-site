import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import SecSingleCoolFact from './SecSingleCoolFact';
import { StaticImageData } from 'next/image';

type CoolFactData = {
  img: StaticImageData;
  link: string;
  title: string;
};

type SecTrustProps = {
  data: CoolFactData[];
};

const SecTrust: React.FC<SecTrustProps> = ({ data }) => {
  return (
    <section className="trust-section section-padding-100">
      <SectionHeading
        title="TDC-2 Talks"
        text="Seminars and presentations sharing the new tasks and architecture of TDC-2."
      />

      <div className="container">
        <div className="row">
          <SecSingleCoolFact data={data} />
        </div>
      </div>
    </section>
  );
};

export default SecTrust;
