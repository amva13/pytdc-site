const Span = () => <span></span>
// src/template/HomeDemo1/SecAboutUsClient/SecWhoWeContant/index.jsx

const SecWhoWeContant = () => {

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
            <h4 data-aos="fade-up">PyTDC Model Server</h4>
            <p data-aos="fade-up">The PyTDC model server streamlines retrieval, inferencing, and training setup for an array 
              of context-aware biological foundation models and models spanning multiple modalities. A model store retrieval 
              API provides unified access to model weights stored in the Hugging Face Model Hub (https://huggingface.co/tdc), 
              Chan-Zuckerberg CELLxGENE Census fine-tuned models, and TDC storage. The model server also provides access to 
              model classes, tokenizer functions, and inference endpoints supporting PyTorch 
              and Hugging Face Transformers. Extracted embeddings, from either model server inference or pre-computed embedding 
              storage, are ready for downstream use by task-specific benchmarking modules.</p>
            <a data-aos="fade-up" className="btn dream-btn mt-30" href="https://huggingface.co/tdc" style={{borderColor: '#FFDF00'}}>HF Model Hub</a>
        </div>
    </div>
  );
}

export default SecWhoWeContant;