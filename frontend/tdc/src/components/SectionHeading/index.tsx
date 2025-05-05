import React from "react";

interface SectionHeadingProps {
  title: string;
  text: string;
  color1?: string;
  color2?: string;
}

const Span: React.FC = () => <span></span>;

const SectionHeading: React.FC<SectionHeadingProps> = ({ title, text, color1, color2 }) => {
  return (
    <div className="section-heading text-center">
      <div
        className="dream-dots justify-content-center"
        data-aos="fade-up"
        data-aos-delay="200"
      >
        {Array(7)
          .fill(null)
          .map((_, key) => (
            <Span key={key} />
          ))}
      </div>
      <h2
        data-aos="fade-up"
        data-aos-delay="300"
        style={{ color: color1 || "white" }}
      >
        {title}
      </h2>
      <p
        data-aos="fade-up"
        data-aos-delay="400"
        style={{ color: color2 || "white" }}
      >
        {text}
      </p>
    </div>
  );
};

export default SectionHeading;
