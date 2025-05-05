import React from 'react';


const SecContent: React.FC = () => {
  return (
    <div className="col-12 col-md-7">
      {/* Content Info */}
      <div className="contact_info_area d-sm-flex justify-content-between">
        <div className="contact_info text-center wow fadeInUp" data-wow-delay="0.2s">
          <h5>NAVIGATE</h5>
          <a href="#"><p>Advertisers</p></a>
          <a href="#"><p>Developers</p></a>
          <a href="#"><p>Resources</p></a>
          <a href="#"><p>Company</p></a>
          <a href="#"><p>Connect</p></a>
        </div>
        <div className="contact_info text-center wow fadeInUp" data-wow-delay="0.3s">
          <h5>Legal</h5>
          <a href="#"><p>Advertiser Agreement</p></a>
          <a href="https://app.termly.io/document/eula/738f70ff-8eb1-4fac-adb5-6d632560c701"><p>Terms of Use</p></a>
          <a href="https://app.termly.io/document/privacy-policy/26081640-b4e9-4c59-9adc-1aaf5807891d"><p>Privacy Policy</p></a>
          <a href="#"><p>Technology Privacy</p></a>
          <a href="#"><p>Developer Agreement</p></a>
        </div>
        <div className="contact_info text-center wow fadeInUp" data-wow-delay="0.4s">
          <h5>Phone</h5>
          <p>Mailing Address: xx00 E. Union Ave</p>
          <p>Suite 1100. Denver, CO 80237</p>
          <p>+999 90932 627</p>
          <p>support@yourdomain.com</p>
        </div>
      </div>
    </div>
  );
};

export default SecContent;
