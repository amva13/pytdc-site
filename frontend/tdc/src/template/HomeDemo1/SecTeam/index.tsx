import React from 'react';
import SectionHeading from '../../../components/SectionHeading';
import { StaticImageData } from 'next/image';

type TeamMember = {
  img: StaticImageData;
  title: string;
  text: string;
};

type SecTeamProps = {
  data: TeamMember[];
};

const SecTeam: React.FC<SecTeamProps> = () => {
  return (
    <section className="our_team_area section-padding-0-0 clearfix" id="team">
      <div className="container">
        <div className="row">
          <div className="col-12">
            <SectionHeading
              title="PyTDC Team"
              text="To be disclosed"
              color1="white"
              color2="white"
            />
          </div>
        </div>

        {/* <div className="row">
          {data &&
            data.map((item, key) => (
              <div className="col-sm-12" data-aos="fade-up" key={key}>
                <div className="single-team-member">
                  <div className="team-member-thumb">
                    <Image src={item.img.src} className="center-block" alt="Team Member" layout="fill" />
                  </div>
                  <div className="team-info">
                    <h5>{item.title}</h5>
                    <p>{item.text}</p>
                  </div>
                  <div className="team-social-icon">
                    <a href="http://alejandrovelez.com">
                      <i className="fa fa-id-badge"></i>
                    </a>
                    <a href="#">
                      <i className="fa fa-twitter"></i>
                    </a>
                    <a href="#">
                      <i className="fa fa-instagram"></i>
                    </a>
                    <a href="#">
                      <i className="fa fa-facebook"></i>
                    </a>
                    <a href="#">
                      <i className="fa fa-skype"></i>
                    </a>
                  </div>
                </div>
              </div>
            ))}
        </div> */}
      </div>
    </section>
  );
};

export default SecTeam;
