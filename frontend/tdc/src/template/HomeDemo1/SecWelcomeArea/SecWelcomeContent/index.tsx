import React from 'react';
import { DocElementTitle } from '../../../../data/data-containers/data-HomeDemo1';
import IcoDocs from './SecFAQ_Timeline/IcoDocs';


const SecWelcomeContent: React.FC = () => {
  return (
    <div className="welcome-content">
      <h1 style={{ color: '#3A9C94', fontFamily: 'sans-serif'}}>PyTDC-NextML</h1>
      <h1 style={{ color: '#FFB300', fontFamily: 'sans-serif' }}>A multimodal ML platform for biomedical foundation models</h1>
      <p></p>
      <h3 style={{ color: '#FFEFC2', fontFamily: 'sans-serif' }}>
        Learn more about our alpha release of PyTDC (scFMs) below! 
      </h3>
      <p>
      We present PyTDC, a machine-learning platform providing streamlined training, evaluation, and inference software for 
      biological foundation models to accelerate research in transfer learning method development in therapeutics.
      </p>
      <div className='row'>
        <div className="col-md-2"></div>
        <div className="col-md-8">
          <IcoDocs data={DocElementTitle} />
        </div>
        <div className='col-md-2'></div>
      </div>
      <p></p>
      <div className="dream-btn-group">
        <a href="/home" className="btn dream-btn" style={{borderColor: '#FFDF00', marginRight: '5px'}}>
          Go to PyTDC homepage
        </a>
      </div>
    </div>
  );
};

export default SecWelcomeContent;
