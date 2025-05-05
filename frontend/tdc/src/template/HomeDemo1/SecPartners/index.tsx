import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import { StaticImageData } from 'next/image';

type PartnerData = {
  link: string;
  img: StaticImageData;
};

type SecPartnersProps = {
  data: PartnerData[];
};

const SecPartners: React.FC<SecPartnersProps> = () => {
  return (
    <section className="partners">
      <SectionHeading
        title="Our Collaborators"
        text="To be disclosed"
      />

      {/* <div className="container">
        {data &&
          data.map((item, key) => (
            <div className="row" key={key}>
              <div className="col-sm-4"></div>
              <div className="col-sm-4" data-aos="fade-up">
                <div className="partner-box">
                  <a href={item.link}>
                    <Image src={item.img.src} alt={`Collaborator ${key}`} layout="fill" className="center-block" />
                  </a>
                </div>
              </div>
              <div className="col-sm-4"></div>
            </div>
          ))}
      </div> */}
    </section>
  );
};

export default SecPartners;
