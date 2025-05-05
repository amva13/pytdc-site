import React from 'react';

type EmbeddedPageProps = {
  src: string; 
  title: string; 
};

const EmbeddedPage: React.FC<EmbeddedPageProps> = ({ src, title }) => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        width: '100%',
      }}
    >
      <iframe
        src={src}
        title={title}
        style={{
          width: '80%',
          height: '80%',
          border: 'none',
        }}
      ></iframe>
    </div>
  );
};

export default EmbeddedPage;
