import React from 'react';

const Form: React.FC = () => {
  return (
    <div className="row justify-content-center">
      <div className="col-12 col-md-10 col-lg-8">
        <div className="contact_form">
          <form action="mailto:kaela@alphunt.com" method="post" id="main_contact_form" noValidate>
            <div className="row">
              <div className="col-12">
                <div id="success_fail_info" />
              </div>
              <div className="col-12 col-md-6" data-aos="fade-up">
                <div className="group wow fadeInUp" data-wow-delay="0.2s">
                  <label htmlFor="name">Name</label>
                  <input type="text" name="name" id="name" required />
                  <span className="highlight" />
                  <span className="bar" />
                </div>
              </div>
              <div className="col-12 col-md-6" data-aos="fade-up">
                <div className="group wow fadeInUp" data-wow-delay="0.3s">
                  <label htmlFor="email">Email</label>
                  <input type="text" name="email" id="email" required />
                  <span className="highlight" />
                  <span className="bar" />
                </div>
              </div>
              <div className="col-12" data-aos="fade-up">
                <div className="group wow fadeInUp" data-wow-delay="0.4s">
                  <label htmlFor="subject">Subject</label>
                  <input type="text" name="subject" id="subject" required />
                  <span className="highlight" />
                  <span className="bar" />
                </div>
              </div>
              <div className="col-12" data-aos="fade-up">
                <div className="group wow fadeInUp" data-wow-delay="0.5s">
                  <label htmlFor="message">Message</label>
                  <textarea name="message" id="message" required defaultValue={""} />
                  <span className="highlight" />
                  <span className="bar" />
                </div>
              </div>
              <div className="col-12 text-center wow fadeInUp" data-wow-delay="0.6s">
                <a
                  className="btn dream-btn"
                  data-aos="fade-up"
                  href="https://forms.gle/VVwrxRcgQdHrH84x8"
                >
                  Join Waitlist
                </a>
                <button type="submit" className="btn dream-btn" data-aos="fade-up">
                  Send Message
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Form;
