import React from 'react';

type DocElementProps = {
  title: string;
  link: string;
};

const DocElement: React.FC<DocElementProps> = ({ title, link }) => {
  return (
    <div className="col-md-6 col-sm-6 col-xs-12" data-aos="fade-up">
      <a href={link}>
        <div className="doc-element">
          <a className="document-entry" href={link}>
            <span className="title">{title}</span>
          </a>
        </div>
      </a>
    </div>
  );
};

export default DocElement;
