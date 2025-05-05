import React from 'react';

type LI_AProps = {
  nameIco: string;
  url: string;
};

const LI_A: React.FC<LI_AProps> = ({ nameIco, url }) => (
  <li>
    <a href={url}>
      <i className={nameIco} aria-hidden="true"></i>
    </a>
  </li>
);

type SecVerticalSocialProps = {
  data: { nameIco: string; link: string }[];
};

const SecVerticalSocial: React.FC<SecVerticalSocialProps> = ({ data }) => {
  return (
    <div className="vertical-social">
      <ul>
        {data &&
          data.map((item, index) => (
            <LI_A key={index} nameIco={item.nameIco} url={item.link} />
          ))}
      </ul>
    </div>
  );
};

export default SecVerticalSocial;
