import React from 'react';
import { DocElementTitle } from '../../../../data/data-containers/data-HomeDemo1';
import IcoDocs from './SecFAQ_Timeline/IcoDocs';


const SecWelcomeContent: React.FC = () => {
  return (
    <div className="welcome-content">
      <h1 style={{ color: '#3A9C94', fontFamily: 'sans-serif'}}>PyTDC: Therapeutics Commons</h1>
      <h1 style={{ color: '#FFB300', fontFamily: 'sans-serif' }}>A multimodal ML platform for biomedical foundation models</h1>
      <h3 style={{ color: '#FFDF00', fontFamily: 'sans-serif' }}>COMING SOON</h3>
      <p></p>
      <h3 style={{ color: '#FFEFC2', fontFamily: 'sans-serif' }}>
        Learn more about our alpha release of TDC-2 below! 
      </h3>
      <p>
      We present PyTDC, a first-of-its-kind machine-learning platform for biomedical foundation models across multiple modalities.
      PyTDC is open-source software providing infrastructure to streamline biomedical AI training, benchmarking, and inferencing. It 
      integrates multimodal biological data, single-cell analysis biomarkers, and a broad range of machine learning tasks in 
      therapeutics. 
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
        <a href="https://tdcommons.ai" className="btn dream-btn" style={{borderColor: '#FFDF00', marginRight: '5px'}}>
          Go to TDC homepage
        </a>
        <a></a>
        <a href="http://tdcommons.ai/news" className="btn dream-btn mr-3" style={{borderColor: '#FFDF00', marginLeft: '5px'}}>
          See recent news
        </a>
      </div>
    </div>
  );
};

export default SecWelcomeContent;
