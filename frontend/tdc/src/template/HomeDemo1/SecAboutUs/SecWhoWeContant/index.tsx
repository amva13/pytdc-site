const Span = () => <span></span>
const SecWhoWeContant = () => {

  return (
    <div className="col-12 col-lg-6">
        <div className="who-we-contant">
            <div className="dream-dots" data-aos="fade-up">
              <Span />
              <Span /> 
              <Span /> 
              <Span /> 
              <Span /> 
              <Span /> 
              <Span /> 
            </div>
            <h4 data-aos="fade-up">PyTDC API-first Architecture</h4>
            <p data-aos="fade-up">A collection of multimodal continually updated heterogeneous data sources is unified under the 
              introduced &quot;API-first-dataset&quot; architecture. Inspired by API-first design, this microservice architecture is 
              implemented using the model-view-controller design pattern to enable multimodal data views 
              under a domain-specific-language.</p>
            <a className="btn dream-btn mt-30" href="https://colab.research.google.com/drive/1xTgBwKUfP2b8j6Fqh28M2GUp2ScfENMX?usp=sharing" style={{borderColor: '#FFDF00'}}>CELLxGENE notebook</a>
        </div>
    </div>
  );
}

export default SecWhoWeContant;