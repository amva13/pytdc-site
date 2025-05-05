import React from 'react';
import DocElement from './DocElement';

type IcoDocsProps = {
  data: { title: string; link: string }[];
};

const IcoDocs: React.FC<IcoDocsProps> = ({ data }) => {
  return (
    <div className="ico-docs">
      <div>
        {data &&
          data.map((item, key) => (
            <DocElement key={key} title={item.title} link={item.link} />
          ))}
      </div>
    </div>
  );
};

export default IcoDocs;
