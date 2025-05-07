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
            <p data-aos="fade-up">The platform introduces a model server, which provides unified access to model weights across distributed repositories 
              and standardized inference endpoints. The model server accelerates research workflows by exposing state-of-the-art, research-ready models 
              and training setups for biomedical representation learning models across modalities. A model store retrieval 
              API provides unified access to model weights stored in the Hugging Face Model Hub (https://huggingface.co/apliko), 
              Chan-Zuckerberg CELLxGENE Census fine-tuned models, and TDC storage. The model server also provides access to 
              model classes, tokenizer functions, and inference endpoints supporting PyTorch 
              and Hugging Face Transformers. Extracted embeddings, from either model server inference or pre-computed embedding 
              storage, are ready for downstream use by task-specific benchmarking modules. In this alpha release, the model server 
              exposes SoTA single-cell foundation models (scFMs).</p>
            <a data-aos="fade-up" className="btn dream-btn mt-30" href="https://huggingface.co/apliko" style={{borderColor: '#FFDF00'}}>HF Model Hub</a>
        </div>
    </div>
  );
}

export default SecWhoWeContant;