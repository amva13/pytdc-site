import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import Timeline from './Timeline';

type RoadmapData = {
  timelineClass: string;
  title: string;
  date_from: string;
  date_to: string;
  content: string;
};

type SecOurRoadmapProps = {
  data: RoadmapData[];
};

const SecOurRoadmap: React.FC<SecOurRoadmapProps> = ({ data }) => {
  return (
    <section className="roadmap" style={{ paddingBottom: 0 }} id="roadmap">
      <SectionHeading title="TDC-2 Roadmap" text="" />
      <div className="container">
        <div className="row">
          <div className="timeline-split">
            <div className="col-lg-12 col-md-12 col-sm-12">
              <div className="timeline section-box-margin">
                {data &&
                  data.map((item, key) => (
                    <Timeline
                      key={key}
                      timelineClass={item.timelineClass}
                      title={item.title}
                      date_from={item.date_from}
                      date_to={item.date_to}
                      content={item.content}
                    />
                  ))}
                <div className="circle"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default SecOurRoadmap;
