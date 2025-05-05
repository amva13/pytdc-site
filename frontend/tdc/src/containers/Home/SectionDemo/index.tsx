import React from "react";
import Demo from "./Demo";
import { StaticImageData } from "next/image";

interface SectionDemoProps {
  data: {
    img: StaticImageData;
    path: string;
  }[];
}

const SectionDemo: React.FC<SectionDemoProps> = ({ data }) => {
  return (
    <div className="row">
      {data &&
        data.map((item, key) => (
          <Demo key={key} img={item.img.src} path={item.path} />
        ))}
    </div>
  );
};

export default SectionDemo;
