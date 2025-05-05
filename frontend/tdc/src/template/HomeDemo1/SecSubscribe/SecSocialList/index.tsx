import React from 'react';

type LiAProps = {
  icoName: string;
};

const Li_A: React.FC<LiAProps> = ({ icoName }) => (
  <li>
    <a href="#">
      <i className={icoName}></i>
    </a>
  </li>
);

type SecSocialListProps = {
  data: { icoName: string }[];
};

const SecSocialList: React.FC<SecSocialListProps> = ({ data }) => {
  return (
    <div className="col-lg-5 col-sm-12 text-center">
      <ul className="list-unstyled list-inline social-list">
        {data &&
          data.map((item, key) => (
            <Li_A key={key} icoName={item.icoName} />
          ))}
      </ul>
    </div>
  );
};

export default SecSocialList;
