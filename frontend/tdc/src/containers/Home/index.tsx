import { useEffect } from 'react';
import data from '../../data/data-containers/data-Home';
import { handelTitle } from '../../utils';

import Footer from '../../layouts/Footer';
import SectionHeading from './SectionHeading';
import SectionDemo from './SectionDemo';

const HomeContainer: React.FC = () => {
  useEffect(() => {
    // Update the document title client-side
    handelTitle('PyTDC: A multimodal machine learning training, evaluation, and inference platform for biomedical foundation models');
  }, []);

  useEffect(() => {
    // Update body background style client-side
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
      <section className={`demo section-padding-100-0`} id="demo">
        <div className="container">
          <SectionHeading />
          <SectionDemo data={data} />
        </div>
      </section>
      <Footer />
    </>
  );
};

export default HomeContainer;
