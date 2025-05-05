import { useEffect } from 'react';

import { 
  VerticalSocial,
  service_single_content,
  TeamMember,
  PartnersData,
  SingleCoolFact
} from '../../data/data-containers/data-HomeDemo1';
import { handelTitle } from '../../utils';

import Header from '../../layouts/Header';

import SecAboutUs from './SecAboutUs';
import SecAboutUsClient from './SecAboutUsClient';
import SecAboutUsClientPeople from './SecAboutUsClientPeople';
import SecDemoVideo from './SecDemoVideo';
import SecOurServices from './SecOurServices';
import SecPartners from './SecPartners';
import SecTeam from './SecTeam';
import SecTrust from './SecTrust';
import SecWelcomeArea from './SecWelcomeArea';
import SecVerticalSocial from './SecVerticalSocial';

import { 
  HomeDemo1About1,
  HomeDemo1Solution,
  HomeDemo1About1People,
} from '@/utils/allImgs';

const HomeDemo1: React.FC = () => {
  useEffect(() => {
    handelTitle('PyTDC: A multimodal machine learning training, evaluation, and inference platform for biomedical foundation models');
  }, []);

  useEffect(() => {
    // Set the body background image client-side
    if (typeof document !== 'undefined') {
      const body = document.getElementsByTagName('body')[0];
      if (document.title === 'PyTDC: A multimodal machine learning training, evaluation, and inference platform for biomedical foundation models') {
        body.style.backgroundImage =
          'linear-gradient(180deg,#240044 0,#0f0240 25%,#400959 40%,#0f0240 65%,#0f0240)';
      } else {
        body.style.backgroundImage =
          'linear-gradient(to right, #4834d4, #341f97)';
      }
    }
  }, []);

  return (
    <>
      <Header />
      <div className="HomeDemo1">
        <SecWelcomeArea />
        <SecVerticalSocial data={VerticalSocial} />
        <SecTrust data={SingleCoolFact} />
        <SecAboutUsClient img={HomeDemo1About1.src} />
        <SecAboutUs img={HomeDemo1Solution.src} />
        <SecAboutUsClientPeople img={HomeDemo1About1People.src} />
        <div className="clearfix" />
        <SecDemoVideo />
        <div className="clearfix" />
        <SecOurServices data={service_single_content} />
        <SecTeam data={TeamMember} />
        <SecPartners data={PartnersData} />
      </div>
    </>
  );
};

export default HomeDemo1;
