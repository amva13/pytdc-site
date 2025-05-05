import React from 'react';

const SecGroup: React.FC = () => {
  return (
    <div className="col-lg-8 col-lg-offset-2 col-md-8 offset-md-2 col-xs-12 text-center">
      <div className="group">
        <label htmlFor="email-input">Enter your email</label>
        <input id="email-input" type="text" name="subject" required />
        <span className="highlight"></span>
        <span className="bar"></span>
        <button className="dream-btn" aria-label="Submit email">
          <i className="fa fa-paper-plane-o"></i>
        </button>
      </div>
    </div>
  );
};

export default SecGroup;
