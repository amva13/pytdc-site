import React from 'react';

type SingleMissionProps = {
  text: string;
};

const SingleMission: React.FC<SingleMissionProps> = ({ text }) => {
  return (
    <div className="col-12 col-md-4">
      <div className="single-mission wow fadeInUp" data-wow-delay="0.2s">
        <i className="ti-shine"></i>
        <h6>Quality</h6>
        <p>{text}</p>
      </div>
    </div>
  );
};

export default SingleMission;
