import React from 'react';
import SectionHeading from './SectionHeading';
import SecGroup from './SecGroup';
import SecTelegramText from './SecTelegramText';
import SecSocialList from './SecSocialList';

type SecSubscribeProps = {
  data: { icoName: string }[];
};

const SecSubscribe: React.FC<SecSubscribeProps> = ({ data }) => {
  return (
    <section className="container" style={{ paddingBottom: '0px' }} id="start">
      <div className="subscribe">
        <div className="row">
          <div className="col-sm-12">
            <div className="subscribe-wrapper">
              <SectionHeading />
              <div className="service-text">
                <SecGroup />
                <SecTelegramText />
                <SecSocialList data={data} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default SecSubscribe;
