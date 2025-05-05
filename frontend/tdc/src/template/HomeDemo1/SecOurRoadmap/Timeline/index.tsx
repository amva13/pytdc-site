import React from 'react';

type TimelineProps = {
  timelineClass: string;
  title: string;
  date_from: string;
  date_to: string;
  content: string;
};

const Timeline: React.FC<TimelineProps> = ({
  timelineClass,
  title,
  date_from,
  date_to,
  content,
}) => {
  return (
    <div className={timelineClass}>
      <h3>{title}</h3>
      <span className="date">{date_from}</span> <span className="between">to</span>{' '}
      <span className="date">{date_to}</span>
      <p>{content}</p>
    </div>
  );
};

export default Timeline;
