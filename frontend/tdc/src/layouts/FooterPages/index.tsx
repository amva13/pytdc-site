import{
  FooterLogo,
  FooterPattern,
  FooterBg1
} from '../../utils/allImgs'

import SecContact from './SecContact'
import SecIco from './SecIco'
import SecContent from './SecContent'

const Footer = () => {
    return (
      <footer className="footer-area bg-img" style={{backgroundImage: `url(${FooterPattern})`}}>
        <SecContact />
        <div className="footer-content-area" style={{backgroundImage: `url(${FooterBg1})`}}>
          <div className="container">
            <div className="row align-items-end">
            {/* <div className="row"> */}
              <div className="col-md-4">
                <SecIco logo={FooterLogo.src} />
              </div>
              <div className="col-md-4"></div>
              <div className="col-md-4"><SecContent /></div>
            </div>
          </div>
        </div>
      </footer>
    );
};

export default Footer