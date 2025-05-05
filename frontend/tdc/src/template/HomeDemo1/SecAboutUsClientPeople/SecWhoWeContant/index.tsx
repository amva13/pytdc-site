const Span = () => <span></span>
// src/template/HomeDemo1/SecAboutUsClient/SecWhoWeContant/index.jsx
const SecWhoWeContantPeople = () => {

  return (
    <div className="col-12 col-lg-6">
        <div className="who-we-contant">
            <div className="dream-dots">
            <Span />
            <Span />
            <Span />
            <Span />
            <Span />
            <Span />
            <Span />
            </div>
            <h4 data-aos="fade-up">Single-cell Therapeutics AI</h4>
            <p data-aos="fade-up">TDC-2 presents datasets, tools, models, and benchmarks integrating cell-type-specific contextual features with ML tasks across therapeutics. We present four tasks for contextual learning at single-cell resolution.</p>
            {/* <p data-aos="fade-up">Your data is untraceable. Your identity anonymized. No spam, ads, or unsolicited inboxes.</p> */}
            <a data-aos="fade-up" className="btn dream-btn mt-30" href="https://tdcommons.ai/multi_pred_tasks/scdti" style={{borderColor: '#FFDF00'}}>Single-cell Drug Target Nomination</a>
        </div>
    </div>
  );
}

export default SecWhoWeContantPeople;